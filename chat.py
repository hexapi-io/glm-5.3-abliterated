import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MODEL = "glm-5.3-abliterated"
ENDPOINT = "https://api.hexapi.io/v1/chat/completions"
DEMO_REPORT = (
    "On a narrow display in landscape mode, open the settings drawer and "
    "change the email notification toggle. The Save button disappears."
)


def ticket_from_completion(completion):
    choices = completion.get("choices")
    if not choices:
        raise ValueError("HEX did not return a completion.")

    answer = choices[0]
    if answer.get("finish_reason") == "length":
        raise ValueError("The response reached the output limit before finishing.")

    content = answer.get("message", {}).get("content")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("The completion did not contain text.")

    content = content.strip()
    if content.startswith("```") and content.endswith("```"):
        content = content.split("\n", 1)[-1].removesuffix("```").strip()

    ticket = json.loads(content)
    fields = ("title", "expected", "actual")
    if not isinstance(ticket, dict) or not all(
        isinstance(ticket.get(field), str) and ticket[field].strip() for field in fields
    ):
        raise ValueError("The response is missing one or more ticket fields.")

    steps = ticket.get("steps")
    if not isinstance(steps, list) or not steps or not all(
        isinstance(step, str) and step.strip() for step in steps
    ):
        raise ValueError("The response did not provide a non-empty list of steps.")

    return {field: ticket[field] for field in ("title", "steps", "expected", "actual")}


def main():
    parser = argparse.ArgumentParser(description="Convert a report to a bug ticket with HEX.")
    parser.add_argument("report", type=Path, nargs="?", help="UTF-8 text file with a bug report")
    args = parser.parse_args()

    key = os.environ.get("HEX_API_KEY")
    if not key:
        parser.exit(1, "Set HEX_API_KEY before running this example.\n")

    try:
        report = args.report.read_text(encoding="utf-8-sig") if args.report else DEMO_REPORT
        if not report.strip():
            raise ValueError("The report is empty.")

        body = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Return a JSON object with title, steps (an array of strings), "
                        "expected, and actual. Use only details from the report. "
                        "Write 'Unknown' for missing details."
                    ),
                },
                {"role": "user", "content": report},
            ],
            "reasoning_effort": "low",
            "max_tokens": 2048,
        }
        request = Request(
            ENDPOINT,
            data=json.dumps(body).encode("utf-8"),
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=120) as response:
            ticket = ticket_from_completion(json.load(response))
        print(json.dumps(ticket, ensure_ascii=False, indent=2))
    except HTTPError as error:
        parser.exit(1, f"HEX returned HTTP {error.code}. See https://hexapi.io/status.\n")
    except (URLError, TimeoutError):
        parser.exit(1, "Could not complete the request to HEX.\n")
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()

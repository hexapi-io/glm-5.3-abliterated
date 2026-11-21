# Example ticket output

The [Python example](chat.py) requests a JSON object with a title, steps, expected behavior, and actual behavior. This is an illustrative output for the demo report.

~~~json
{
  "title": "Save disappears in landscape view",
  "steps": [
    "Open settings on a narrow display in landscape mode.",
    "Change the email notification toggle."
  ],
  "expected": "Unknown",
  "actual": "The Save button disappears."
}
~~~

The example validates the field types and prints JSON to stdout. Review the steps and expected behavior before creating a ticket.

[Run the example](README.md#run-the-example) · [Integration details](INTEGRATION.md)

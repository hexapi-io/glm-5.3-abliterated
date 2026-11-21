# Integrating GLM 5.3 Abliterated

## Try a direct request

Set `HEX_API_KEY` in your terminal. The command below uses bash-compatible quoting. For Windows PowerShell, run [chat.py](chat.py) instead.

~~~bash
curl --fail-with-body https://api.hexapi.io/v1/chat/completions \
  -H "Authorization: Bearer $HEX_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{
    "model": "glm-5.3-abliterated",
    "reasoning_effort": "low",
    "max_tokens": 2048,
    "messages": [
      {"role": "user", "content": "Write a concise bug title. In landscape mode, the Save button disappears after opening Settings."}
    ]
  }'
~~~

Read `choices[0].message.content` for text. The Python example requests four JSON fields and validates the result before printing it. Treat the generated fields as suggestions and review them before inserting a ticket into a tracker.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| HTTP 401 | Make sure the bearer key is a HEX key and is set in the terminal running the example. |
| Model unavailable | Check the account's `GET /v1/models` result and current HEX status. |
| `finish_reason` is `length` | Shorten the report or raise the output limit within your budget. |
| Missing JSON fields | Inspect the original input and ensure the response finished before consuming the result. |
| Persistent 5xx | Check status and share the request ID, model, and timestamp with HEX support. |

[API reference](https://hexapi.io/docs) · [Service status](https://hexapi.io/status) · [Support](https://hexapi.io/support)

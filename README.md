[![GLM 5.3 Abliterated on HEX API](cover.png)](https://hexapi.io/models)

# GLM 5.3 Abliterated API

Call GLM 5.3 Abliterated on the HEX API with an OpenAI-compatible client. The Python example turns a rough bug report into a JSON ticket with a title, steps, expected behavior, and actual behavior. The integration guide shows the equivalent curl request.

| Setting | Value |
| --- | --- |
| Model ID | `glm-5.3-abliterated` |
| Endpoint | `POST https://api.hexapi.io/v1/chat/completions` |
| Authentication | HEX API key in `HEX_API_KEY` |
| Example runtime | Python 3.10+ with the standard library |

## Run the example

Set `HEX_API_KEY` in your terminal using a key from your HEX account. Then run:

~~~bash
python chat.py
~~~

You can pass a bug-report text file instead:

~~~bash
python chat.py issue.txt
~~~

The script prints a JSON ticket to stdout. Use fictional data for your first run. Each invocation makes one billable request.

| Resource | What it covers |
| --- | --- |
| [Python example](chat.py) | Submit a report and validate the returned JSON shape |
| [Example output](EXAMPLE-OUTPUT.md) | Inspect the JSON ticket returned by the example |
| [Integration guide](INTEGRATION.md) | Raw curl request, output handling, and troubleshooting |
| [GLM model variants](MODEL-VARIANTS.md) | Compare standard, Flash, Uncensored, and Abliterated model IDs |

## AI jailbreak terminology and GLM variants

The term *AI jailbreak* (or *LLM jailbreak*) describes a prompt-based attempt to change how a model responds. Abliteration describes a change to the model itself. The [HEX model terminology guide](https://github.com/hexapi-io/hex-model-catalog/blob/main/JAILBREAK-AND-MODEL-VARIANTS.md) explains both concepts, along with prompt injection and the Uncensored catalog label.

## Use GLM 5.3 Abliterated in OpenCode

Follow the [HEX setup guide for OpenCode Desktop](https://github.com/hexapi-io/hex-opencode-setup), then select GLM 5.3 Abliterated in the model picker. In your own API client, use the exact ID `glm-5.3-abliterated`. The [GLM section of the catalog](https://github.com/hexapi-io/hex-model-catalog/blob/main/MODEL-INDEX.md#glm) lists the separate IDs for Flash and Uncensored variants.

[Pricing](https://hexapi.io/pricing) · [API reference](https://hexapi.io/docs) · [Service status](https://hexapi.io/status) · [OpenCode Desktop](https://hexapi.io/setup/opencode)

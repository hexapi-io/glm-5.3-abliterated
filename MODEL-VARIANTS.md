# GLM 5.3 model variants on HEX

Select the model ID by the workflow you want to evaluate. GLM 5.3 and GLM 5.3 Flash each have a standard entry and separately named Uncensored and Abliterated entries.

| Base family | Standard | Uncensored | Abliterated |
| --- | --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `glm-5.3-uncensored` | `glm-5.3-abliterated` |
| GLM 5.3 Flash | `glm-5.3-flash` | `glm-5.3-flash-uncensored` | `glm-5.3-flash-abliterated` |

## GLM 5.3 Abliterated and AI jailbreak terminology

An AI jailbreak is an input-based attempt to change model behavior. **GLM 5.3 Abliterated** is the literal name of an API model variant. The HEX catalog lets you select that variant by ID. The [terminology guide](https://github.com/hexapi-io/hex-model-catalog/blob/main/JAILBREAK-AND-MODEL-VARIANTS.md) covers LLM jailbreaks, prompt injection, and variant labels.

## Test the differences on your own tasks

Use the same fictional bug report across variants. Check four properties: valid JSON, reproductions grounded in the report, faithful language, and completion without truncation. Record the ID and output limit with each run. When using the [GLM 5.3 Abliterated integration example](INTEGRATION.md), its `low` reasoning setting applies to the documented model ID.

[Live model list](https://hexapi.io/models) · [Current price](https://hexapi.io/pricing) · [Model evaluation checklist](https://github.com/hexapi-io/hex-model-catalog/blob/main/MODEL-EVALUATION.md)

---
name: "dpxx-gemini-image-skill v1.0.1"
version: 1.0.1
description: Generate or edit images with RootFlowAI Gemini image models. Use when the user asks to draw, generate, create, edit, 出图, 作图, 生成图, 改图, or P 图 and wants the DPXX Gemini image workflow.
changelog:
  - "1.0.1 (2026-05-08): 独立为 Gemini 专用 RootFlowAI skill。"
---

# dpxx-gemini-image-skill v1.0.1

This skill is Gemini-only. It uses RootFlowAI as the only active image provider.

## 0. Required Checks

1. Check the API key before calling scripts:
   ```bash
   env | grep -E "ROOTFLOWAI_GEMINI_API_KEY" || echo MISSING
   ```
2. If missing, ask the user for the Gemini RootFlowAI key and pass it as `--api-key "<ROOTFLOWAI_GEMINI_API_KEY>"`. Do not write keys to files and do not edit shell rc files.
3. Use `https://api.rootflowai.com/v1` unless the user explicitly gives another RootFlowAI base URL.
4. Scripts are standard-library Python:
   - `{SKILL_DIR}/scripts/generate_image.py`
   - `{SKILL_DIR}/scripts/edit_image.py`

## 1. Mandatory Flow

Collect the generation parameters before running the script:

1. Ask for model family: `Gemini 3.1 Flash` or `Gemini 3 Pro`.
2. Ask for resolution: `1K`, `2K`, or `4K`.
3. Ask for ratio or pixel size.
4. Ask for subject if the user did not provide one.
5. Pick a prompt template by reading `references/prompt-patterns.md`; if no template fits, use the six-slot prompt flow: Subject, Composition, Lighting, Style, Color, Constraints.
6. Show a concise execution summary and wait for user confirmation.

## 2. Model Mapping

| Resolution | Gemini 3.1 Flash | Gemini 3 Pro |
| --- | --- | --- |
| 1K | `gemini-3.1-flash-image-count` | `gemini-3-pro-image-count` |
| 2K | `gemini-3.1-flash-image-hd-count` | `gemini-3-pro-image-hd-count` |
| 4K | `gemini-3.1-flash-image-4k-count` | `gemini-3-pro-image-4k-count` |

Default: use `gemini-3.1-flash-image-hd-count` for final-looking work and `gemini-3.1-flash-image-count` for quick composition checks.

## 3. Size Rules

Gemini models support these ratios in this skill:

```text
1:1  3:2  2:3  4:3  3:4  5:4  4:5  16:9  9:16  2:1  1:2  21:9  9:21
```

Pixel sizes such as `1024x1024` are also accepted by the script and mapped to the closest supported ratio when validation needs it.

## 4. Quality

Do not ask for a `quality` setting for Gemini. The scripts accept `--quality` for CLI compatibility, but omit it from Gemini API requests.

## 5. Commands

Text to image:

```bash
python3 {SKILL_DIR}/scripts/generate_image.py \
  --api-key "<ROOTFLOWAI_GEMINI_API_KEY>" \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "<FINAL_PROMPT>" \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini
```

Image to image:

```bash
python3 {SKILL_DIR}/scripts/generate_image.py \
  --api-key "<ROOTFLOWAI_GEMINI_API_KEY>" \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "<FINAL_PROMPT>" \
  --image ./input.png \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini-ref
```

Edit:

```bash
python3 {SKILL_DIR}/scripts/edit_image.py \
  --api-key "<ROOTFLOWAI_GEMINI_API_KEY>" \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "<EDIT_INSTRUCTION>" \
  --image ./input.png \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini-edit
```

## 6. Output Rules

Return saved image paths and the effective model, resolution, ratio, and prompt source. Keep user-visible error text concise and do not expose API keys.

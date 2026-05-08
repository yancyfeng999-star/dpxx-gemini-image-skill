<div align="center">

# DPXX Gemini Image Skill

RootFlowAI-powered Gemini image generation workflow for DPXX.

[English](README.md) · [简体中文](README.zh.md) · [Release v1.0.1](https://github.com/yancyfeng999-star/dpxx-gemini-image-skill/releases/tag/v1.0.1)

![Version](https://img.shields.io/badge/version-v1.0.1-blue)
![Provider](https://img.shields.io/badge/provider-RootFlowAI-111827)
![Model](https://img.shields.io/badge/model-Gemini-10b981)
![Python](https://img.shields.io/badge/python-3.x-3776ab)

</div>

## Overview

`dpxx-gemini-image-skill` is a standalone DPXX image-generation skill for Gemini image models through RootFlowAI. It supports text-to-image, reference-image generation, and image editing.

This repository is independent from the GPT skill. A customer can install this Gemini skill by itself when the preferred workflow needs Gemini image-model prompt following.

## Highlights

- Single-provider Gemini workflow through RootFlowAI
- Shared DPXX prompt, request, download, and output conventions
- Text-to-image, reference-image generation, and edit workflows
- Version-controlled skill metadata, script metadata, and release tags
- Public documentation with private runtime configuration kept outside the repository

## Model Map

| Resolution | Gemini 3.1 Flash | Gemini 3 Pro |
| --- | --- | --- |
| 1K | `gemini-3.1-flash-image-count` | `gemini-3-pro-image-count` |
| 2K | `gemini-3.1-flash-image-hd-count` | `gemini-3-pro-image-hd-count` |
| 4K | `gemini-3.1-flash-image-4k-count` | `gemini-3-pro-image-4k-count` |

Recommended default: `gemini-3.1-flash-image-hd-count`. Use the Gemini 3 Pro series for more complex poster and professional visual work.

## Aspect Ratios

Supported:

```text
1:1  3:2  2:3  4:3  3:4  5:4  4:5  16:9  9:16  2:1  1:2  21:9  9:21
```

Gemini requests do not send the `quality` parameter.

## Quick Start

Configure RootFlowAI authentication through your runtime environment before running. Keep private credentials outside the repository.

```bash
python3 scripts/generate_image.py \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "A clean product hero image on a plain background." \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini
```

## Workflow

1. Pick the Gemini model that matches the target resolution and prompt complexity.
2. Write the prompt using the DPXX prompt rules in `SKILL.md`.
3. Run `scripts/generate_image.py` with `--profile gemini`.
4. Review the generated image and rerun with a refined prompt when needed.
5. Keep version files aligned before publishing workflow changes.

## Versioning

Current version: `v1.0.1`

- `SKILL.md` frontmatter is the source of truth.
- `references/VERSION.md` and `scripts/VERSION.md` must match `SKILL.md`.
- GitHub release tags use the same semantic version, for example `v1.0.1`.
- Bump the version when scripts, model mapping, or user-facing workflow behavior changes.

## Repository Layout

```text
SKILL.md                 Skill instructions
USER_GUIDE.md            User-facing operation guide
WORKFLOW.md              End-to-end generation workflow
scripts/                 RootFlowAI request scripts
references/              Prompt templates and case library
tests/                   Unit tests
```

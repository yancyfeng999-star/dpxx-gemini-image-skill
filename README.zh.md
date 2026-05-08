<div align="center">

# DPXX Gemini 生图 Skill

面向 DPXX 工作流的 RootFlowAI Gemini 生图项目。

[简体中文](README.zh.md) · [English](README.md) · [版本 v1.0.1](https://github.com/yancyfeng999-star/dpxx-gemini-image-skill/releases/tag/v1.0.1)

![版本](https://img.shields.io/badge/version-v1.0.1-blue)
![渠道](https://img.shields.io/badge/provider-RootFlowAI-111827)
![模型](https://img.shields.io/badge/model-Gemini-10b981)
![Python](https://img.shields.io/badge/python-3.x-3776ab)

</div>

## 项目简介

`dpxx-gemini-image-skill` 是一个独立的 DPXX 生图技能项目，专注于通过 RootFlowAI 调用 Gemini 图像模型完成文生图、参考图生图和图片编辑。

这个仓库不依赖 GPT 版本。客户如果需要 Gemini 图像模型的提示词跟随能力，可以单独安装和使用这个 skill。

## 核心特点

- 单独保留 Gemini 生图流程，渠道为 RootFlowAI
- 复用 DPXX 的 prompt、请求、下载和输出规范
- 支持文生图、参考图生图和图片编辑
- 技能元数据、脚本元数据和 GitHub release 统一控版
- 公开文档不包含任何私密运行配置

## 模型映射

| 分辨率 | Gemini 3.1 Flash | Gemini 3 Pro |
| --- | --- | --- |
| 1K | `gemini-3.1-flash-image-count` | `gemini-3-pro-image-count` |
| 2K | `gemini-3.1-flash-image-hd-count` | `gemini-3-pro-image-hd-count` |
| 4K | `gemini-3.1-flash-image-4k-count` | `gemini-3-pro-image-4k-count` |

默认建议使用 `gemini-3.1-flash-image-hd-count`。如果需要更复杂的海报或专业视觉资产，可以选择 Gemini 3 Pro 系列。

## 比例规则

支持：

```text
1:1  3:2  2:3  4:3  3:4  5:4  4:5  16:9  9:16  2:1  1:2  21:9  9:21
```

Gemini 请求不会发送 `quality` 参数。

## 快速开始

运行前请先在你的部署环境中完成 RootFlowAI 鉴权配置。所有私密凭证都应保留在运行环境里，不要提交到仓库。

```bash
python3 scripts/generate_image.py \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "A clean product hero image on a plain background." \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini
```

## 使用流程

1. 根据目标分辨率和 prompt 复杂度选择 Gemini 模型。
2. 按 `SKILL.md` 中的 DPXX prompt 规则整理提示词。
3. 使用 `scripts/generate_image.py` 并指定 `--profile gemini`。
4. 检查生成结果，根据画面继续优化 prompt。
5. 发布流程变更前，保持所有版本文件一致。

## 版本控制

当前版本：`v1.0.1`

- `SKILL.md` frontmatter 里的 `version` 是版本源头。
- `references/VERSION.md` 和 `scripts/VERSION.md` 必须与 `SKILL.md` 保持一致。
- GitHub release tag 使用同名语义版本号，例如 `v1.0.1`。
- 修改脚本、模型映射或用户可感知流程时必须提升版本号。

## 项目结构

```text
SKILL.md                 技能主说明
USER_GUIDE.md            用户操作指南
WORKFLOW.md              端到端生图流程
scripts/                 RootFlowAI 调用脚本
references/              prompt 模板和案例库
tests/                   单元测试
```

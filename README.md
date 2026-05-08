# dpxx-gemini-image-skill

## 中文说明

`dpxx-gemini-image-skill` 是一个 DPXX 生图技能项目，专注于通过 RootFlowAI 调用 Gemini 图像模型完成文生图、参考图生图和图片编辑。

这个仓库是独立项目，可以单独安装、分发和使用，不依赖 GPT 版本的 skill。

### 适合场景

- 复杂海报、长 prompt、多元素画面
- 文字要求更高的视觉资产
- 商品图、社媒图、品牌视觉和创意海报
- 需要 Gemini 图像模型提示词跟随能力的 DPXX 工作流

### 模型映射

| 分辨率 | Gemini 3.1 Flash | Gemini 3 Pro |
| --- | --- | --- |
| 1K | `gemini-3.1-flash-image-count` | `gemini-3-pro-image-count` |
| 2K | `gemini-3.1-flash-image-hd-count` | `gemini-3-pro-image-hd-count` |
| 4K | `gemini-3.1-flash-image-4k-count` | `gemini-3-pro-image-4k-count` |

默认建议使用 `gemini-3.1-flash-image-hd-count`。如果需要更复杂的海报或专业视觉资产，可以选择 Gemini 3 Pro 系列。

### 比例规则

支持：

```text
1:1  3:2  2:3  4:3  3:4  5:4  4:5  16:9  9:16  2:1  1:2  21:9  9:21
```

Gemini 请求不会发送 `quality` 参数。

### 基本命令

运行前请先按你的部署环境完成 RootFlowAI 鉴权配置。不要把任何私密凭证写入仓库。

```bash
python3 scripts/generate_image.py \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "A clean product hero image on a plain background." \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini
```

### 项目结构

```text
SKILL.md                 技能主说明
scripts/                 RootFlowAI 调用脚本
references/              prompt 模板和案例库
tests/                   单元测试
```

---

## English

`dpxx-gemini-image-skill` is a standalone DPXX image-generation skill for Gemini image models through RootFlowAI. It supports text-to-image, reference-image generation, and image editing.

This repository is self-contained and can be installed, distributed, and used independently from the GPT skill.

### Use Cases

- Complex posters, long prompts, and multi-element compositions
- Visual assets with stronger text-following requirements
- Product images, social media images, brand visuals, and creative posters
- DPXX workflows that need Gemini image-model prompt following

### Model Mapping

| Resolution | Gemini 3.1 Flash | Gemini 3 Pro |
| --- | --- | --- |
| 1K | `gemini-3.1-flash-image-count` | `gemini-3-pro-image-count` |
| 2K | `gemini-3.1-flash-image-hd-count` | `gemini-3-pro-image-hd-count` |
| 4K | `gemini-3.1-flash-image-4k-count` | `gemini-3-pro-image-4k-count` |

Recommended default: `gemini-3.1-flash-image-hd-count`. Use the Gemini 3 Pro series for more complex poster and professional visual work.

### Aspect Ratios

Supported:

```text
1:1  3:2  2:3  4:3  3:4  5:4  4:5  16:9  9:16  2:1  1:2  21:9  9:21
```

Gemini requests do not send the `quality` parameter.

### Basic Command

Configure RootFlowAI authentication through your runtime environment before running. Do not commit private credentials to the repository.

```bash
python3 scripts/generate_image.py \
  --profile gemini \
  --model gemini-3.1-flash-image-hd-count \
  --prompt "A clean product hero image on a plain background." \
  --size 1:1 \
  --output-dir ./out \
  --prefix gemini
```

### Repository Layout

```text
SKILL.md                 Skill instructions
scripts/                 RootFlowAI request scripts
references/              Prompt templates and case library
tests/                   Unit tests
```

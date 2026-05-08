# RootFlowAI Gemini API Notes

Base URL:

```text
https://api.rootflowai.com/v1
```

Authentication:

```text
Authorization: Bearer <ROOTFLOWAI_GEMINI_API_KEY>
```

Supported Gemini image models:

- `gemini-3.1-flash-image-count`
- `gemini-3.1-flash-image-hd-count`
- `gemini-3.1-flash-image-4k-count`
- `gemini-3-pro-image-count`
- `gemini-3-pro-image-hd-count`
- `gemini-3-pro-image-4k-count`

Generation endpoint:

```text
POST /images/generations
```

Edit endpoint:

```text
POST /images/edits
```

Do not include `quality` for Gemini requests.

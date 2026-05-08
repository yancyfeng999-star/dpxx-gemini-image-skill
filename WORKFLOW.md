# Gemini Image Workflow

1. Confirm `ROOTFLOWAI_GEMINI_API_KEY` or receive the key from the user for one-time `--api-key` use.
2. Choose model family:
   - `Gemini 3.1 Flash`
   - `Gemini 3 Pro`
3. Choose resolution and map it to the selected family.
4. Choose ratio from the supported ratio list.
5. Build the prompt from `references/prompt-patterns.md` or the six-slot fallback.
6. Confirm the final command summary with the user.
7. Run `generate_image.py` or `edit_image.py`.
8. Report the saved path, model, ratio, and any skipped response items.

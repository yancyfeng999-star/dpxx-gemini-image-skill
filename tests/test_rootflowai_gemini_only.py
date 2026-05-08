from __future__ import annotations

import os
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import generate_image
import image_api_common


class RootFlowAIGeminiOnlyTests(unittest.TestCase):
    def test_only_gemini_profile_is_exposed(self) -> None:
        self.assertEqual(image_api_common.SUPPORTED_PROFILES, (image_api_common.PROFILE_GEMINI,))
        self.assertFalse(hasattr(image_api_common, "PROFILE_GPT"))

    def test_gemini_model_matrix_has_1k_2k_4k_for_31_flash_and_3_pro(self) -> None:
        self.assertEqual(
            image_api_common.GEMINI_31_FLASH_MODELS_BY_RESOLUTION,
            {
                "1K": image_api_common.GEMINI_31_FLASH_MODEL,
                "2K": image_api_common.GEMINI_31_FLASH_HD_MODEL,
                "4K": image_api_common.GEMINI_31_FLASH_4K_MODEL,
            },
        )
        self.assertEqual(
            image_api_common.GEMINI_3_PRO_MODELS_BY_RESOLUTION,
            {
                "1K": image_api_common.GEMINI_3_PRO_MODEL,
                "2K": image_api_common.GEMINI_3_PRO_HD_MODEL,
                "4K": image_api_common.GEMINI_3_PRO_4K_MODEL,
            },
        )

    def test_gpt_model_names_are_rejected(self) -> None:
        with self.assertRaises(SystemExit):
            image_api_common.resolve_model(None, "gpt-image-2-count")

    def test_get_api_key_uses_only_gemini_env_var(self) -> None:
        with mock.patch.dict(os.environ, {"ROOTFLOWAI_GEMINI_API_KEY": "gemini-key"}, clear=True):
            key, profile, source = image_api_common.get_api_key(None)

        self.assertEqual((key, profile, source), ("gemini-key", image_api_common.PROFILE_GEMINI, "ROOTFLOWAI_GEMINI_API_KEY"))

    def test_generate_image_omits_quality_for_gemini_models(self) -> None:
        captured_payloads: list[dict] = []

        def fake_post_json_request(**kwargs):
            captured_payloads.append(kwargs["payload"])
            return {"data": [{"b64_json": "iVBORw0KGgo="}]}

        with (
            mock.patch.dict(os.environ, {"ROOTFLOWAI_GEMINI_API_KEY": "gemini-key"}, clear=True),
            mock.patch.object(generate_image, "post_json_request", side_effect=fake_post_json_request),
            mock.patch.object(generate_image, "save_response_images", return_value=(["/tmp/img.png"], [], None)),
            mock.patch.object(
                sys,
                "argv",
                [
                    "generate_image.py",
                    "--model",
                    image_api_common.GEMINI_31_FLASH_MODEL,
                    "--prompt",
                    "A clean product hero image.",
                    "--size",
                    "16:9",
                    "--quality",
                    "high",
                ],
            ),
        ):
            with redirect_stdout(StringIO()):
                self.assertEqual(generate_image.main(), 0)

        self.assertEqual(len(captured_payloads), 1)
        self.assertNotIn("quality", captured_payloads[0])


if __name__ == "__main__":
    unittest.main()

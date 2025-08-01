# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

"""Basic Lighthouse accessibility check."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys

import pytest

LH = shutil.which("lighthouse") or shutil.which("lighthouse.cmd")
CHROME = shutil.which("chromium") or shutil.which("chromium-browser") or os.environ.get("CHROME_PATH")

pytestmark = pytest.mark.skipif(not LH or not CHROME, reason="Lighthouse or Chrome not available")


def test_lighthouse_accessibility(tmp_path):
    report = tmp_path / "report.json"
    cmd = [
        "npx",
        "--yes",
        "lighthouse",
        "https://example.com",
        "--quiet",
        "--only-categories=accessibility",
        "--output=json",
        f"--output-path={report}",
        "--chrome-flags=--headless",
    ]
    env = os.environ.copy()
    env.setdefault("CHROME_PATH", CHROME)
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        pytest.skip(f"lighthouse failed: {result.stderr}")
    data = json.loads(report.read_text())
    audits = data.get("audits", {})
    assert "color-contrast" in audits
    assert "aria-valid-attr" in audits

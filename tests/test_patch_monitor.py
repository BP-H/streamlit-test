# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import textwrap
from pathlib import Path

from governance.patch_monitor import check_patch_compliance
from disclaimers import (
    STRICTLY_SOCIAL_MEDIA,
    INTELLECTUAL_PROPERTY_ARTISTIC_INSPIRATION,
    LEGAL_ETHICAL_SAFEGUARDS,
)


def test_patch_without_disclaimers_flagged(tmp_path):
    patch = textwrap.dedent(
        """\
        diff --git a/foo.py b/foo.py
        +++ b/foo.py
        +print('hello')
        """
    )
    issues = check_patch_compliance(patch)
    assert issues == ["New additions missing required disclaimers"]


def test_patch_ok_when_file_contains_disclaimers(tmp_path):
    target = tmp_path / "bar.py"
    target.write_text(
        f"# {STRICTLY_SOCIAL_MEDIA}\n"
        f"# {INTELLECTUAL_PROPERTY_ARTISTIC_INSPIRATION}\n"
        f"# {LEGAL_ETHICAL_SAFEGUARDS}\n"
        "print('original')\n"
    )
    abs_path = target.as_posix()
    patch = textwrap.dedent(
        f"""\
        diff --git a/{abs_path} b/{abs_path}
        +++ b/{abs_path}
        +print('change')
        diff --git a/dev/null b/dev/null
        """
    )
    issues = check_patch_compliance(patch)
    assert issues == []


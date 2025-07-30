import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "page_registry",
    Path(__file__).resolve().parents[1] / "utils" / "page_registry.py",
)
page_registry = importlib.util.module_from_spec(spec)
sys.modules["page_registry"] = page_registry
spec.loader.exec_module(page_registry)
ensure_pages = page_registry.ensure_pages


def test_ensure_pages_creates_stubs(tmp_path):
    pages = {"One": "one", "Two": "two"}
    pages_dir = tmp_path / "pages"
    ensure_pages(pages, pages_dir)
    for slug in pages.values():
        file_path = pages_dir / f"{slug}.py"
        assert file_path.exists()
        content = file_path.read_text()
        assert "Placeholder page" in content


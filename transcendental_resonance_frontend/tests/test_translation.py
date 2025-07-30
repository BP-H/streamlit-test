from utils.translation import translate_text


def test_translate_text_returns_input_on_error(monkeypatch):
    def fail_translate(*args, **kwargs):
        raise RuntimeError

    monkeypatch.setattr('utils.translation.translator.translate', fail_translate)
    assert translate_text("hello", "es") == "hello"


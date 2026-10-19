
from main import explain_error, review_code
from snippet_manager import save_snippet, list_snippets, SNIPPETS_FILE
def test_empty_error():
    result = explain_error("", "Python")
    assert result == "Please provide an error message."

def test_empty_code():
    result = review_code("")
    assert result == "Please provide a code snippet."

def test_review_code():
    result = review_code('print("Hello World")')
    assert 'print("Hello World")' in result

print("Running DevMate AI tests...")

test_empty_error()
test_empty_code()
test_review_code()

def test_name_error():
    result = explain_error(
        "NameError: name 'username' is not defined",
        "Python"
    )
    assert "undefined" in result.lower()


def test_syntax_error():
    result = explain_error(
        "SyntaxError: invalid syntax",
        "Python"
    )
    assert "syntax" in result.lower()


def test_type_error():
    result = explain_error(
        "TypeError: unsupported operand type(s)",
        "Python"
    )
    assert "data types" in result.lower()
    
def test_whitespace_error():
    result = explain_error("   ", "Python")
    assert result == "Please provide an error message."


def test_unknown_error():
    result = explain_error(
        "RandomError: something went wrong",
        "Python"
    )
    assert "relevant line" in result

def test_list_snippets_handles_invalid_json():
    
    original_content = None

    try:
        if SNIPPETS_FILE.exists():
            original_content = SNIPPETS_FILE.read_text(encoding="utf-8")

        SNIPPETS_FILE.write_text("{invalid json", encoding="utf-8")

        result = list_snippets()

        assert result == [], "Expected an empty list for invalid JSON"

    finally:
        if original_content is not None:
            SNIPPETS_FILE.write_text(original_content, encoding="utf-8")
        elif SNIPPETS_FILE.exists():
            SNIPPETS_FILE.unlink()

def test_save_snippet_rejects_empty_input():
    assert save_snippet("", 'print("Hello")') == "empty"
    assert save_snippet("Test title", "") == "empty"
            
print("Running remaining DevMate AI tests...")

test_name_error()
test_syntax_error()
test_type_error()
test_whitespace_error()
test_unknown_error()
test_list_snippets_handles_invalid_json()

print("All tests passed!")







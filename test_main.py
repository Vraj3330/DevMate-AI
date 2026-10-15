
from main import explain_error, review_code

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

print("All tests passed!")

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

def test_whitespace_error():
    result = explain_error("   ", "Python")
    assert result == "Please provide an error message."


def test_unknown_error():
    result = explain_error(
        "RandomError: something went wrong",
        "Python"
    )
    assert "relevant line" in result



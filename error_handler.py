
def explain_error(error_message, language):
    if not error_message.strip():
        return "Please provide an error message."

    error = error_message.lower()

    if "nameerror" in error:
        advice = (
            "A name may be undefined. "
            "Check your variable and function names."
        )

    elif "syntaxerror" in error:
        advice = (
            "Check your Python syntax, brackets, "
            "quotation marks, and colons."
        )

    elif "typeerror" in error:
        advice = (
            "Check whether you are using "
            "compatible data types."
        )

    else:
        advice = (
            "Check the error message, the relevant "
            "line, and the values used there."
        )

    return (
        f"Language: {language}\n"
        f"Error: {error_message}\n"
        f"Suggestion: {advice}"
    )

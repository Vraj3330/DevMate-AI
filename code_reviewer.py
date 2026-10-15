
def review_code(code):
    if not code.strip():
        return "Please provide a code snippet."

    suggestions = []

    if "print(" not in code:
        suggestions.append(
            "No print() statement found. "
            "Check whether you need to display output."
        )

    if "def " in code and "return" not in code:
        suggestions.append(
            "Your code defines a function but has no "
            "return statement. Check whether a value is needed."
        )

    if not suggestions:
        suggestions.append(
            "Basic checks passed. Review the logic, "
            "inputs, outputs, and possible edge cases."
        )

    return (
        f"Your submitted code:\n{code}\n\n"
        "Suggestions:\n- " + "\n- ".join(suggestions)
    )

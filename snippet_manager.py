

import json
from pathlib import Path

SNIPPETS_FILE = Path("snippets.json")


def save_snippet(title, code):
    title = title.strip()
    code = code.strip()

    if not title or not code:
        return "empty"

    try:
        if SNIPPETS_FILE.exists():
            with open(SNIPPETS_FILE, "r", encoding="utf-8") as file:
                snippets = json.load(file)
        else:
            snippets = []

        if not isinstance(snippets, list):
            return "invalid"

        # Prevent duplicate titles
        for snippet in snippets:
            if snippet["title"].casefold() == title.casefold():
                return "duplicate"

        snippets.append({
            "title": title,
            "code": code
        })

        with open(SNIPPETS_FILE, "w", encoding="utf-8") as file:
            json.dump(snippets, file, indent=4)

        return "saved"

    except (json.JSONDecodeError, KeyError, AttributeError):
        return "invalid"

    except OSError:
        return "file_error"


def list_snippets():
    if not SNIPPETS_FILE.exists():
        return []

    try:
        with open(SNIPPETS_FILE, "r", encoding="utf-8") as file:
            snippets = json.load(file)

        if not isinstance(snippets, list):
            print("Error: The snippets file has an invalid format.")
            return []

        return snippets

    except json.JSONDecodeError:
        print("Error: Your snippets.json file contains invalid JSON.")
        return []

    except OSError:
        print("Error: Could not read the snippets file.")
        return []

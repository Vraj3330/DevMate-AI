
import json
from pathlib import Path

SNIPPETS_FILE = Path("snippets.json")



def save_snippet(title, code):
    title = title.strip()
    code = code.strip()

    if not title or not code:
        return False

    if SNIPPETS_FILE.exists():
        with open(SNIPPETS_FILE, "r", encoding="utf-8") as file:
            snippets = json.load(file)
    else:
        snippets = []

    # Prevent duplicate titles
    for snippet in snippets:
        if snippet["title"].casefold() == title.casefold():
            return False

    snippets.append({
        "title": title,
        "code": code
    })

    with open(SNIPPETS_FILE, "w", encoding="utf-8") as file:
        json.dump(snippets, file, indent=4)

    return True


    snippets.append({
        "title": title,
        "code": code
    })

    with open(SNIPPETS_FILE, "w", encoding="utf-8") as file:
        json.dump(snippets, file, indent=4)

    return True

def list_snippets():
    if not SNIPPETS_FILE.exists():
        return []

    with open(SNIPPETS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

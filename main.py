from error_handler import explain_error
from code_reviewer import review_code
from snippet_manager import save_snippet, list_snippets


def handle_save_snippet():
    title = input("Enter snippet title: ")
    code = input("Enter your code: ")

    if save_snippet(title, code):
        print("Snippet saved successfully!")
    else:
        print("Title and code cannot be empty.")


def handle_list_snippets():
    snippets = list_snippets()

    if not snippets:
        print("No saved snippets found.")
        return

    for number, snippet in enumerate(snippets, start=1):
        print(f"\n{number}. {snippet['title']}")
        print(snippet["code"])




def main():
    while True:
        print("\n=== DevMate AI ===")
        print("1. Explain a Python error")
        print("2. Review a code snippet")
        print("3. Save a code snippet")
        print("4. List saved snippets")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            error = input("Paste your Python error: ")
            language = input("Enter programming language: ")
            print(explain_error(error, language))

        elif choice == "2":
            code = input("Paste your code snippet: ")
            print(review_code(code))

        elif choice == "3":
            handle_save_snippet()

        elif choice == "4":
            handle_list_snippets()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()


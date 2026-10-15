from error_handler import explain_error
from code_reviewer import review_code


def main():
    while True:
        print("\n=== DevMate AI ===")
        print("1. Explain a Python error")
        print("2. Review a code snippet")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            error = input("Paste your Python error: ")
            language = input("Enter programming language: ")
            print(explain_error(error, language))

        elif choice == "2":
            code = input("Paste your code snippet: ")
            print(review_code(code))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


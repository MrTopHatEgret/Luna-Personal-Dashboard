import os
import pathlib

CLASS_TYPES = ["Online", "Offline", "Hybrid (Can work online or offline)"]
FUNCTION_TEXT = '''
class CLASS_NAME:
    """CLASS_DESCRIPTION"""

    class_type = "CLASS_TYPE"

    def __class__(self, *args, **kwargs):
        pass
        '''


def user_class_type_input() -> str:
    print("Choose Function Type:")
    for class_type_index, class_type in enumerate(CLASS_TYPES):
        print(f"[{class_type_index}] {class_type}")
    user_class_type = input("-> ")

    if int(user_class_type) not in range(0, len(CLASS_TYPES) - 1):
        print("\nInvalid Function Type.\nRe-enter Function Type to Continue.")
        return user_class_type_input()

    return user_class_type


def class_name_input() -> str:
    class_name = input("What is the Function Name:\n-> ")
    if "_" in class_name:
        print("Class name cannot have underscore.")
        print("Re-enter Function Name to Continue.")
        return class_name_input()
    elif " " in class_name:
        print("Class name cannot have `space`.")
        print("Re-enter Function Name to Continue.")
        return class_name_input()
    return class_name


def main():
    class_type = CLASS_TYPES[int(user_class_type_input())]
    class_name = class_name_input()
    class_description = input("What is the Function Description\n-> ").title()

    class_template = FUNCTION_TEXT

    # Replace each placeholder in the `class_template` with it value
    class_template = class_template.replace("CLASS_NAME", class_name)
    class_template = class_template.replace("CLASS_TYPE", class_type)
    class_template = class_template.replace("CLASS_DESCRIPTION", class_description)

    # Resolves path of project root directory
    function_file_path = f"{pathlib.Path(__file__).parent.parent.resolve()}\\{class_type}\\{class_name}.py"
    # Create a new file at `function_file_path`
    with open(function_file_path, "w") as file:
        file.write(class_template)

    # Formats the code file using black to make it PIP complaint
    print("Formatting File.")
    os.system(f'black --quiet "{function_file_path}"')
    print("Done.")


if __name__ == "__main__":
    main()

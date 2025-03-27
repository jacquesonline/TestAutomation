import os


def search_requirements(root_folder):
    print(f"Searching for requirements.txt files in {root_folder}")
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if 'requirements.txt' in filenames:
            requirements_path = os.path.join(dirpath, 'requirements.txt')
            print(f"Found: {requirements_path}")


if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    search_requirements(root_folder)

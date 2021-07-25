import os
import json


def get_content(file_paths: str) -> dict:
    content = dict()
    for path in file_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content[path] = [line.split()[0].replace("\n", "").strip().lower() for line in f if not line.startswith("#")]
        else:
            print("[Error] Invalid file path ->", path)

    return content


def get_duplicates(content: dict) -> list:
    all_lines = []
    for lines in content.values():
        all_lines += lines

    duplicates = dict()
    for path, lines in content.items():
        duplicates[path] = dict()
        for index, line in enumerate(lines):
            count = all_lines.count(line)

            if count > 1 and line not in duplicates.values():
                duplicates[path][line] = lines.count(line)

    return duplicates


if __name__ == '__main__':
    while True:
        file_paths = input("Enter paths to files separated by space >>> ").split()
        content = get_content(file_paths)

        print(json.dumps(get_duplicates(content), indent=4))

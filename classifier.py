import os
import json

THRESHOLD = 10


def get_json_file() -> str:
    file_path = input("Enter path to a parser result json file >>> ")

    if os.path.exists(file_path):
        return file_path
    else:
        print("[Error] Invalid file path")


def get_monomers(data) -> list:
    monomers = list()
    for protein_id, protein in data.items():
        for name, value in protein.items():
            if not isinstance(name, str):
                continue

            if name.upper() == "I" and value['percentage'] < THRESHOLD:
                monomers.append(protein_id)
        
    return monomers


if __name__ == '__main__':
    while True:
        file_path = get_json_file()

        if file_path is None:
            continue
        
        with open(file_path) as json_file:
            data = json.load(json_file)
            monomers = get_monomers(data)
    
            print(json.dumps(monomers, indent=4))
            print("-" * 50)
            print("Found -", len(monomers))
            print("-" * 50)

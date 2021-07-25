import json
import os

import pandas as pd

HEADER_INDEX = 0
SEPARATOR = "\t"

def save_result(path, result):
    with open(path + "/parser_result.json", "w+") as csv_file:
        print(f"Saving result at {path}...")
        json.dump(result, csv_file, indent=4)

def should_be_saved():
    try:
        while True:
            answer = input("Do you want to save the result? [y/n] ").lower()
            valid_answers = ["y", "n"]
            if answer in valid_answers:
                return answer == "y"
            else:
                print("[Error] Not a valid answer")
                continue
    except KeyboardInterrupt:
        quit()

def get_path(reason):
    try:
        while True:
            file_path = input(f"{reason} >>> ")
            if os.path.exists(file_path):
                return file_path
            else:
                print("[Error] Unknown file path")
    except KeyboardInterrupt:
        quit()

def add_percentage(proteins):
    for protein_id in proteins:
        protein = proteins[protein_id]
        for value, data in protein.items():
            if isinstance(data, dict):
                total_count = protein['total_count']
                percentage = data['count'] / (total_count / 100)
                protein[value]["percentage"] = round(percentage, 2)

    return proteins

def search(file_path, save=False) -> None:
    print("Searching for proteins and counting their values...")
    print("-" * 50)

    proteins = {}
    csv_file = pd.read_csv(
        file_path,
        header=HEADER_INDEX,
        names=["Protein", "value"],
        sep=SEPARATOR,
    )
    for index, row in csv_file.iterrows():
        protein_id = row.name[0]
        protein_value = row['value']

        if protein_id not in proteins:
            proteins[protein_id] = dict()

        if "total_count" not in proteins[protein_id]:
            proteins[protein_id]['total_count'] = 0

        if protein_value not in proteins[protein_id]:
            proteins[protein_id][protein_value] = dict()
            proteins[protein_id][protein_value]['count'] = 1
        else:
            proteins[protein_id][protein_value]['count'] += 1
        
        proteins[protein_id]['total_count'] += 1

    return add_percentage(proteins)


def main():
    while True:
        file_path = get_path("Enter path to json result file or csv")

        if file_path.endswith(".csv"):
            result = search(file_path)
            if result is not None:
                print(json.dumps(result, indent=4))
                print("-" * 50)
                print(f"Found {len(result)} proteins in this file")
                print("-" * 50)
    
                if should_be_saved():
                    save_path = get_path("Enter save location")
                    save_result(save_path, result)
            else:
                print("No results")
        else:
            print("[Error] Uknown file type")


if __name__ == '__main__':
    main()

import os
import json


def get_path() -> str:
    while True:
        file_path = input("Enter path to the json file >>> ")

        if os.path.exists(file_path) and file_path.endswith(".json"):
            return file_path
        else:
            print("[Error] Invalid file path or file type")


def print_statistics(data):
    percentages = []
    for protein_id, protein in data.items():
        if "I" in protein.keys():
            percentages.append(protein['I']['percentage'])
        else:
            percentages.append(0)
    
    print("Average ->", round(sum(percentages) / len(percentages), 2))
    print("Max ->", max(percentages))
    print("Min ->", min(percentages))
    print("Proteins Count ->", len(percentages))
        


def main() -> None:
    file_path = get_path()
    
    with open(file_path) as json_file:
        try:
            data = json.load(json_file)
        except json.error.JSONDecodeError:
            print("[Error] Couldn't load the json file")
            quit()
        
        print_statistics(data)

if __name__ == '__main__':
    main()
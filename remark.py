import re
import os
import json


REMARK_350_AUTHOR = "REMARK 350 AUTHOR DETERMINED BIOLOGICAL UNIT: MONOMERIC"
REMARK_350_SOFTWARE = "REMARK 350 SOFTWARE DETERMINED QUATERNARY STRUCTURE: MONOMERIC"

proteins = {}

def get_path() -> str:
    while True:
        path = input("Enter path to pdb file or directory >>> ")
    
        if not os.path.exists(path):
            print("[Error] Invalid path")
            continue
            
        return path

def is_monomer(file) -> bool:
    content = file.read()
    if REMARK_350_AUTHOR in content or REMARK_350_SOFTWARE in content:
        return True
    
    return False

def process_file(file) -> None:
    file_name = os.path.basename(file.name)[3:][:4].upper()
    
    proteins[file_name] = is_monomer(file)


    

if __name__ == '__main__':
    while True:
        path = get_path()

        print("Counting monomers...")
        print("-" * 50)
    
        if os.path.isdir(path):
            for file_name in os.listdir(path):
                file_path = path + "/" + file_name
                with open(file_path) as file:
                    process_file(file)
        elif path.endswith(".ent") or path.endswith(".pdb"):
            with open(path) as file:
                process_file(file)
        
        print(json.dumps(proteins, indent=4))
        print("-" * 50)
        print(f"Monomers: {list(proteins.values()).count(True)}/{len(proteins)}")
        print("-" * 50)

        proteins.clear()

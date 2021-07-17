from Bio import PDB

import os

pdb_list = PDB.PDBList()
run = True
while run:
    source_file = os.path.abspath(input("Enter source file name >>> "))
    if not os.path.exists(source_file):
        print("[Error] Entered file doesn't exists!")
        continue

    install_dir = input("Enter instalation directory >>> ")
    if not os.path.exists(install_dir):
        print("[Error] Entered file doesn't exists!")
        continue

    with open(source_file, "r") as f:
        for line in f:
            protein = line[:4].replace("\n", "")
            pdb_list.retrieve_pdb_file(protein, file_format = 'pdb', pdir=install_dir)

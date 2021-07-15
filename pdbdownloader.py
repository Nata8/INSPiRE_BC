from Bio import PDB

INSTALL_DIR = "pdb_files"

pdb_list = PDB.PDBList()
run = True
while run:
    file = input("Enter file name >>> ")
    with open(file, "r") as f:
        for line in f:
            pdb_list.retrieve_pdb_file(line.replace("\n", ""), file_format = 'pdb', pdir=INSTALL_DIR)

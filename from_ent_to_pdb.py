import os

path = "pdb_files_BIO"
ent_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in ent_files:
    new_file = file.replace("pdb", "").replace("ent", "pdb")
    os.rename(path+"/"+file, path+"/"+new_file)

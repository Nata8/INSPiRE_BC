
DATASETS_DIR = "datasets/"
DC_FILES = ["DCBio.txt", "DCxtal.txt"]
MANY_FILES = ["ManyBio.txt", "ManyXtal.txt"]


if __name__ == "__main__":
    for dc_file in DC_FILES:
        with open(DATASETS_DIR + dc_file) as dc:
            for many_file in MANY_FILES:
                with open(DATASETS_DIR + many_file) as many:
                    dc = [protein.split()[0] for protein in dc if not protein.startswith("#")]
                    many = [protein.split()[0] for protein in many if not protein.startswith("#")]
                    same = set(dc).intersection(many)
    
    for line in same:
        print(line)


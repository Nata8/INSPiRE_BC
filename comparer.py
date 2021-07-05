import os

DATASETS_DIR = "datasets/"
DC_FILES = ["DCBio.txt", "DCxtal.txt"]
MANY_FILES = ["ManyBio.txt", "ManyXtal.txt"]


def get_duplicates(filename):
    duplicates = []
    with open(DATASETS_DIR + filename) as f:
        lines = [line.split()[0].replace("\n", "").strip() for line in f if not line.startswith("#")]
        for index, line in enumerate(lines):
            if not line.startswith("#"):
                count = lines.count(line)
                #print(count)
                t = (count, line, filename)
                if count > 1 and t not in duplicates:
                    duplicates.append(t)
                    lines[index] = "\n"

        if duplicates:
            with open(DATASETS_DIR + filename, "w") as fw:
                filtred_lines = filter(lambda value: value != "\n", lines)
                fw.write("\n".join(filtred_lines))
    
    duplicates.sort()

    return duplicates


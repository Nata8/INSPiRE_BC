import requests
import os



def get_assembly_id():
    return input("Enter assembly id >>> ")


def get_ids():
    ids_string = input("Enter destination directory to save assemblies >>> ")

    return [protein_id.lower() for protein_id in ids_string.split()]


def get_download_dir():
    while True:
        path = input("Enter download dir path >>> ")

        if os.path.exists(path):
            return path
        
        print("[Error] Invalid path")


def download(pdb_id, dir, url):
    path = dir + "/" + pdb_id + ".cif"
    r = requests.get(url, allow_redirects=True)

    if r.status_code != 200:
        print(f"[Error] Couldn't download {pdb_id}")
        return

    with open(path, 'wb') as f:
        f.write(r.content)
    
    print(f"Successfully downloaded {pdb_id}")


def main():
    id_list = get_ids()
    dir = get_download_dir()
    assembly_id = get_assembly_id()
    
    for pdb_id in id_list:
        url = f'http://www.eppic-web.org/ewui/ewui/fileDownload?type=assembly&id={pdb_id}&assemblyId={assembly_id}&coordsFormat=cif'
        download(pdb_id, dir, url)


if __name__ == '__main__':
    main()


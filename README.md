# INSPiRE_BC

Repository created for the purpose of storing/viewing the scripts and results for bachelor thesis **`"Identification of crystal packing contacts using a method for detection of protein-protein interaction sites"`**. 
<br />
**REQUIREMENTS:** <br />
[INSPiRE](https://github.com/Jelinek-J/INSPiRE) <br />
[Python version 3.7.9](https://www.python.org/) <br />
[Biopython](https://biopython.org/) <br />
[EPPIC](https://www.eppic-web.org/ewui/) <br />
[Pandas](https://pandas.pydata.org/)
<br />
<br />
** RUN THIS REPOSITORY (COPY & PASTE)**
 
- clone this repository
 `git clone https://github.com/Nata8/INSPiRE_BC.git`
<br />
<br />
<br />


**Python scripts:**

`pdbdownloader.py` <br />
 - It downloads protein structures from PDB database. The input is a file with pdb ids and path to storage.
 
`comparer.py` <br />
 - The input is one or more files with pdb ids (datasets). Then the same PDB identifiers are searched for within one dataset and also within all of them.
 
`classifier.py` <br />
 - It divides residues within protein structure into two sets - interface and non interface. Output is a number of each set and its percentage.
 
 `remark.py` <br />
  - It searches for monomers from PDB structures based on information from REMARK 350. 
    The input is the path to a single pdb file or to a directory with multiple pdb files. The result is a file with a binary classification - true/false. 

 `csvparser.py` <br />
  - The output of INSPiRE is a csv file with the residue and its classification on each line. Based on the information from the aforementioned csv file,
    this script determines the absolute and relative numbers of "N" and "I" in each protein structure. The result can be saved  to the selected directory 
    in json format.
 
 `statistics.py` <br />
  - Simple exploration of the resulting data from csv_parser.py. The output shows the number of protein structures, the average percentage of "I" residues 
    in the structures, the maximum and minimum of the relative "I" counts.
 
 `classifier.py` <br />
  - It classifies structures from the output file created by the csv_parser.py script based on the threshold that is set as a global variable. 
    The result is the number and list of complexes that are evaluated as not containing a biological interface.
  
 `from_ent_to_pdb.py` <br />
  - Simple script to transform ent files to pdb files.
  
 `eppicdownloader.py` <br />
  - It downloads assemblies from EPPIC tool. Input is pdb identifier, its assembly numeric identifier and destination directory to save. 
    The resulting assemblies are in cif format.
    <br />
    <br />
  <br />
  
 **DATASETS:**
    
  Datasets (`Ponstingl, DC and Many`) are stored in [dataset directory](https://github.com/Nata8/INSPiRE_BC/tree/main/datasets). <br />
  <br />
  Original sources <br />
  -  [DC and Many](https://github.com/eppic-team/datasets/tree/master/data) <br />
  -  [Ponstingl](https://onlinelibrary.wiley.com/doi/10.1002/1097-0134%2820001001%2941%3A1%3C47%3A%3AAID-PROT80%3E3.0.CO%3B2-8) <br />
  <br />
  <br />
  <br />
  
  **INSPiRE pipeline:**
  
  You can find applied INSPiRE commands in this [file](https://github.com/Nata8/INSPiRE_BC/blob/main/INSPiRE_results/working_with_INSPiRE.md)
  
  For more infor type `man inspire`
  <br />
    <br />
    <br />
 
  **RESULTS:**
  - from classifier `EPPIC` using DC dataset are in this [directory](https://github.com/Nata8/INSPiRE_BC/tree/main/EPPIC_results) <br />
  - from classifier `INSPiRE`: <br />
        using Many dataset - this [directory](https://github.com/Nata8/INSPiRE_BC/tree/main/MANYXTAL_check) <br />
        using DC dataset - this [directory](https://github.com/Nata8/INSPiRE_BC/tree/main/INSPiRE_results) <br />
        using Ponstingl dataset - this [directory](https://github.com/Nata8/INSPiRE_BC/tree/main/PONSTINGL_results) <br />

 

 
 

 
 

 
 








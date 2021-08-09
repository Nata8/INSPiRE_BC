# INSPiRE_BC

Repository created for the purpose of storing/viewing the scripts and results for bachelor thesis **`"Identification of crystal packing contacts using a method for detection of protein-protein interaction sites"`**. 

**REQUIREMENTS:** <br />
[INSPiRE](https://github.com/Jelinek-J/INSPiRE) <br />
[Python version 3.7.9](https://www.python.org/) <br />
[Biopython](https://biopython.org/) <br />
[EPPIC](https://www.eppic-web.org/ewui/) <br />
[MakeMultimer](http://watcut.uwaterloo.ca/tools/makemultimer/) <br />
[Pandas](https://pandas.pydata.org/)


*Python scripts:*

`pdbdownloader.py` <br />
 - It downloads protein structures from PDB database. The input is a file with pdb ids and path to storage.
 
`comparer.py` <br />
 - The input is one or more files with pdb ids (datasets). Then the same PDB identifiers are searched for within one dataset and also within all of them.
 
`classifier.py` <br />
 - It divides residues within protein structure into two sets - interface and non interface. Output is a number of each set and its percentage.
 
 `remark.py` <br />
  It searches for monomers from PDB structures based on information from REMARK 350. 
  The input is the path to a single pdb file or to a directory with multiple pdb files. The result is a file with a binary classification - true/false. 

 `csvparser.py` <br />
 
 
 `from_ent_to_pdb.py` <br />
  - Simple script to transform ent files to pdb files.
 
 
 `interface.py` <br />
 
 

 
 

 
 
 `statistics.py` <br />







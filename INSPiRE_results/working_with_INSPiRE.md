In this section, there are used commands for the INSPiRE classifier.


For more info enter **man inspire**.

- `-s <PATH-TO-PROTEIN,>`  Path  to  a  protein  or  a  directory  with  proteins  that  should  be used.
- `-x <TEMP-DIR,>`  Path to a directory, where to store temporary files.
- `-k <KNOWLEDGE-BASE,>` Path to a directory, where is/ should be stored a knowledge-base.
- `-m Construction mode:` knowledge-base will be constructed instead of used for prediction.
- `-i<RADDI-FILE, distance>` Redefines  radii  of  chemical  elements  using  RADII-FILE  and optionally DISTANCE resets the maximal
                          allowed distance of two radiuses.
- `-q<OUTPUT-PATH>` Where  to  store  output file.
 

1. Creating a knowledge-base
   
   **cd INSPiRE/src** <br>
   **inspire -s <path_to_dataset> -xknowledge_base -kknowledge_base -m**
   
2. Finding residues at a maximum distance 6Å from another chain and they create biological interface

   **features knowledge_base/residues.ind knowledge_base/interfaces-0-6.tur "-iknowledge_base/radiuses.rus;6" <path_to_dataset>**
   
   Then it is needed to remove the original interfaces.tur and replace (rename) it with the new interfaces-0-6.tur
   
3. Test part 
  
    **inspire -s <path_to_dataset> -kknowledge_base -qresults**

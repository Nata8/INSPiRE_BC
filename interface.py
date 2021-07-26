#! /usr/bin/python

from Bio.PDB.PDBList import PDBList
from pdbparser import Parser
from sys import exit

import os
import itertools
import numpy as np
import json

JSON_FILE = "local_data/interfaces.json"

def save_to_json(protein, interfaces):
    with open(JSON_FILE, "w") as json_file:
        json_data = {protein: {}}
        for chain, chain_interfaces in interfaces:
            json_data[protein][chain] = chain_interfaces


def main(protein):
    parser = Parser(protein=protein)
    chains = parser.find_remark(350, pattern="APPLY THE FOLLOWING TO CHAINS: ")

    print("-" * 50)
    print(parser.COLOR_GREEN + protein.center(50) + parser.COLOR_END)
    print("-" * 50)
    
    if chains:
        chains = [chain_obj for chain_obj in parser.structure.get_chains() if chain_obj.get_full_id()[2] in chains]
        chains_list = np.array([(chain, np.array([atom for atom in chain.get_atoms()])) for chain in chains], dtype=object)
    else:
        parser.send_error(protein.upper() + " is a monomer! Skipping...")
        return

    if len(chains_list) < 2:
        parser.send_error("Selected protein has not enought chains")
        structure = None
        return
    
    interfaces = {}
    for chain in chains:
        interfaces[chain.get_full_id()[2]] = []

    for (chain1, atoms1), (chain2, atoms2) in itertools.combinations(chains_list, 2):
        neighbors = parser.get_neighbor_atoms(atoms1, atoms2)

        for neighbor1, neighbor2 in neighbors:
            residue1 = neighbor1.get_parent()
            residue2 = neighbor2.get_parent()
            residue1_id = residue1.get_full_id()[3][1]
            residue2_id = residue2.get_full_id()[3][1]

            chain1_id = chain1.get_full_id()[2]
            chain2_id = chain2.get_full_id()[2]

            if not residue1_id in interfaces[chain1_id]:
                interfaces[chain1_id].append(residue1_id)

            if not residue2_id in interfaces[chain2_id]:
                interfaces[chain2_id].append(residue2_id)
            #residue_id_tuple = (f"{chain1.get_full_id()[2]} - {residue1_id}", f"{chain2.get_full_id()[2]} - {residue2_id}")

    for chain, chain_interfaces in interfaces.items():
        print(f"{parser.COLOR_BLUE}{chain}{parser.COLOR_END} -> {sorted(chain_interfaces)}\n")
    #print("-" * 100, f"\n{parser.COLOR_BLUE}[{residue1} - {residue2}]{parser.COLOR_END}\n{neighbors}")

if __name__ == "__main__":
    valid = False
    while not valid:
        try:
            protein = input("Enter protein ID or path to a file of proteins >>> ")
        except KeyboardInterrupt:
            exit()

        if os.path.exists(protein) and protein.endswith(".txt"):
            file_of_proteins = os.path.abspath(protein)
            with open(file_of_proteins, "r") as f:
                print("Reading file at", file_of_proteins)
                for line in f.readlines():
                    main(line.replace("\n", ""))
        else:
            main(protein)

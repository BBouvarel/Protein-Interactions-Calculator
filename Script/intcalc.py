#!/usr/bin/env python

import math
import atom


def calc_range(elem1, elem2):
    """
    function allowing the calculation of the distance of two atoms

    :param elem1, elem2: two objects of the class atom
    :return: distance between two atoms
    """
    dist = math.sqrt((elem2.x-elem1.x)**2+
                     (elem2.y-elem1.y)**2+
                     (elem2.z-elem1.z)**2)
    return dist


def add_to_list(line, liste):
    """
    :param line: line of the pdb file containing the element of interest
    :param liste: list containing the objects of class atom
    :return: list of objects of class atom with the new element added
    """
    liste.append(atom.Atom(line[12:15].strip(), line[22:26].strip(),
                           line[17:20].strip(), line[21:22].strip(),
                           line[30:38].strip(), line[38:46].strip(),
                           line[46:54].strip()))
    return liste


def parsing(pdb, name, res):
    """
    function allowing the parsing of the pdb file following certain conditions

    :param pdb: the pdb file given by the user
    :param name: atom name
    :param res: list of residues containing the element
    :return: list of objects of class atom that respect the conditions
    """
    elements = []
    with open(pdb, "r") as finput:
        for line in finput:
            if line[0:6].strip() == "ATOM":
                # if the line describe an atom
                if line[17:20].strip() in res and len(res) != 0:
                    # if the residue of the line contain this specific atom
                    if line[12:15].strip() in name and len(name) != 0:
                        # if the atom of the line is the desired atom
                        elements = add_to_list(line, elements)
                elif len(res) == 0:
                    if line[12:15].strip() in name and len(name) != 0:
                        elements = add_to_list(line, elements)

    return elements


def calc_centroid():
    pass


def print_header():
    """
    function printing the head of the result's table
    """
    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Position",
                                                              "Residue", "Chain",
                                                              "Position", "Residue",
                                                              "Chain", "Distance"))


def print_pos_res_ch_dis(pos1, res1, chain1, pos2, res2, chain2, dist):
    """
    function printing the the result's table
    """
    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10.2f}"
          .format(pos1, res1, chain1, pos2, res2, chain2, dist))


def print_hydrogen_header():
    """
    function printing the head of the result's table
    """
    print("{:^10}{:^10}{:^10}{:^10}{:^10}"
          "{:^10}{:^10}{:^10}{:^10}".format("Position", "Residue", "Chain",
                                            "Atom", "Position", "Residue", "Chain",
                                            "Atom", "Distance"))


def print_hydrogen_res(posd, resd, chaind, named, posa, resa, chaina, namea, dist):
    """
    function printing the the result's table
    """
    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10.2f}"
          .format(posd, resd, chaind, named, posa, resa, chaina, namea, dist))

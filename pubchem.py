import pubchempy as pcp

# input name of the compound
chemical_compound = input("Please enter name of the compound: ")
try:
    # get the compound from PubChem
    compound = pcp.get_compounds(chemical_compound, 'name')[0]
    print(f"PubChem CID: {compound.cid}")
    print(f"IUPAC name: {compound.iupac_name}")
    print(f"Common name: {compound.synonyms[0]}")
    print(f"Molecular weight: {compound.molecular_weight}")
    print(f"Molecular formula: {compound.molecular_formula}")
    print(f"Canonical SMILES: {compound.isomeric_smiles}")
except:
    print(f"The compound {chemical_compound} is not in the PubChem database.")
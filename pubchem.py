import pubchempy as pcp
import os
import requests

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
url = 'https://go.drugbank.com/releases/5-1-12/downloads/all-full-database'
response = requests.get(url, auth=(username, password))
with open('filename.zip', 'wb') as f:
    f.write(response.content)
print('Download completed!')
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
    print(f"Isomeric SMILES: {compound.canonical_smiles}")
except:
    print(f"The compound {chemical_compound} is not in the PubChem database.")



#DBank API....
drug_id = 'DB01048'

# Construct the URL for the API request
url = f'https://api.drugbank.com/v1/drugs/{drug_id}'

# Set the authorization header with the API key


# Send the request to the DrugBank API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    drug_data = response.json()

    # Print out some structural information
    print(f"Drug Name: {drug_data['name']}")
    print(f"SMILES: {drug_data['structure']['smiles']}")
    print(f"InChI: {drug_data['structure']['inchi']}")
    print(f"InChIKey: {drug_data['structure']['inchikey']}")

    # Additional details like molecular weight
    print(f"Molecular Weight: {drug_data['properties']['molecular_weight']}")
else:
    print(f"Failed to retrieve data for {drug_id}. Status Code: {response.status_code}")
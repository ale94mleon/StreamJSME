from StreamJSME import StreamJSME
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
from io import BytesIO
import streamlit as st
st.title('✍️ molecules with JSME in Streamlit 🤩')
# Create a first plot with an input SMILES, by default smiles = 'C'
update_smiles = StreamJSME(smiles='CCC')

st.subheader('Using the draw molecule inside RDKit')
st.write(f"New SMILES = {update_smiles}")
mol = Chem.MolFromSmiles(update_smiles)
st.write(f"MolLogP = {Descriptors.MolLogP(mol)}\n\nTPSA = {Descriptors.TPSA(mol)}")

st.subheader('Getting the RDKit image')
img = Draw.MolToImage(mol)
bio = BytesIO()
img.save(bio, format='png')
st.image(img)

from StreamJSME import StreamJSME
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
from io import BytesIO
import streamlit as st
st.title('✍️ molecules with JSME in Streamlit')

with st.expander('**Code**'):
    st.markdown("""You must have a `requirements.txt` in the directory of the Streamlit App

```bash
streamlit
rdkit
StreamJSME
```

And also `packages.txt` at the root directory of your GitHub repo

```bash
libxrender1
```

Finally the python code: 

``` python
from StreamJSME import StreamJSME
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
from io import BytesIO
import streamlit as st
st.title('✍️ molecules with JSME in Streamlit')

# Create a first plot with an input SMILES, by default smiles = 'C'
update_smiles = StreamJSME(smiles='CCC')

st.subheader('Using the draw molecule inside RDKit')
st.write(f"New SMILES = {update_smiles}")
mol = Chem.MolFromSmiles(update_smiles)
st.write(f"MolLogP = {Descriptors.MolLogP(mol)}")
st.write(f"TPSA = {Descriptors.TPSA(mol)}")

with st.expander('You can even retrieve the highlighted atoms on RDKit'):
    selected_atoms = [atom for atom in mol.GetAtoms() if atom.GetAtomMapNum() == 1]
    st.write(f'**Number of highlighted atoms**: {len(selected_atoms)}')
    for atom in selected_atoms:
        st.write(f"**Atom**: {atom.GetSymbol()}{atom.GetIdx()}")

st.subheader('Getting the RDKit image')
img = Draw.MolToImage(mol)
bio = BytesIO()
img.save(bio, format='png')
st.image(img)
```

Check [StreamJSME GitHub Repo](https://github.com/ale94mleon/StreamJSME).
""")



# Create a first plot with an input SMILES, by default smiles = 'C'
update_smiles = StreamJSME(smiles='CCC')

st.subheader('Using the draw molecule inside RDKit')
st.write(f"New SMILES = {update_smiles}")
mol = Chem.MolFromSmiles(update_smiles)
st.write(f"MolLogP = {Descriptors.MolLogP(mol)}")
st.write(f"TPSA = {Descriptors.TPSA(mol)}")

with st.expander('You can even retrieve the highlighted atoms on RDKit'):
    selected_atoms = [atom for atom in mol.GetAtoms() if atom.GetAtomMapNum() == 1]
    st.write(f'**Number of highlighted atoms**: {len(selected_atoms)}')
    for atom in selected_atoms:
        st.write(f"**Atom**: {atom.GetSymbol()}{atom.GetIdx()}")

st.subheader('Getting the RDKit image')
img = Draw.MolToImage(mol)
bio = BytesIO()
img.save(bio, format='png')
st.image(img)

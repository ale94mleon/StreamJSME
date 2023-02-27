#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For information of TOFF:
    Docs: https://StreamJSME.readthedocs.io/en/latest/
    Source Code: https://github.com/ale94mleon/StreamJSME
"""
import os
import streamlit.components.v1 as components

_RELEASE = True


if _RELEASE:
    root_dir = os.path.dirname(__file__)
    build_dir = os.path.join(root_dir,'frontend/build')
    _StreamJSME = components.declare_component(
        'StreamJSME',
        path = build_dir
        )
else:
    _StreamJSME = components.declare_component(
            "StreamJSME",
            url = 'http://localhost:3001'
            )
# else:
#     parent_dir = os.path.dirname(os.path.abspath(__file__))
#     build_dir = os.path.join(parent_dir, "frontend/build")
#     _StreamJSME = components.declare_component("my_component", path=build_dir)

def StreamJSME(smiles:str = 'C', key = None) -> str:
    """This is the main function of the component.
    It will create an interactive drawing section and
    output the draw molecule

    Parameters
    ----------
    smiles : str, optional
        A valid SMILES string of a molecule, by default 'C'
    key : _type_, optional
        An identification in case that multiple instance are created, by default None

    Returns
    -------
    str
        The SMILES of the draw molecule
    """
    smiles = _StreamJSME(
        smiles = smiles,
        key = key,
        default = 'C'
        )
    return smiles

def example():
    if _RELEASE:
        print("To see the example set `_RELEASE = False` at the top of the script and be sure that you install (`npm install`) and and start (`npm start`) your frontend")
    else:
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



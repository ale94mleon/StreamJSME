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
    build_dir = os.path.join(root_dir, "static")
    _StreamJSME = components.declare_component("StreamJSME", path=build_dir)
else:
    _StreamJSME = components.declare_component(
        "StreamJSME", url="http://localhost:3001"
    )
# else:
#     parent_dir = os.path.dirname(os.path.abspath(__file__))
#     build_dir = os.path.join(parent_dir, "static")
#     _StreamJSME = components.declare_component("my_component", path=build_dir)


def StreamJSME(
    smiles: str = "C",
    height: int = 350,
    width: int = 500,
    margin: int = 50,
    src=None,
    key=None,
) -> str:
    """This is the main function of the component.
    It will create an interactive drawing section and
    output the draw molecule

    Parameters
    ----------
    smiles : str, optional
        A valid SMILES string of a molecule, by default 'C'
    height : int, optional
        The height of the drawing section, by default 350
    width : int, optional
        The width of the drawing section, by default 500
    margin: int, optional
        The margin of the drawing section, by default 50
    src : str, optional
        The source of the JSME editor, by default None
        If None, it will use the default JSME on github.io
    key : _type_, optional
        An identification in case that multiple instance are created, by default None

    Returns
    -------
    str
        The SMILES of the draw molecule
    """

    if src is None:
        # Fallback to the default JSME source
        src = "https://jsme-editor.github.io/dist/jsme/jsme.nocache.js"

    smiles = _StreamJSME(
        smiles=smiles,
        height=height,
        width=width,
        margin=margin,
        src=src,
        key=key,
        default="C",
    )
    return smiles


def example():
    if _RELEASE:
        print(
            "To see the example set `_RELEASE = False` at the top of the script and be sure that you install (`npm install`) and and start (`npm start`) your frontend"
        )
    else:
        from io import BytesIO

        import streamlit as st
        from rdkit import Chem
        from rdkit.Chem import Draw

        st.title("✍️ molecules with JSME in Streamlit 🤩")
        # Create a first plot with an input SMILES, by default smiles = 'C'
        update_smiles = StreamJSME(
            smiles="C",
            height=400,
            width=700,
            # src="http://localhost:3001/jsme/jsme.nocache.js",  # Change here if you want to use a custom JSME source
        )

        # st.subheader("Using the draw molecule inside RDKit")
        st.write(f"New SMILES = {update_smiles}")
        mol = Chem.MolFromSmiles(update_smiles)

        st.subheader("Getting the RDKit image")
        img = Draw.MolToImage(mol)
        bio = BytesIO()
        img.save(bio, format="png")
        st.image(img)


if __name__ == "__main__":
    example()

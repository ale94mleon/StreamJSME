#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For information of TOFF:
    Docs: https://StreamJSME.readthedocs.io/en/latest/
    Source Code: https://github.com/ale94mleon/StreamJSME
"""
from _version import __version__, __version_tuple__
import os
import streamlit.components.v1 as components
__author__ = "Alejandro Martínez León"
__email__ = "ale94mleon@gmail.com"

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

def StreamJSME(smiles='C', key = None):
    smiles = _StreamJSME(
        smiles = smiles,
        key = key,
        default = 'C'
        )
    return smiles

if not _RELEASE:
    s = StreamJSME()


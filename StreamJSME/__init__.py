#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For information of TOFF:
    Docs: https://StreamJSME.readthedocs.io/en/latest/
    Source Code: https://github.com/ale94mleon/StreamJSME
"""
import os
import streamlit.components.v1 as components

# Metadata
# We will use semantic version (major, minor, patch)
__main_version_tuple__ = (0, 0, 1)
__pre_version_tuple__ = None # or None or an empty tuple, the first char is alpha, beta, rc, etc...

if __pre_version_tuple__:
    __version_tuple__ = tuple(list(__main_version_tuple__) + list(__pre_version_tuple__))
    __version__ = '.'.join([str(i) for i in __main_version_tuple__]) + f'{__pre_version_tuple__[0][0]}' + '.'.join([str(i) for i in __pre_version_tuple__[1:]])
else:
    __version_tuple__ = __main_version_tuple__
    __version__ = '.'.join([str(i) for i in __main_version_tuple__])
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


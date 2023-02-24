import os
import streamlit.components.v1 as components

_RELEASE = False



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

def StreamJSME(smiles='C', key = None):
    response = _StreamJSME(
        smiles = smiles,
        key = key,
        default = {
            'data':{
                'smiles':'C'
                }
            }
        )
    smiles = response['data']['smiles']
    return smiles


StreamJSME()


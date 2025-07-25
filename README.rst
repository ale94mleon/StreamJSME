StreamJSME
==========

This package is intended to be used as a Molecule Draw component on `Streamlit <https://streamlit.io/>`_ applications. It uses `jsme-react <https://github.com/DouglasConnect/jsme-react>`_.

.. list-table::
    :widths: 12 35

    * - **Build**
      - |pypi-version|
    * - **Source Code**
      - |github|
    * - **Python Versions**
      - |pyversions|
    * - **Dependencies**
      - |streamlit| |JSME|
    * - **License**
      - |license|
    * - **Downloads**
      - |downloads|

Installation
------------

.. code-block:: bash

    pip install StreamJSME

Use
------------

.. code-block:: python

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

If trying to run the Streamlit application you get ``OSError: [Errno 28] inotify watch limit reached``,
just use the flag ``--server.fileWatcherType none``:

.. code-block:: bash

    streamlit run app.py --server.fileWatcherType none

Issues
------

If you have found a bug, please open an issue on the `GitHub Issues <https://github.com/ale94mleon/StreamJSME/issues>`_.

Discussion
----------

If you have questions on how to use **StreamJSME**, or if you want to give feedback or share ideas and new features, please head to the `GitHub Discussions <https://github.com/ale94mleon/StreamJSME/discussions>`_.

Acknowledgment
--------------
See the full list of contributors in the `CONTRIBUTORS.md <./CONTRIBUTORS.md>`_ file.


..  |pypi-version|  image:: https://img.shields.io/pypi/v/streamjsme.svg
    :target: https://pypi.python.org/pypi/streamjsme/
    :alt: pypi-version
..  |github|    image:: https://badgen.net/badge/icon/github?icon=github&label
    :target: https://github.com/ale94mleon/streamjsme
    :alt: GitHub-Repo
..  |pyversions|    image:: https://img.shields.io/pypi/pyversions/streamjsme.svg
    :target: https://pypi.python.org/pypi/streamjsme/
..  |streamlit| image:: https://img.shields.io/static/v1?label=Powered%20by&message=Streamlit&color=DC3C19&style=flat
    :target: https://streamlit.io/
    :alt: Streamlit
..  |jsme| image:: https://img.shields.io/static/v1?label=Powered%20by&message=JSME&color=9438ff&style=flat
    :target: https://jsme-editor.github.io/
    :alt: JSME
..  |license| image:: https://badgen.net/pypi/license/streamjsme/
    :target: https://pypi.python.org/pypi/streamjsme/
    :alt: license
..  |downloads| image:: https://static.pepy.tech/personalized-badge/streamjsme?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
    :target: https://pepy.tech/project/streamjsme
    :alt: download
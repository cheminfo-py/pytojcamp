Getting started
====================

Warnings
----------
pytojcamp currently only supports a small set of the JCAMP-DX specification. For example, we do not support any compression. We also do not enforce that standard vocabulary is used.



Installation
--------------

To install the latest stable release use

.. code-block:: bash

    pip install pytojcamp


The latest version of cheminfopy can be installed from GitHub using

.. code-block:: bash

    pip install git+https://github.com/cheminfo-py/pytojcamp.git



Writing JCAMP-DX files
-------------------------

The easiest way to write JCAMP-DX files with multiple columns is to use the :py:func`~pytojcamp.from_dict.from_dict` function.

.. code-block:: python

    jcamp = from_dict({
    'x': {
        "data": d['isotherm']["pressure"],
        "unit": d['isotherm']["pressure_unit"],
        "type": "INDEPENDENT"
    },
    'y': {
        "data": d['isotherm']["loading_absolute_average"],
        "unit": d['isotherm']["loading_absolute_unit"],
        "type": "DEPENDENT"
    }
    }, title="My spectrum", origin='here', owner='me',
        data_type='Adsorption Isotherm',
        meta={'adsorptive': 'N2'})

This will create data in the form :code:`DATA TABLE= (xy...xy), PEAKS` And add the :code:`OWNER`, :code:`ORIGIN`, :code:`TITLE` of the CORE section of the JCAMP-DX files.
Note that you always need to have the :code:`x` and :code:`y` keys in your dictionary.

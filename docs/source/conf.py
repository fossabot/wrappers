# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

import sys

from pathlib import Path

conf_dir = Path(__file__).resolve().parent
source_dir = conf_dir.parent.parent
sys.path.insert(0, str(source_dir))

# -- Project information -----------------------------------------------------

project = u'CRC Wrapper Applications'
copyright = u'2022, Pitt Center for Research Computing'
author = u'Pitt Center for Research Computing'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'autoapi.extension'
]

# Configure automatic documentation of commandline applications
autoapi_type = 'python'
autoapi_dirs = [str(source_dir / 'apps')]
autoapi_add_toctree_entry = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

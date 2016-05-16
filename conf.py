# -*- coding: utf-8 -*-

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# The suffix(es) of source filenames.
source_suffix = '.rst'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.napoleon'
]

autoclass_content = 'init'

# Add header to each RST file
import io
with io.open('synapse-includes.rst', encoding='utf-8') as file:
    rst_prolog = file.read()

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SNAP Connect'
copyright = u'2016, Synapse Wireless'
author = u'Synapse Wireless, Inc.'

# -- Options for HTML output ----------------------------------------------
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'synapse-includes.rst', 'README.rst']



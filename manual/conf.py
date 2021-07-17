# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Enroute Flight Navigation'
copyright = '2021, Stefan Kebekus'
author = 'Stefan Kebekus'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx_rtd_theme']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = ''

html_theme_options = {
    'globaltoc_depth': 1,
    'touch_icon': 'enroute.png',
#    'logo_icon': 'X',
    "nav_links": [
        {"href": "https://akaflieg-freiburg.github.io/enrouteText/manual", "internal": False, "title": "Online"},
        {"href": "https://akaflieg-freiburg.github.io/enrouteText/manual.epub", "internal": False, "title": "eBook"},
        {"href": "https://akaflieg-freiburg.github.io/enrouteText/manual.pdf", "internal": False, "title": "PDF"},
    ],
    'nav_title': 'Enroute Flight Navigation',
}

# globaltoc seems it's not added by default
html_sidebars = {
    "**": [
#        "logo-text.html",
        "globaltoc.html",
        "localtoc.html",
        "searchbox.html",
    ]
}

html_favicon = "enroute.png"

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'preamble': r'\input{../../latexPreamble.tex.txt}',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

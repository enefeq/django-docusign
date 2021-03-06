# -*- coding: utf-8 -*-
"""django-docusign documentation build configuration file.

Created by diecutter on .

This file is execfile()d with the current directory set to its containing dir.

"""
import os
import re


doc_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(doc_dir)
version_filename = os.path.join(project_dir, 'VERSION')

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.coverage',
              'sphinx.ext.intersphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'django-docusign'
project_slug = re.sub(r'([\W_.-]+)', u'-', project)
copyright = u'2014-2017 - PeopleDoc'
author = u'Benoît Bryon'
author_slug = re.sub(r'([\W_.-]+)', u'-', author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = open(version_filename).read().strip()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Ignore some warnings
suppress_warnings = ['image.nonlocal_uri']


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['globaltoc.html',
           'relations.html',
           'sourcelink.html',
           'searchbox.html'],
}

# Output file base name for HTML help builder.
htmlhelp_basename = u'{project}doc'.format(project=project_slug)


# -- Options for sphinx.ext.intersphinx ---------------------------------------

intersphinx_mapping = {
    'python': (
        'http://docs.python.org/2.7',
        None),
    'django': (
        'https://docs.djangoproject.com/en/1.10/',
        'https://docs.djangoproject.com/en/1.10/_objects/'),
    'pydocusign': (
        'https://pydocusign.readthedocs.org/en/latest/',
        None),
    'djangoanysign': (
        'https://django-anysign.readthedocs.org/en/latest/',
        None),
}

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     u'{project}.tex'.format(project=project_slug),
     u'{project} Documentation'.format(project=project),
     author,
     'manual'),
]


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index',
     project,
     u'{project} Documentation'.format(project=project),
     [author],
     1)
]


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index',
     project_slug,
     u'{project} Documentation'.format(project=project),
     author,
     project,
     'One line description of project.',
     'Miscellaneous'),
]

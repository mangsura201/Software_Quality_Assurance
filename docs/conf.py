# Configuration file for the Sphinx documentation builder.
#
#source_dir = '../path_to_your_source_directory'
import os
import sys
import django
# Add the Django project directory to the Python path
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../OnlineBankingManagement'))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'OnlineBankingManagement.settings'
django.setup()


master_doc = 'index'
language = 'en'


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OnlineBankingManagementSystem'
copyright = '2024, ShifatiRabbi & Team members'
author = 'ShifatiRabbi & Team members'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
    'members': True,  # Include all members (methods, attributes, etc.)
    'undoc-members': True,  # Include members without docstrings
    'show-inheritance': True,  # Show inherited members
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

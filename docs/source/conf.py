# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'LeU Vademecum'
copyright = '2024, Kemosh'
author = 'Kemosh'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'rst2pdf.pdfbuilder',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinxdoc'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
pdf_name = project
pdf_doc_title = project
pdf_documents = [('index', pdf_name, pdf_doc_title, author)]

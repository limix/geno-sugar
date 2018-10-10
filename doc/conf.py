from __future__ import unicode_literals

import sphinx_rtd_theme


def get_version():
    import geno_sugar

    return geno_sugar.__version__


extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "Geno Sugar"
copyright = "2018, Francesco Paolo Casale"
author = "Francesco Paolo Casale"
version = get_version()
release = version
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "conf.py"]
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = "genosugardoc"
man_pages = [(master_doc, "geno_sugar", "Geno Sugar Documentation", [author], 1)]
texinfo_documents = [
    (
        master_doc,
        "geno_sugar",
        "Geno Sugar Documentation",
        author,
        "geno_sugar",
        "Utils for GWAS using plink and bgen files.",
        "Miscellaneous",
    )
]
intersphinx_mapping = {"https://docs.python.org/": None, "http://matplotlib.org": None}

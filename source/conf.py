"""
Configuration file for the Sphinx documentation builder.
Documentation: http://www.sphinx-doc.org/en/master/config
"""

# -- Imports -----------------------------------------------------------------

import datetime

# -- Project Information -----------------------------------------------------

project = "novelWriter"
copyright = f"{datetime.date.today().year}"
author = "Veronica Berglyd Olsen"

# -- General Configuration ---------------------------------------------------

needs_sphinx = "5.0"
extensions = []
templates_path = []
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = []

# -- Options for HTML Output -------------------------------------------------

html_theme = "sphinx_book_theme"
html_title = ""
html_static_path = ["_static"]
html_theme_options = {
    "logo": {
        "image_light": "_static/novelwriter-light.png",
        "image_dark": "_static/novelwriter-dark.png",
    },
    "repository_url": "https://github.com/vkbo/novelwriter",
    "use_repository_button": True,
}

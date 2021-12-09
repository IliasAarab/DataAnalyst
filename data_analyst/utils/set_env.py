"""Setup of jupyter notebook based environment"""


## Main libraries to use for everyday data analytics work
# --------------------------------------------------------
# To import the libs & assocciated namespaces into JN use:
# from data_analyst.utils.set_env import *

# JN libs
from IPython.display import display, Markdown, Latex

# Standard libs
import glob
import os

# DS libs
import numpy as np
import pandas as pd

# Graphing libs
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Excel libs
from win32com.client import Dispatch
import openpyxl

# ECB libs
from connectors import disc

# -----------------------------------------------------------

## Settings for Jupyter Notebook
# -----------------------------------------------------------
# Option to turn Jedi off in case it messes up autocompletion
# Sets dir one folder up to access relevant folders easily (based on cookiecutter folder structure)

# Environment variables
ACTIVE_RELOAD = False
ACTIVE_CHDIR = False
PATH_ORGINAL = None


def ipython_settings(
    jedi: bool = False, reset_state: bool = False, verbose: bool = True
) -> None:

    ## Global settings
    # ----------------------------
    global ACTIVE_RELOAD, ACTIVE_CHDIR, PATH_ORGINAL
    if PATH_ORGINAL is None:
        PATH_ORGINAL = os.getcwd()
    if reset_state:
        ACTIVE_RELOAD = False
        ACTIVE_CHDIR = False
        os.chdir(PATH_ORGINAL)
    get_ipython().magic(f"%config Completer.use_jedi = {jedi} ")
    if not ACTIVE_RELOAD:
        ACTIVE_RELOAD = True
        get_ipython().magic(f"%load_ext autoreload")
        get_ipython().magic(f"%autoreload 2")
    if not ACTIVE_CHDIR:
        ACTIVE_CHDIR = True
        os.chdir("..")
        if verbose:
            display(Markdown(f"Working directory: {os.getcwd()}"))

    ## Lib settings
    # -----------------
    pd.options.mode.chained_assignment = None
    pd.options.plotting.backend = "plotly"
    plotly.io.templates.default = "ggplot2"

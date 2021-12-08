# Standard libs
from IPython.display import display, Markdown, Latex
from win32com.client import Dispatch
import glob
import os

# External libs
import numpy as np
import pandas as pd
import openpyxl
import plotly
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# ECB libs
from connectors import disc


# Enviroment variables
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
    pio.templates.default = "ggplot2"

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
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

# Excel libs
from win32com.client import Dispatch
import openpyxl

# ECB libs
# from connectors import disc

# -----------------------------------------------------------

## Settings for Jupyter Notebook
# -----------------------------------------------------------
# Option to turn Jedi off in case it messes up autocompletion
# Sets dir one folder up to access relevant folders easily (based on cookiecutter folder structure)


class IPythonConfig:
    # Environment variables
    PATH_ORGINAL = None

    def __init__(self):
        if IPythonConfig.PATH_ORGINAL is None:
            IPythonConfig.PATH_ORGINAL = os.getcwd()

    def config_jedi(self, jedi=False):
        get_ipython().magic(f"%config Completer.use_jedi = {jedi} ")

    def set_cwd(self, cwd=True, verbose=True):
        if isinstance(cwd, bool):
            os.chdir("..")
        else:
            os.chdir(cwd)
        if verbose:
            display(Markdown(f"Working directory: {os.getcwd()}"))

    def set_autoreload(self):
        get_ipython().magic(f"%load_ext autoreload")
        get_ipython().magic(f"%autoreload 2")

    def reset_config(self):

        # Revert cwd
        try:
            os.chdir(IPythonConfig.PATH_ORGINAL)
        except:
            pass

        # Revert autoreload function
        get_ipython().magic(f"%autoreload 0")

        # Revert jedi
        get_ipython().magic(f"%config Completer.use_jedi = True")
    
    def config_libs(lib= True):
        
        # Pandas
        pd.options.mode.chained_assignment = None
        pd.options.plotting.backend = "plotly"
        # Pandas thousand separator + 2 decimal rounding
        pd.set_option('display.float_format', '{:,.2f}'.format)
        # pandas latex
        pd.set_option('display.notebook_repr_html', True)
        def _repr_latex_(self):
            return "\\begin{center} \n %s \n \\end{center}" % self.to_latex()
        pd.DataFrame._repr_latex_ = _repr_latex_  # monkey patch pandas DataFrame to latex
        
        # Plotly
        pio.renderers.default = "notebook+pdf+vscode+jupyterlab"
        pio.templates.default = "ggplot2"

        if lib == True:
            lib= ['pandas', 'numpy', 'plotly', 'matplotlib', 'tensorflow']
        elif isinstance(lib, list):
            lib = [i.lower() for i in list]
        else:
            raise AttributeError("lib should be bool or list of strings!")

        if 'pandas' in lib:
            pd.options.mode.chained_assignment = None
            pd.options.plotting.backend = "plotly"
            # Pandas thousand separator + 2 decimal rounding
            pd.set_option('display.float_format', '{:,.2f}'.format)
            # pandas latex
            pd.set_option('display.notebook_repr_html', True)
            def _repr_latex_(self):
                return "\\begin{center} \n %s \n \\end{center}" % self.to_latex()
            pd.DataFrame._repr_latex_ = _repr_latex_  # monkey patch pandas DataFrame to latex
        
        if 'numpy' in lib:
            np.set_printoptions(precision=2)

        if 'plotly' in lib:
            pio.renderers.default = "notebook+pdf+vscode+jupyterlab"
            pio.templates.default = "ggplot2"'
            plotly_config= {'staticPlot': True}

        if 'tf' in lib or 'tensorflow' in lib:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #no info and warnings printed







# # Environment variables
# ACTIVE_RELOAD = False
# ACTIVE_CHDIR = False
# PATH_ORGINAL = None


# def ipython_settings(
#     jedi: bool = False, reset_state: bool = False, verbose: bool = True
# ) -> None:
#     """Modify Jupyter Notebook config

#     Parameters
#     ----------
#     jedi : bool, optional
#         Whether to enable Jedi autocompletion, by default False
#     reset_state : bool, optional
#         Reset config back to original state, by default False
#     verbose : bool, optional
#         Whether to print out progress, by default True
#     """

#     ## Global settings
#     # ----------------------------
#     global ACTIVE_RELOAD, ACTIVE_CHDIR, PATH_ORGINAL
#     if PATH_ORGINAL is None:
#         PATH_ORGINAL = os.getcwd()
#     if reset_state:
#         ACTIVE_RELOAD = False
#         ACTIVE_CHDIR = False
#         os.chdir(PATH_ORGINAL)
#         get_ipython().magic(f"%autoreload 0")
#         get_ipython().magic(f"%config Completer.use_jedi = {jedi} ")
#     if not ACTIVE_RELOAD:
#         ACTIVE_RELOAD = True
#         get_ipython().magic(f"%load_ext autoreload")
#         get_ipython().magic(f"%autoreload 2")
#     if not ACTIVE_CHDIR:
#         ACTIVE_CHDIR = True
#         os.chdir("..")
#         if verbose:
#             display(Markdown(f"Working directory: {os.getcwd()}"))

#     ## Lib settings
#     # -------------------------------------------
#     # Pandas
#     pd.options.mode.chained_assignment = None
#     pd.options.plotting.backend = "plotly"
#     # Plotly
#     pio.renderers.default = "notebook+pdf+vscode+jupyterlab"
#     plotly.io.templates.default = "ggplot2"


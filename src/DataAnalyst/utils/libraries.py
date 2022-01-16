"""Load standard data science packages into running Python kernel"""

## Main libraries to use for everyday data analytics/science work
# --------------------------------------------------------
# To import the libs & assocciated namespaces into JN use:
# from data_analyst.utils.libraries import *
# TODO: install missing packages automatically

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

# import openpyxl

# ECB libs
# from connectors import disc

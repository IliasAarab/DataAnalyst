"""Setup of jupyter notebook based environment"""


# Main libs
# --------------------
from IPython.display import display, Markdown, Latex
import os
import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
try:
    from met_brewer.palettes import dwdw
except (ModuleNotFoundError, ImportError):
    print("""met_brewer is missing, install using 'pip install "git+https://github.com/BlakeRMills/MetBrewer.git#subdirectory=Python"' """)
    
    
## Settings for Jupyter Notebook
# -----------------------------------------------------------
# Option to turn Jedi off in case it messes up autocompletion
# Sets dir one folder up to access relevant folders easily (based on cookiecutter folder structure)


class IPythonConfig:
    """Modify Jupyter Notebook configuration"""

    # Environment variables
    PATH_ORGINAL = None

    def __init__(self):
        pass

    @staticmethod
    def config_jedi(jedi=False):
        """Whether to disable/enable jedi. Disable in case autocompletion is getting stuck.

        Parameters
        ----------
        jedi : bool, optional
            enable/disable jedi, by default False
        """
        get_ipython().magic(f"%config Completer.use_jedi = {jedi} ")

    @staticmethod
    def set_cwd(cwd=True, verbose=True):
        """Changes current working directory

        Parameters
        ----------
        cwd : bool, optional
            If True changes cwd one level up. Else input str of path, by default True
        verbose : bool, optional
            If verbose print display cwd, by default True
        """
        if IPythonConfig.PATH_ORGINAL is None:
            IPythonConfig.PATH_ORGINAL = os.getcwd()
        if isinstance(cwd, bool):
            os.chdir("..")
        else:
            os.chdir(cwd)
        if verbose:
            display(Markdown(f"Working directory: {os.getcwd()}"))

    @staticmethod
    def set_autoreload():
        """Activates autoreload magic command to automatically reload in-house modules whenever a change in the module happens."""
        get_ipython().magic(f"%reload_ext autoreload")
        get_ipython().magic(f"%autoreload 2")

    @staticmethod
    def reset_config():
        """Resets configuration to initial state when Kernel started."""

        # Revert cwd
        try:
            os.chdir(IPythonConfig.PATH_ORGINAL)
        except:
            pass

        # Revert autoreload function
        get_ipython().magic(f"%autoreload 0")

        # Revert jedi
        get_ipython().magic(f"%config Completer.use_jedi = True")

    @staticmethod
    def config_libs(lib=True):
        """Modify configuration of standard data science packages. Currently encapsulates:\
            Pandas, Numpy, Tensorflow, Matplotlib and Plotly

        Parameters
        ----------
        lib : bool, optional
            If true configure all libs. Else input list of package names as str, by default True

        Returns
        -------
        In case plotly is configured, plotly_config contains dict for fig.show(config)

        Raises
        ------
        AttributeError
            lib arg must be True or list of package names
        """

        if lib == True:
            lib = ["pandas", "numpy", "plotly", "matplotlib", "tensorflow"]
        elif isinstance(lib, list):
            lib = [i.lower() for i in lib]
        else:
            raise AttributeError("lib should be bool or list of strings!")

        
        import warnings
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        if "pandas" in lib:
            pd.options.mode.chained_assignment = None
            pd.options.plotting.backend = "plotly"
            # Pandas thousand separator + 2 decimal rounding
            pd.set_option("display.float_format", "{:,.2f}".format)
            # pandas latex
            pd.set_option("display.notebook_repr_html", True)

            def _repr_latex_(self):
                return "\\begin{center} \n %s \n \\end{center}" % self.to_latex()

            pd.DataFrame._repr_latex_ = (
                _repr_latex_  # monkey patch pandas DataFrame to latex
            )

        if "numpy" in lib:
            np.set_printoptions(precision=2, suppress=True)

        if "plotly" in lib:
            pio.renderers.default = "notebook+pdf+vscode+jupyterlab+colab"
            pio.templates["metbrewer"] = go.layout.Template(
            layout=go.Layout(colorway=met_brew(name="Greek", brew_type="discrete"))
                                         )
            pio.templates.default = "plotly_white+presentation+metbrewer"
            IPythonConfig.plotly_config = {"staticPlot": True}

        if "tf" in lib or "tensorflow" in lib:
            os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # no info and warnings printed

        if "matplotlib" in lib:
            import matplotlib.font_manager
            from matplotlib_inline.backend_inline import set_matplotlib_formats

            get_ipython().magic(f"%config InlineBackend.figure_format = 'png'")
            get_ipython().magic(f"%matplotlib inline")
            set_matplotlib_formats("pdf", "png")
            plt.rcParams["figure.autolayout"] = False
            plt.rcParams["figure.figsize"] = 10, 6
            plt.rcParams["axes.labelsize"] = 18
            plt.rcParams["axes.titlesize"] = 20
            plt.rcParams["font.size"] = 16
            plt.rcParams["lines.linewidth"] = 2.0
            plt.rcParams["lines.markersize"] = 8
            plt.rcParams["legend.fontsize"] = 14
            plt.rcParams["text.usetex"] = False
            plt.rcParams["font.family"] = "serif"
            # plt.rcParams['font.serif'] = "cm"
            plt.rcParams[
                "text.latex.preamble"
            ] = r"\usepackage{subdepth}, \usepackage{type1cm}"
            sns.set_context(context="notebook", font_scale=1.2)
            sns.set_palette(met_brew(name="Greek", brew_type="discrete")) 
            sns.set(rc={"figure.dpi": 100, "savefig.dpi": 600})
            set_matplotlib_formats("retina")
            sns.set_style(
                "ticks",
                {
                    "axes.grid": True,
                    "grid.linestyle": ":",
                    "grid.alpha": 1,
                    "grid.color": "#343434",
                    "lines.linewidth": 2.5,
                    "xtick.bottom": True,
                },
            )

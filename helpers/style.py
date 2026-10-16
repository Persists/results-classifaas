import matplotlib.pyplot as plt
import seaborn as sns


def use_paper_style():
    """Theme and fonts shared by all paper figures.

    Call this at the top of a paper-figure cell. Other cells in the notebooks call
    sns.set_theme(...) with a different font_scale, which silently changes the font
    sizes and the font family of every figure drawn afterwards.
    """
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.0)
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Linux Libertine"],
        "font.size": 9,
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{libertine}",
        "mathtext.fontset": "custom",
        "mathtext.rm": "Linux Libertine",
        "mathtext.it": "Linux Libertine:italic",
        "mathtext.bf": "Linux Libertine:bold",
        "hatch.linewidth": 0.5,
    })

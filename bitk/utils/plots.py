# AUTOGENERATED! DO NOT EDIT! File to edit: 03_utils_plots.ipynb (unless otherwise specified).

__all__ = ['scatter_plots_for_reduce_dimensional']

# Cell

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Cell

def scatter_plots_for_reduce_dimensional(df,x,y,output=None,hue=None,size=None,style=None,xlabel=None,ylabel=None,title=None):
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=x, y=y, data=df,hue=hue,size=size,style=style,)
    ax.legend(loc='best', ncol=2)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_title(title)
    if output is not None:
        fig.savefig(output,dpi=300)
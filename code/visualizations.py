
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter

# Standard data manipulation packages
import pandas as pd
import numpy as np

def result(data, title, color = ['grey','tab:blue','tab:red']):

    fig, ax = plt.subplots(figsize=(7,8))
    plt.rcParams.update({'font.size': 15})
    ax.bar(data.index[:3], 
           data.values[:3],
           color = color)
    for i, v in enumerate(data.values[:3]):
        ax.text(i - 0.1, v + 0.005, str(round(v, 2)), color='blue', fontweight='bold', fontsize = 15)
    ax.yaxis.set_major_formatter('{x:.0%}')
    ax.set_ylim(0, data.values[:3].max() + 0.05)
    ax.set_title(title, fontsize=20)
    plt.xticks(fontsize= 13)
    plt.yticks(fontsize= 13)
    plt.show()
    
    pass
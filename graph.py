import matplotlib.pyplot as plt
from enum import Enum

class Colormap(Enum):
    Default = None
    Blues = plt.cm.Blues
    Oranges = plt.cm.Oranges
    Reds = plt.cm.Reds

def histogram_plot(x_data, bins, title, x_label, y_label):
    plt.figure(figsize=(8,5))
    plt.hist(x_data, bins=bins, linewidth=1, edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.show()

def line_plot(df, title, x_label, y_label):
    plt.figure(figsize=(8,5))
    for col in df.columns:
        plt.plot(df.index, df[col], marker='o', label=str(col))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(title='Group')
    plt.tight_layout()
    plt.show()

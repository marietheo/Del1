import matplotlib.pyplot as plt

def plot_histogram(df, col, bins=20):
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=bins, edgecolor="black")
    plt.title(f"Histogram över {col}")
    plt.xlabel(col)
    plt.ylabel("Antal")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_boxplot(df, x_col, y_col):
    groups = df.groupby(x_col)[y_col].apply(list)
    plt.figure(figsize=(6,4))
    plt.boxplot(groups, labels=groups.index)
    plt.title(f"Boxplot av {y_col} per {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_bar(df, col):
    counts = df[col].value_counts(normalize=True)
    plt.figure(figsize=(6,4))
    counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(f"Andel {col}")
    plt.xlabel(col)
    plt.ylabel("Andel")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


import matplotlib.pyplot as plt
import os

def plot_histogram(df, col, bins=20, save=False, outdir="figures"):
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=bins, edgecolor="black")
    plt.title(f"Histogram över {col}")
    plt.xlabel(col)
    plt.ylabel("Antal")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    if save:
        os.makedirs(outdir, exist_ok=True)
        plt.savefig(f"{outdir}/hist_{col}.png", dpi=300, bbox_inches="tight")
    plt.show()

def plot_boxplot(df, x_col, y_col, save=False, outdir="figures"):
    groups = df.groupby(x_col)[y_col].apply(list)
    plt.figure(figsize=(6,4))
    plt.boxplot(groups, labels=groups.index)
    plt.title(f"Boxplot av {y_col} per {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    if save:
        os.makedirs(outdir, exist_ok=True)
        plt.savefig(f"{outdir}/box_{y_col}_per_{x_col}.png", dpi=300, bbox_inches="tight")
    plt.show()

def plot_bar(df, col, save=False, outdir="figures"):
    counts = df[col].value_counts(normalize=True)
    plt.figure(figsize=(6,4))
    counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(f"Andel {col}")
    plt.xlabel(col)
    plt.ylabel("Andel")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    if save:
        os.makedirs(outdir, exist_ok=True)
        plt.savefig(f"{outdir}/bar_{col}.png", dpi=300, bbox_inches="tight")
    plt.show()

import pandas as pd
import numpy as np

def descriptive_stats(df, cols):
    """
    Returnerar enkel deskriptiv statistik för valda kolumner.
    """
    stats_dict = {}
    for col in cols:
        stats_dict[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "min": df[col].min(),
            "max": df[col].max(),
            "std": df[col].std()
        }
    return pd.DataFrame(stats_dict).T

def disease_rate(df):
    """
    Beräknar andelen med sjukdom (1 = sjuk, 0 = frisk).
    """
    return df["disease"].mean()

def simulate_disease(n, p, seed=42):
    """
    Simulerar sjukdomsutfall med sannolikhet p.
    """
    np.random.seed(seed)
    return np.random.binomial(1, p, size=n)

import numpy as np

def ci_mean_normal(df, col, alpha=0.05):
    """
    Konfidensintervall för medelvärde med normalapproximation.

    """
    x = df[col].dropna()
    mean = x.mean()
    se = x.std(ddof=1) / np.sqrt(len(x))

    # Vanliga z-värden för olika konfidensnivåer
    z_table = {
        0.10: 1.645,  # 90% CI
        0.05: 1.960,  # 95% CI
        0.01: 2.576   # 99% CI
    }

    if alpha not in z_table:
        raise ValueError("Endast alpha = 0.10, 0.05 eller 0.01 stöds utan SciPy")

    z = z_table[alpha]
    return mean, (mean - z*se, mean + z*se)


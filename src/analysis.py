from src.metrics
import descriptive_stats, disease_rate, simulate_disease, ci_mean_normal
import pandas as pd

def full_analysis(df, numeric_cols, n_sim=1000, alpha=0.05):
    results = {}

    # 1. Deskriptiv statistik
    results["descriptive_stats"] = descriptive_stats(df, numeric_cols)

    # 2. Andel sjukdom
    results["disease_rate"] = disease_rate(df)

    # 3. Simulerad sjukdomsandel
    sim = simulate_disease(len(df), results["disease_rate"])
    results["simulated_rate"] = sim.mean()

    # 4. Konfidensintervall (normalapproximation)
    mean_norm, ci_norm = ci_mean_normal(df, "systolic_bp", alpha=alpha)
    results["ci_normal"] = (mean_norm, ci_norm)

    return results

# Health Study – Statistical Analysis Report


-> About the Project

This project presents a complete statistical workflow for analyzing a health study dataset containing 800+ observations. The analysis includes:

- **Descriptive statistics** for key health variables (age, weight, height, blood pressure, cholesterol)
- **Visualizations** (histograms, boxplots, bar charts)
- **Monte Carlo simulation** of disease prevalence
- **Confidence intervals** computed using two methods (normal approximation and bootstrap)
- **Hypothesis testing** to investigate whether smokers have higher systolic blood pressure
- **Power analysis** to assess the test's sensitivity

### Quick Start

1. Open `health_study_final_report.ipynb` in Jupyter
2. Run all cells in order: `Cell` → `Run All`
3. Results and visualizations are generated automatically

### Key Findings

| Analysis | Result | Interpretation |
|----------|--------|----------------|
| **Disease Prevalence** | ~10% | Approximately 1 in 10 individuals have the disease |
| **Simulated Prevalence** | ≈10% | Monte Carlo simulation confirms observed rate |
| **Mean Systolic BP** | ~149 mmHg | 95% CI: [148.3, 150.06] (both methods agree) |
| **Smokers vs Non-smokers** | p < 0.05 | Smokers have significantly higher BP |
| **Test Power** | ~0.85 | High power - test reliably detects true differences |


---





*Last updated: January 2025*





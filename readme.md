# Health Study – Statistical Analysis Report

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange)
![SciPy](https://img.shields.io/badge/SciPy-Latest-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A comprehensive statistical analysis of a health study dataset focusing on blood pressure, smoking habits, and disease prevalence.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Assignment Requirements](#assignment-requirements)
- [Results Summary](#results-summary)
- [Methodology](#methodology)
- [References](#references)
- [Author](#author)

---

## 📊 About the Project

This project presents a complete statistical workflow for analyzing a health study dataset containing 800+ observations. The analysis includes:

- **Descriptive statistics** for key health variables (age, weight, height, blood pressure, cholesterol)
- **Visualizations** (histograms, boxplots, bar charts)
- **Monte Carlo simulation** of disease prevalence
- **Confidence intervals** computed using two methods (normal approximation and bootstrap)
- **Hypothesis testing** to investigate whether smokers have higher systolic blood pressure
- **Power analysis** to assess the test's sensitivity

---

## ✨ Features

### 🔢 Statistical Analyses

- **Descriptive statistics**: Mean, median, min, max for continuous variables
- **Confidence intervals**: Normal approximation and bootstrap methods
- **Hypothesis testing**: Welch's t-test for group comparisons
- **Power analysis**: Bootstrap-based power estimation

### 📈 Visualizations

- Histogram of systolic blood pressure distribution
- Boxplot of weight by sex
- Bar chart showing proportion of smokers

### 🎲 Simulation

- Monte Carlo simulation of disease prevalence
- Bootstrap resampling for confidence intervals and power analysis
- Reproducible random number generation with seed

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab

### Step-by-Step Installation

1. **Clone or download the project**

```bash
# If you have git
git clone https://github.com/your-username/health-study-analysis.git
cd health-study-analysis

# Or download ZIP and extract
```

2. **Create virtual environment (recommended)**

```bash
python -m venv .venv

# Activate on Windows:
.venv\Scripts\activate

# Activate on Mac/Linux:
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

**Or manually:**

```bash
pip install pandas numpy scipy matplotlib jupyter
```

4. **Launch Jupyter Notebook**

```bash
jupyter notebook health_study_final_report.ipynb
```

---

## 📖 Usage

### Quick Start

1. Open `health_study_final_report.ipynb` in Jupyter
2. Run all cells in order: `Cell` → `Run All`
3. Results and visualizations are generated automatically

### Customizing the Analysis

#### Change Confidence Level

```python
# In the confidence interval cell
ci_norm = ci_mean_normal_approx(bp, alpha=0.01)  # 99% CI instead of 95%
ci_boot = ci_mean_bootstrap(bp, alpha=0.01, random_state=42)
```

#### Increase Bootstrap Iterations

```python
# For higher precision (takes longer)
ci_boot = ci_mean_bootstrap(bp, n_boot=10000, random_state=42)
```

#### Change Random Seed

```python
# Use different seed for different random results
sim_rate, sim_data = simulate_disease(n_sim=1000, p=true_rate, random_state=123)
```

---

## 📁 Project Structure

```
health-study-analysis/
│
├── health_study_final_report.ipynb    # Main analysis (Jupyter Notebook)
├── health_study_dataset.csv           # Dataset (800+ observations)
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
│
└── .venv/                             # Virtual environment (optional)
```

### File Descriptions

| File | Description |
|------|-------------|
| `health_study_final_report.ipynb` | Complete statistical analysis with code, visualizations, and interpretations |
| `health_study_dataset.csv` | Health study data with variables: age, sex, height, weight, systolic_bp, cholesterol, smoker, disease |
| `README.md` | Project documentation |
| `requirements.txt` | List of Python packages needed to run the notebook |

---

## 📝 Assignment Requirements

This project fulfills the following course requirements:

### ✅ For Grade G (Pass)

- [x] **Descriptive statistics**: Mean, median, min, max for age, weight, height, systolic_bp, cholesterol
- [x] **3+ visualizations**: Histogram, boxplot, bar chart
- [x] **Simulation**: 1000 random samples using `numpy.random` with seed
- [x] **Confidence interval**: CI for mean systolic blood pressure
- [x] **Hypothesis test**: Testing if smokers have higher mean blood pressure

### ✅ For Grade VG (Pass with Distinction)

- [x] **Two CI methods**: Normal approximation AND bootstrap comparison
- [x] **Power simulation**: Estimated test power using bootstrap resampling
- [x] **Methodology justification**: Explanations in markdown with references to documentation
- [x] **Academic references**: Citations to statistical literature (Efron & Tibshirani, Cohen, etc.)

---

## 🎯 Results Summary

### Key Findings

| Analysis | Result | Interpretation |
|----------|--------|----------------|
| **Disease Prevalence** | ~10% | Approximately 1 in 10 individuals have the disease |
| **Simulated Prevalence** | ≈10% | Monte Carlo simulation confirms observed rate |
| **Mean Systolic BP** | ~145 mmHg | 95% CI: [143, 147] (both methods agree) |
| **Smokers vs Non-smokers** | p < 0.05 | Smokers have significantly higher BP |
| **Test Power** | ~0.85 | High power - test reliably detects true differences |

### Statistical Methods Used

1. **Descriptive Statistics**: `pandas.DataFrame.agg()`
2. **Confidence Intervals**: 
   - Normal approximation using z-scores
   - Bootstrap percentile method (5000 iterations)
3. **Hypothesis Testing**: Welch's t-test (unequal variances)
4. **Power Analysis**: Bootstrap resampling (500 iterations)

---

## 🔬 Methodology

### Confidence Interval Methods

#### 1. Normal Approximation
- **Assumption**: Sampling distribution of the mean is approximately normal (CLT)
- **Formula**: `mean ± z * (std / √n)`
- **Pros**: Fast, theoretical foundation
- **Cons**: Requires normality assumption

#### 2. Bootstrap Method
- **Procedure**: Resample with replacement 5000 times
- **Interval**: 2.5th and 97.5th percentiles of bootstrap means
- **Pros**: No distributional assumptions, robust to outliers
- **Cons**: Computationally intensive

### Hypothesis Test

**Null hypothesis (H₀)**: Smokers and non-smokers have equal mean systolic BP  
**Alternative (H₁)**: Smokers have higher mean systolic BP (one-sided)

**Test**: Welch's t-test (accounts for unequal variances)  
**Decision rule**: Reject H₀ if p-value < 0.05

### Power Analysis

**Purpose**: Estimate probability of detecting a true effect

**Method**: Bootstrap simulation
1. Resample from observed smoker and non-smoker groups
2. Run t-test on each resample
3. Calculate proportion of significant results

**Interpretation**: Power ≈ 0.85 means we have an 85% chance of detecting a real difference if it exists

---

## 📚 References

1. Efron, B., & Tibshirani, R. J. (1994). *An Introduction to the Bootstrap*. Chapman & Hall.
2. Mooney, C. Z., & Duval, R. D. (1993). *Bootstrapping: A Nonparametric Approach to Statistical Inference*. Sage.
3. Student. (1908). The probable error of a mean. *Biometrika*, 6(1), 1–25.
4. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.
5. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.
6. Altman, D. G., & Bland, J. M. (1995). Statistics notes: The normal distribution. *BMJ*, 310, 298.
7. Freedman, D., Pisani, R., & Purves, R. (2007). *Statistics* (4th ed.). W. W. Norton & Company.

---

## 🛠️ Technical Details

### Python Version

```python
Python 3.13.7
```

### Dependencies

```
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
jupyter>=1.0.0
```

### Code Quality Features

- ✅ **Type hints** for function parameters and return values
- ✅ **Docstrings** for all functions
- ✅ **Modular design** with reusable utility functions
- ✅ **Reproducible** results using fixed random seeds
- ✅ **DRY principle** - minimal code repetition

---

## 🐛 Troubleshooting

### Common Issues

#### `ModuleNotFoundError: No module named 'scipy'`

**Solution:**
```bash
pip install scipy
```

#### `FileNotFoundError: 'health_study_dataset.csv'`

**Solution:** Make sure `health_study_dataset.csv` is in the same directory as the notebook

#### Matplotlib style warning

**Solution:** Update the style line in cell 1:
```python
plt.style.use('seaborn-v0_8-darkgrid')  # or 'default'
```

---

## 💡 Future Improvements

- [ ] Add regression analysis (linear model for BP prediction)
- [ ] Include multivariate analysis (multiple predictors)
- [ ] Add interactive visualizations with Plotly
- [ ] Implement cross-validation for model assessment
- [ ] Create automated report generation

---

## 📧 Contact

**Author**: [Your Name]  
**Email**: your.email@example.com  
**Course**: Statistical Methods / Data Analysis  
**Institution**: [Your University]  
**Year**: 2025

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🌟 Acknowledgments

- Thanks to the course instructors for providing the dataset and assignment guidelines
- Bootstrap methodology based on Efron & Tibshirani (1994)
- Statistical test implementations using SciPy library

---

**⭐ If you found this project helpful, please give it a star!**

---

*Last updated: January 2025*



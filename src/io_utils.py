import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)

def save_results(df, path):
    df.to_csv(path, index=False)

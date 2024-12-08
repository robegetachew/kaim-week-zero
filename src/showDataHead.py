import pandas as pd
import os

base_dir = os.path.dirname(__file__)  # Directory of the current script
beninFile = os.path.join(base_dir, '..', 'data', 'benin-malanville.csv')
sierraFile = os.path.join(base_dir, '..', 'data', 'sierraleone-bumbuna.csv')
togoFile = os.path.join(base_dir, '..', 'data', 'togo-dapaong_qc.csv')

def readData(city):
    if city == 'benin':
        return pd.read_csv(beninFile)
    elif city == 'sierra':
        return pd.read_csv(sierraFile)
    elif city == 'togo':
        return pd.read_csv(togoFile)
    else:
        raise ValueError("City not found")

def stats(city):
    data = readData(city)
    return data.describe()
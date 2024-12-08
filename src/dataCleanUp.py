import pandas as pd
import os

base_dir = os.path.dirname(__file__)  # Directory of the current script
beninFile = os.path.join(base_dir, '..', 'data', 'benin-malanville.csv')
sierraFile = os.path.join(base_dir, '..', 'data', 'sierraleone-bumbuna.csv')
togoFile = os.path.join(base_dir, '..', 'data', 'togo-dapaong_qc.csv')

benin = pd.read_csv(beninFile)
sierra = pd.read_csv(sierraFile)
togo = pd.read_csv(togoFile)

def removeComments(city):
    if city == 'benin':
        return benin.drop(['Comments'], axis=1)
    elif city == 'sierra':
        return sierra.drop(['Comments'], axis=1)
    elif city == 'togo':
        return togo.drop(['Comments'], axis=1)
    else:
        raise ValueError("City not found")
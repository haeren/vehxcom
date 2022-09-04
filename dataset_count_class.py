import pandas as pd
import numpy as np

dataset_path = 'dataset.csv'
dataset = pd.read_csv(dataset_path)

y = dataset.iloc[:, -1:].values

count_3gpp = (y == 0).sum()
count_ieee = (y == 1).sum()

print('3GPP:', count_3gpp, 'instance(s)')
print('IEEE:', count_ieee, 'instance(s)')
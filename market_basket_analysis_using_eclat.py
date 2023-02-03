# -*- coding: utf-8 -*-
"""Market_Basket_Analysis_using_ECLAT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17nrZoLNS7ol_mh7MnFHStzcxgoBPSdMY

### Importing the basic libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""### Load Dataset from Local Directory"""

from google.colab import files
uploaded = files.upload()

"""### Importing the dataset"""

dataset = pd.read_csv('dataset1.csv')
print(dataset.shape)
print(dataset.head(5))

"""### Data Pre-Processing"""

transactions = []
for i in range(0, 7500):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
transactions

"""### Training APRIORI"""

!pip install apyori
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

"""### Result"""

results = list(rules)
results

"""### Results in Dataframe"""

lhs         = [tuple(result[2][0][0])[0] for result in results]
rhs         = [tuple(result[2][0][1])[0] for result in results]
supports    = [result[1] for result in results]
confidences = [result[2][0][2] for result in results]
resultsinDataFrame = pd.DataFrame(zip(lhs, rhs, supports, confidences), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence'])
resultsinDataFrame

resultsinDataFrame.nlargest(n = 15, columns = 'Support')


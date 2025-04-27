import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

file_path = 'train.csv'
data = pd.read_csv(file_path)

print(data.head())

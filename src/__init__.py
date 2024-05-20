import numpy as np #
import pandas as pd #
import seaborn as sns #
import plotly.express as px  # Gera um gráfico dinâmico
import matplotlib.pyplot as plt # 

baseCredit = pd.read_csv('data/credit_risk_dataset.csv', engine='python')
print(baseCredit)
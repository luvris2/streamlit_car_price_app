import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# sns.heatmap(data= , annot=True, fmt='.2f')

# scaler_y = MinMaxScaler()
# y = scaler_y.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=50)

# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
# y_pred = regressor.predict(X_test)
# scaler_y.inverse_transform(y_pred)
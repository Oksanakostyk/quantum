import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('D:\python\Quantum internship\internship_train.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 53].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

data = pd.read_csv('D:\python\Quantum internship\internship_hidden_test.csv')

X_target= data.values
target_pred=model.predict(X_target)

df2 = pd.DataFrame(data)
df2["53"] = target_pred
export_csv=df2.to_csv(r'D:\python\Quantum internship\internship_prediction.csv')


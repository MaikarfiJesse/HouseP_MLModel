import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import __version__ as sklearn_version
import joblib

df = pd.read_csv(
    r'_YOUR_LOCATION_\house_data.csv')

columns = ['bedrooms', 'bathrooms', 'floors', 'yr_built', 'price']
df = df[columns]

X = df.iloc[:, 0:4]
y = df.iloc[:, 4:]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

model_filename = 'model.pkl'
joblib.dump(lr, model_filename)

version_filename = 'model_version.pkl'
with open(version_filename, 'wb') as f:
    joblib.dump(sklearn_version, f)

import pandas as pd
import numpy as np
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("Salary_Data.csv")

X = dataset["YearsExperience"].values.reshape(-1,1)
y = dataset["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

dump(model, "salary.pk1")

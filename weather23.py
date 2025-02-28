# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RKwfalkvNlMJXuf3IQt_5wr7utXf4bNt
"""

!pip install pandas scikit-learn matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

data = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'Temperature (C)': [10, 12, 15, 14, 16],
    'Humidity (%)': [60, 65, 70, 68, 72],
    'Wind Speed (km/h)': [15, 18, 20, 16, 22],
    'Pressure (millibars)': [1012, 1010, 1008, 1009, 1011],
    'Wind Bearing (degrees)': [180, 190, 200, 195, 205],
    'Visibility (km)': [10, 12, 15, 14, 16]
}

weather_df = pd.DataFrame(data)
weather_df.to_csv('weather_data.csv', index=False)

def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in the CSV:", df.columns)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

    df = df.dropna()  # Drop rows with missing values
    return df

def perform_eda(df):
    if df is None:
        print("Error: DataFrame is None. Cannot perform EDA.")
        return

    print(df.head())
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Temperature (C)'], bins=30, kde=True)
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (C)')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()

def train_model(df):
    X = df[['Humidity (%)', 'Pressure (millibars)', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)']]
    y = df['Temperature (C)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open('temperature_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

def load_model():
    with open('temperature_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_temperature(model, input_data):
    return model.predict([input_data])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in the CSV:", df.columns)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

    df = df.dropna()  # Drop rows with missing values
    return df

def perform_eda(df):
    if df is None:
        print("Error: DataFrame is None. Cannot perform EDA.")
        return

    print(df.head())
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Temperature (C)'], bins=30, kde=True)
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (C)')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))

    plt.title('Correlation Heatmap')
    plt.show()

def train_model(df):
    X = df[['Humidity (%)', 'Pressure (millibars)', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)']]
    y = df['Temperature (C)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open('temperature_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

def load_model():
    if not os.path.exists('temperature_model.pkl'):
        print("Error: Model file not found.")
        return None

    with open('temperature_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_temperature(model, input_data):
    if model is None:
        print("Error: Model is not loaded. Cannot make predictions.")
        return None

    # Ensure input_data is a list of the correct length
    if len(input_data) != 5:
        print("Error: Input data must have 5 features.")
        return None

    return model.predict([input_data])

if __name__ == "__main__":
    df = load_and_clean_data('weather_data.csv')
    if df is not None:
        perform_eda(df)
        train_model(df)
        model = load_model()

        # Example input for prediction
        input_data = [65, 1010, 18, 190, 12]  # Example: [Humidity, Pressure, Wind Speed, Wind Bearing, Visibility]
        predicted_temp = predict_temperature(model, input_data)

        if predicted_temp is not None:
            print(f"Predicted Temperature: {predicted_temp[0]} °C")
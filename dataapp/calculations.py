import pandas as pd
import os
from .GenAI import create_agent

def about_data(file):
    df = pd.read_csv(file)
    df = convert_categorical(df)
    rows, cols = df.shape
    nulls = df.isnull().sum().sum()
    duplicate = df.duplicated().sum()
    categorical = df.select_dtypes("O").shape[1]
    include = ["int32", "int64", "float32", "float64"]
    numerical = df.select_dtypes(include=include).shape[1]
    agent = create_agent(file)
    about = agent.run("What is this data about?")

    dic = {
        "Number of columns":cols,
        "Number of recoreds":rows,
        "Number of missing data":nulls,
        "duplicates":duplicate,
        "categorical feature":categorical,
        "numerical feature":numerical,
        "about":about
    }
    return dic


def convert_categorical(df):
    types = ["int32", "int64", "float32", "float64"]
    for cols in df.columns:
        if df[cols].dtype in types:
            uniue_value = df[cols].nunique()
            total_value = df[cols].count()
            percentage_of_unique_value = uniue_value/total_value
            if percentage_of_unique_value<0.08 and total_value<500:
                df[cols] = df[cols].astype("category")
            elif percentage_of_unique_value<0.05 and total_value>500:
                df[cols] = df[cols].astype("category")
    return df

def convert_datetime(df):
    for cols in  df.select_dtypes("O").columns:
        try:
            df[cols] = pd.to_datetime(df[cols])
        except ValueError:
                pass
    return df

def classify_data(file):
    df = pd.read_csv(file)
    df = convert_categorical(df)
    df = convert_datetime(df)
    types = ["int32", "int64", "float32", "float64"]
    numeric_data = df.select_dtypes(include=types)
    cat_data = df.select_dtypes("O")
    date_time = df.select_dtypes(include='datetime64[ns]')
    return numeric_data, cat_data, date_time


def descriptive_statistics(file):
    df = pd.read_csv(file)
    statistics = df.describe().to_json()
    return statistics

def nulls(file):
    df = pd.read_csv(file)
    return df.isnull().sum().to_json()
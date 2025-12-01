import pandas as pd

def clean_data(df):
    df=df.dropna()
    df['OrderDate']=pd.to_datetime(df['OrderDate'])
    return df

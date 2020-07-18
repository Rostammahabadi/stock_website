"""Prepare data for Plotly Dash."""
import pandas as pd
import numpy as np


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv('data/ibm_intraday_data.csv', parse_dates=['timestamp'])
    df.set_index(['timestamp'])
    #df['timestamp'] = df['timestamp'].dt.date
    return df

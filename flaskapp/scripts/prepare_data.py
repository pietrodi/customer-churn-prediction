import pandas as pd
import numpy as np

"""
This script is used to prepare training and prediction data for the model.
"""

def prepare_data(df):
    """
    Returns prepared dataframe for training or prediction
    on the model.

    Args:
        df: the dataframe to prepare

    Returns:
        The prepared dataframe for the model
    """
    df['HasNoBalance'] = df['Balance'] == 0

    df['Balance'] = np.log1p(df['Balance'])
    df['Age'] = np.log1p(df['Age'])

    return df
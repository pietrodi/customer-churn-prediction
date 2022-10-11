import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from xgboost import XGBClassifier

from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import make_pipeline

from prepare_data import prepare_data

"""
This script is used for training the model used for prediction.
"""

""" The training dataframe path. """
DATA_PATH = '../data/customer-data.csv'
""" The best params for the model. """
BEST_PARAMS = {'learning_rate': 0.15, 'max_depth': 4, 'n_estimators': 50}

def load_data(path):
    """
    Loads the training dataframe.

    Args:
        path: The path of the traning dataframe

    Returns:
        The training dataframe
    """
    df = pd.read_csv(path)
    return df

def train_model(df, params):
    """
    Returns a trained model.

    Args:
        df: The training dataframe of the model
        params: The parameters of the model

    Returns:
        The trained model
    """
    #Feature Engineering
    df = prepare_data(df)
    y = df['Exited'].values

    numerical_features = ['Balance', 'CreditScore', 'Age']
    categorical_features = ['Geography', 'Gender', 'Tenure', 'NumOfProducts', 
                            'IsActiveMember', 'HasNoBalance']
    numerical_transformer = Pipeline(steps = [('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps = [('onehot', OneHotEncoder(drop = 'if_binary', handle_unknown = 'ignore', sparse = False))])

    # Training
    model = make_pipeline (
        RandomUnderSampler(),
        ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)],
        ),
        XGBClassifier(**params)
    )

    model.fit(df, y)
    return model

def save_model(model):
    """
    Saves a model.

    Args:
        model: The model to be saved
    """
    pickle.dump(model, open('model.pkl', 'wb'))

def main():
    data = load_data(DATA_PATH)
    model = train_model(data, BEST_PARAMS)
    save_model(model)

if __name__ == '__main__':
    main()
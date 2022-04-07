import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ColumnRename(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.new_columns = X.columns.str.replace(' ', '_').str.lower()
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X.columns = self.new_columns
        return X

    def get_feature_names_out(self, feature_names_from_previous_step):
        return self.new_columns


class MatrixToDataFrame(BaseEstimator, TransformerMixin):
    def __init__(self, transformer):
        self.transformer = transformer

    def fit(self, X, y=None):
        self.cols = self.transformer.get_feature_names_out()
        return self

    def transform(self, X, y=None):
        df = pd.DataFrame(X, columns=self.cols)
        df = df.apply(pd.to_numeric, errors='ignore')
        return df

    def get_feature_names_out(self, feature_names_from_previous_step):
        return self.cols



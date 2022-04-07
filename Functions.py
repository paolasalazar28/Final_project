# python
from functools import partial

# basics
import numpy as np
import pandas as pd
import scipy.stats as stats

# graphing
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# preprocessing
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, MinMaxScaler

# model selection
from sklearn.model_selection import train_test_split, KFold, GridSearchCV, cross_val_score

from sklearn.metrics import (r2_score, mean_squared_error, accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, roc_curve, precision_recall_curve, make_scorer,confusion_matrix,classification_report
)

# models
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, LogisticRegression

from sklearn import tree

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

def get_final_data():
    X_train_raw, X_test_raw, y_train, y_test = get_raw_data()

    cols = ['avg_dist', 'avg_rating_by_driver', 'avg_rating_of_driver', 'avg_surge','city', 'phone', 'surge_pct','trips_in_first_30_days', 'luxury_car_user', 'weekday_pct']
    clean = Cleaner(cols)
    clean.fit(X_train_raw_col_fix)
    X_train = clean.transform(X_train_raw_col_fix)
    X_test = clean.transform(X_test_raw_col_fix)
    return X_train, X_test, y_train, y_test

def get_raw_data():
    colsName=['festivo', 'mes', 'diaSemana', 'hora', 'mda', 'mtr', 'mda7', 'mtr7',
       'ypast7', 'festivo7', 'mda14', 'mtr14', 'ypast14', 'festivo14', 'mda52',
       'mtr52', 'ypast52', 'festivo52', 'ypast3avg', 'eolica', 'fotovol',
       'demanda', 'temperatura', 'hsc', 'DART (MXN/MWh)', 'DARTbin', 'Year',
       'Day']
    df_train = pd.read_csv('data/BD.csv');
    
    df_train['fecha']=pd.to_datetime(df_train['fecha']);
    df_train['fecha_h']=pd.to_datetime(df_train['fecha_h']);

    df_train['temperatura']= df_train['temperatura'].replace("#Â¡REF!", np.NaN)
    df_train['temperatura']=pd.to_numeric(df_train['temperatura'])
    
    df_train['DART (MXN/MWh)']=df_train['mtr']-df_train['mda']
    df_train['DARTbin']=df_train['mtr']>=df_train['mda']
    df_train['DARTbin']=df_train['DARTbin'].map({True:1,False:0})
    
    df_train['Year']=pd.DatetimeIndex(df_train['fecha']).year
    df_train['Day']=pd.DatetimeIndex(df_train['fecha']).day
    
    df_train=df_train.dropna()
    
    DF_temp_A = df_train[df_train['fecha'] < '2021-02-13']
    DF_temp_B = df_train[df_train['fecha'] >= '2021-02-22']
    
    df_train=pd.concat([DF_temp_A,DF_temp_B],axis=0)


    y_train = df_train.DARTbin
  
        
    
    return df_train, y_train





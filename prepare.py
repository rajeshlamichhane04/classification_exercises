import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import acquire
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

#iris database
#clean function
def clean_iris(df):
    df = df.drop(columns = ["species_id", "measurement_id"])
    df = df.rename(columns = {"species_name":"species"})
    dummy_df = pd.get_dummies(df[["species"]],drop_first=True)
    df = pd.concat([df,dummy_df], axis = 1)
    
    return df

#split funtion
def split_iris_data():
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)
    train,validate = train_test_split(train,test_size = .25, random_state = 123, stratify = train.species )
    return train,validate,test

#prep function
def prep_iris_data(df):
    df = clean_iris(df)
    train,validate,test=split_iris_data(df)
    return train,validate,test


#titanic database

def clean_data(df):
    df=df.drop(columns = ["embarked","class"])
    df=df.drop(columns = ["age","deck"])
    df.embark_town = df.embark_town.fillna(value = "Southampton")
    dummy_df =pd.get_dummies(df[['sex','embark_town']], drop_first = True)
    df = pd.concat([df,dummy_df], axis = 1)
    df = df.drop(columns = ["sex","embark_town"])

    return df

def split_data(df):
    train,test = train_test_split(df,test_size = .2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train,test_size = 0.25, random_state = 123, stratify= train.survived)
    return train,validate,test

def prep_titanic_data(df):
    df = clean_data(df)
    train,validate,test=split_data(df)
    return train,validate,test
    
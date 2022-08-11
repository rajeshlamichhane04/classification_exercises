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
def split_iris_data(df):
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)
    train,validate = train_test_split(train,test_size = .25, random_state = 123, stratify = train.species )
    return train,validate,test

#prep function
def prep_iris_data(df):
    df = clean_iris(df)
    train,validate,test=split_iris_data(df)
    return train,validate,test







#titanic database

def clean_data_titanic(df):
    df=df.drop(columns = ["embarked","class"])
    df=df.drop(columns = ["age","deck"])
    df.embark_town = df.embark_town.fillna(value = "Southampton")
    dummy_df =pd.get_dummies(df[['sex','embark_town']], drop_first = True)
    df = pd.concat([df,dummy_df], axis = 1)
    df = df.drop(columns = ["sex","embark_town"])

    return df

def split_data_titanic(df):
    train,test = train_test_split(df,test_size = .2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train,test_size = 0.25, random_state = 123, stratify= train.survived)
    return train,validate,test

def prep_titanic_data(df):
    df = clean_data_titanic(df)
    train,validate,test=split_data_titanic(df)
    return train,validate,test










    
#telco data
#clean
def clean_data_telco(telco):
    drop_columns = ["contract_type_id","internet_service_type_id","payment_type_id"]
    telco = telco.drop(columns = drop_columns)

    dummy_df = pd.get_dummies(telco[['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','tech_support',
                                 'streaming_movies','paperless_billing','churn','payment_type', 'internet_service_type',
                                 'contract_type','device_protection','streaming_tv']], dummy_na = False, drop_first = True)
    
    telco = pd.concat([telco,dummy_df], axis = 1)
    
    columns = ['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','tech_support',
            'streaming_movies','paperless_billing','payment_type', 'internet_service_type',
             'contract_type', 'device_protection','streaming_tv']

    telco = telco.drop(columns = columns)
     
    return telco
#split
def my_train_test_split_telco(telco):

     train, test = train_test_split(telco, test_size=.2, random_state=123, stratify=telco.churn)
     train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.churn)

     return train, validate, test 

#make prep function now
def prep_get_telco_data(telco):
    telco = clean_data_telco(telco)
    train, validate, test = my_train_test_split_telco(telco)
    return train,validate,test





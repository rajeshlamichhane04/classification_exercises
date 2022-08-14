import numpy as np
import pandas as pd
import env
import os

#get url
def conn(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. Obtain your data from the Codeup Data Science Database.

#get the sql querry set up
def new_titanic_data():
    sql_query = "SELECT * FROM passengers"
    df = pd.read_sql(sql_query,conn('titanic_db'))
    return df
# this funtion either write and then read the csv file or pull it 
#from sql query first then write, read that csv

def get_titanic_data():
    
    if os.path.isfile("titanic_df.csv"):
        #open that csv 
        df = pd.read_csv("titanic_df.csv", index_col = 0)
    else:
        #if there is csv, use sql qerry function from above
        df = new_titanic_data()
        #change the df to csv
        df.to_csv("titanic_df.csv")
    return df

  
# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

#this function will read iris database 
def get_iris_data():
    #look for iris.csv file in the repo folder
    filename = 'iris.csv'
    #if it finds in the repo folder, return that back to function
    if os.path.isfile(filename):
        df= pd.read_csv(filename,index_col=0 )
        return df
    #if there is no such file, pull it from sql db as a dataframe
    else:
        df = pd.read_sql('SELECT * FROM measurements JOIN species USING(species_id);', conn('iris_db'))
        #cache it out into cvs from df
        df.to_csv(filename)
        return df


#3.Make a function named get_telco_data that returns the data from the telco_churn database in SQL. In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains all the contract, payment, and internet service options. Obtain your data from the Codeup Data Science Database.


#read get_telco_data 
def get_telco_data():
    #take a glace of that csv file name if present locally
    #if present, return it back
    filename = 'telco.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col = 0)
        return df
    #run sql query if not present locally
    else:
        query = '''
            SELECT * FROM customers
            JOIN contract_types USING (contract_type_id)
            JOIN payment_types USING (payment_type_id)
            JOIN internet_service_types USING (internet_service_type_id);  
        '''
        df = pd.read_sql(query, conn('telco_churn')) 
        #convert df to csv
        df.to_csv(filename)
        return df







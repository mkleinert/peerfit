# -*- coding: utf-8 -*-

#import sqlite3
import pandas as pd
import glob
import os
import sys
from etl_sql import etl_sql
from etl_queries import etl_upsert_queries as queries
import json



def stg_data(num_cols,stg_table):
    #loop through and load load all files matching pattern to pandas dataframe
    max_cols = int(num_cols)
    path = r'..\data'                   
    all_files = glob.glob(os.path.join(path,file_pattern )) 
    
    df_from_each_file = (pd.read_csv(f,sep=',',usecols=range(max_cols)) for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
    concatenated_df.to_sql(stg_table+'_stg',con=sql.engine, if_exists='replace')
    
    return concatenated_df

def clean_data(file_df, date_cols,null_cols):
    #try to clean up some bad data.  For dates convert to datetime and removes 
    #dates that are bad.  For some columns drop them if null is not useful with 
    #data missing.  Long term better way would be to write it off in some log
    #for investigation or fixing.
    file_df[date_cols] = file_df[date_cols].apply(pd.to_datetime, errors='coerce')
    file_df = file_df.dropna(subset=null_cols)
    
    return file_df

def insert_data(query):
        sql.upsert_exec(query)
   
if __name__ == "__main__":
        config_sel = sys.argv[1]
        
        with open('config.json', 'r') as f:
            config = json.load(f)
        # set the configuration values    
        file_pattern = config[config_sel]['file_pattern']
        table_dict = config[config_sel]['table_dict']
        dt_cols = config[config_sel]['date_cols']
        null_cols = config[config_sel]['check_nulls']
        col_cnt = config[config_sel]['col_cnt']
        sql = etl_sql()
        #load the files
        file_df = stg_data(col_cnt,config_sel)
        
        sql = etl_sql()
        #clean the data        
        cleaned_df = clean_data(file_df,dt_cols,null_cols)
       # load the tables approriate for that configuration
        for table, columns in table_dict.items():
            upsert_query = queries[table]
            insert_data(upsert_query)

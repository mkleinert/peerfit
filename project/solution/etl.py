# -*- coding: utf-8 -*-

#import sqlite3
import pandas as pd
import glob
import os
import sys
from sqlalchemy import create_engine
import json

db_uri = 'sqlite:///peerfit.db'
engine = create_engine(db_uri)

def file_loader(num_cols):
    #loop through and load load all files matching pattern to pandas dataframe
    max_cols = int(num_cols)
    path = r'..\data'                   
    all_files = glob.glob(os.path.join(path,file_pattern )) 
    
    df_from_each_file = (pd.read_csv(f,sep=',',usecols=range(max_cols)) for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
    return concatenated_df

def clean_data(file_df, date_cols,null_cols):
    #try to clean up some bad data.  For dates convert to datetime and removes 
    #dates that are bad.  For some columns drop them if null is not useful with 
    #data missing.  Long term better way would be to write it off in some log
    #for investigation or fixing.
    file_df[date_cols] = file_df[date_cols].apply(pd.to_datetime, errors='coerce')
    file_df = file_df.dropna(subset=null_cols)
    
    return file_df

def insert_data(df,table_name, col_list,query):
    #for the dimension style tables just do an upsert.  If is a fact style table
    #do the lookups and insert
    df.drop_duplicates(inplace=True)
    df.to_sql(name=table_name+'_temp', con=engine, if_exists = 'replace', index=False)
    insert_df = df.filter(col_list, axis=1)
    insert_df.drop_duplicates(inplace=True)

    if query != "":
        engine.execute(" ".join(query))
    else:
        insert_df.to_sql(name=table_name, con=engine, if_exists = 'append',index=False)
    
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
        
        #load the files
        file_df = file_loader(col_cnt)
        #clean the data        
        cleaned_df = clean_data(file_df,dt_cols,null_cols)
        #load the tables approriate for that configuration
        for table, columns in table_dict.items():
            del_query = config[config_sel][table+'_insert']
            insert_data(cleaned_df,table,columns,del_query)

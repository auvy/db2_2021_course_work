import os

import sys
import pandas as pd
from pymongo import MongoClient
import json

def get_collection(dbname, coll_name):
    mng_client = MongoClient('localhost', 27017)
    mng_db = mng_client[dbname]

    if coll_name not in mng_db.list_collection_names():
        mng_db.create_collection(coll_name)

    return mng_db[coll_name]

def import_csv_to_db(coll_name, file_res, dbname):
    db_cm = get_collection(dbname, coll_name)
    
    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

def csv_to_df(file_res):
    return pd.read_csv(file_res)

def get_dataframe(dbname, coll_name):
    col = get_collection(dbname, coll_name)
    return pd.DataFrame(list(col.find()))

def get_columns(dbname, coll_name):
    col = get_dataframe(dbname, coll_name)
    return col.columns.tolist()



def get_columns_as_dict(dbname, coll_name):
    col = get_dataframe(dbname, coll_name)
    return dict(col.dtypes)
    


def import_df_to_db(df, dbname, coll_name):
    db_cm = get_collection(dbname, coll_name)
    data_json = json.loads(df.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)
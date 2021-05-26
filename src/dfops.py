import csv
import pandas as pd

import sys
import json

def filter_cols(df, columns):
    df.drop(columns, axis=1, inplace=True)

def sort_rows(df, column):
    df.sort_values(by=[column], ascending=False, inplace = True)

def drop_dupl(df):
    df.drop_duplicates(subset ="Name", keep = False, inplace = True)  

def trim_rows(df, top):
    df.drop_duplicates(subset ="Name",
                     keep = False, inplace = True)
    n = len(df.index) - top
    df.drop(df.tail(n).index, inplace = True)

def format_cols(df, cols, platform):
    df.rename(columns=cols, inplace=True)
    df['Platform'] = platform
    # df["Rating Count"] = df["Rating Count"].apply(lambda x: int(x) )

def drop_empty(df, cols):
    df.dropna(subset = cols, inplace=True)

# def drop_invalid(df, cols):
#     df.dropna(subset = cols, inplace=True)

def to_int(df, col):
    df[col] = df[col].apply(lambda x: int(x) )

def genre_rename(df, genres):
    df.loc[df['Category'].isin(genres), 'Category'] = 'Games'


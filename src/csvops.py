import csv
import pandas as pd

import sys
import json


def filter_cols(input, output, columns):
    df = pd.read_csv(input)
    df.drop(columns, axis=1, inplace=True)
    df.to_csv(output, index=False)

def sort_rows(input, column, output):
    df = pd.read_csv(input)
    df = df.sort_values(by=[column], ascending=False)
    df.to_csv(output, index=False)

def drop_dupl(input, output):
    df = pd.read_csv(input)
    df.drop_duplicates(subset ="Name", keep = False, inplace = True)  
    df.to_csv(output, index=False)

def trim_rows(input, output, top):
    df = pd.read_csv(input)
    df.drop_duplicates(subset ="Name",
                     keep = False, inplace = True)
    n = len(df.index) - top
    df.drop(df.tail(n).index, inplace = True)
    df.to_csv(output, index=False)

def format_cols(input, output, cols, platform):
    df = pd.read_csv(input)
    df.rename(columns=cols, inplace=True)
    df['Platform'] = platform
    # df["Rating Count"] = df["Rating Count"].apply(lambda x: int(x) )
    df.to_csv(output, index=False)

def drop_empty(input, cols, output):
    df = pd.read_csv(input)
    df.dropna(subset = cols, inplace=True)
    df.to_csv(output, index=False)

def to_int(input, col, output):
    df = pd.read_csv(input)
    df[col] = df[col].apply(lambda x: int(x) )
    df.to_csv(output, index=False)

def genre_rename(input, genres, output):
    df = pd.read_csv(input)
    df.loc[df['Category'].isin(genres), 'Category'] = 'Games'
    
    # df = df.replace(genres, 'Games')
    print(df['Category'].unique())
    df.to_csv(output, index=False)



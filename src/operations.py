import pandas as pd
import numpy as np
from scipy.stats import stats
from sklearn.linear_model import LinearRegression

import statistics

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import database as db

#sum of all downloads per genre
def genre_popularity(collection):
    df = db.get_dataframe('db2cw', collection)
    genres = df['Category'].unique()
    votes = []
    for one in genres:
        votes.append(df.loc[df['Category'] == one, 'Rating Count'].sum())

    # fig = plt.figure(figsize=(12,4))
    plt.barh(genres, votes)
    plt.title(f'Genre Popularity ({collection})')
    plt.xlabel('Rating Count')
    plt.ylabel('Genres')
    # plt.setp(xlabel.get_xticklabels(), rotation=30, horizontalalignment='right')]
    plt.subplots_adjust(left=0.276)
    plt.savefig(f'graph/popularity_{collection}.png')
    plt.show()


def genre_popularity_2(collection):
    df = db.get_dataframe('db2cw', collection)
    genres = df['Category'].unique()
    votes = []
    for one in genres:
        votes.append(df.loc[df['Category'] == one, 'Rating Count'].mean())

    # fig = plt.figure(figsize=(12,4))
    plt.barh(genres, votes)
    plt.title(f'Genre Popularity ({collection})')
    plt.xlabel('Rating Count')
    plt.ylabel('Genres')
    # plt.setp(xlabel.get_xticklabels(), rotation=30, horizontalalignment='right')]
    plt.subplots_adjust(left=0.276)
    plt.savefig(f'graph/popularity_{collection}.png')
    plt.show()

def genre_max_download(collection):
    df = db.get_dataframe('db2cw', collection)
    genres = df['Category'].unique()
    votes = []
    for one in genres:
        votes.append(df.loc[df['Category'] == one, 'Rating Count'].max())

    # fig = plt.figure(figsize=(12,4))
    plt.barh(genres, votes)
    plt.title(f'Genre Max Count ({collection})')
    plt.xlabel('Rating Count')
    plt.ylabel('Genres')
    # plt.setp(xlabel.get_xticklabels(), rotation=30, horizontalalignment='right')]
    plt.subplots_adjust(left=0.276)
    plt.savefig(f'graph/max_{collection}.png')
    plt.show()


#amount of apps by genre
def genre_saturation(collection):
    df = db.get_dataframe('db2cw', collection)
    genres = df['Category'].unique()
    amount = []
    for one in genres:
        amount.append(len(df.loc[df['Category'] == one]))

    all = list(zip(genres, amount))
    all.sort(key=lambda x: x[1], reverse=True)
    genres, amount = zip(*all)
    # fig1, ax1 = plt.subplots()
    plt.pie(amount, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    labels = [f'{g} ({a})' for g, a in all]
    plt.title(f'Genre Saturation ({collection})')
    plt.legend(labels, loc='upper left', fontsize = 8)
    plt.subplots_adjust(left=0, right=1, top=0.95)
    plt.savefig(f'graph/saturation_{collection}.png')
    plt.show()

#mean of rating by genre
def genre_love(collection):
    df = db.get_dataframe('db2cw', collection)
    genres = df['Category'].unique()
    votes = []
    for one in genres:
        votes.append(df.loc[df['Category'] == one, 'Rating'].mean())

    plt.barh(genres, votes)
    plt.title(f'Genre Adoration ({collection})')
    # plt.title('Genres vs Rating Mean')
    plt.ylabel('Genres')
    plt.xlabel('Rating Mean')
    plt.subplots_adjust(left=0.276)
    plt.savefig(f'graph/love_{collection}.png')
    plt.show()    

def regression(collection, column, value):
    df = db.get_dataframe('db2cw', collection)
    x = np.array(df[value]).reshape(-1, 1)
    y = np.array(df[column]).reshape(-1, 1)
    model = linear_model(x, y)
    x_plot = np.linspace(0, max(x)).reshape(-1, 1)
    y_pred = model.predict(x_plot)

    plt.ylabel(column)
    plt.xlabel(value)
    plt.title(f'Regression ({collection})')
    plt.scatter(x, y, s=2)
    plt.plot(x_plot, y_pred, color='red')
    plt.savefig(f'graph/regression_{collection}.png')
    plt.show()

def get_mode(collection, dbname, column):
    df = db.get_dataframe(dbname, collection)
    df = df[column].to_list()
    print(f'{column} mode = {statistics.mode(df)}')



def categorical_regression(collection, column, value):
    df = db.get_dataframe('db2cw', collection)
    x = np.array(df[value]).reshape(-1, 1)
    y = np.array(df[column]).reshape(-1, 1)
    model = linear_model(x, y)
    x_plot = np.linspace(0, max(x)).reshape(-1, 1)
    y_pred = model.predict(x_plot)

    plt.ylabel(column)
    plt.xlabel(value)
    plt.scatter(x, y, s=2)
    plt.plot(x_plot, y_pred, color='red')
    plt.savefig(f'graph/creg_{collection}.png')
    plt.show()


def popularity_prediction(props, collection, dbname):
    df = db.get_dataframe(dbname, collection)
    x = df[(list(props.keys()))]
    x = pd.get_dummies(data=x, drop_first=True)
    y = np.array(df['Rating Count']).reshape(-1, 1)
    model = linear_model(x, y)

    paint = np.array(list(props.values())).reshape(-1, 1)
    print(paint)

    amount = model.predict(np.array(list(props.values())).reshape(-1, 1))[0][0]
    print(f'Predicted popularity = {int(amount)} ')

def correlation(collection, dbname):
    df = db.get_dataframe(dbname, collection)
    map = df.corr()
    sns.heatmap(map)
    plt.savefig(f'graph/correlation_{collection}.png')
    plt.show()


def linear_model(x, y):
    model = LinearRegression()
    model.fit(x, y)
    return model
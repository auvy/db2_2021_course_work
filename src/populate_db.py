import csv

import pandas as pd

import csvops as csvops
import dfops as dfops

import database as dbops

import sys
import pandas as pd
import pymongo
import json

src_folder = 'csvsrc/'
res_folder = 'csvsres/'
gsrc = 'google2.csv'
gres = 'googleres.csv'
asrc = 'appstore763kk.csv'
ares = 'appleres.csv'

ginput = src_folder + gsrc
goutput = res_folder + gres
ainput = src_folder + asrc
aoutput = res_folder + ares

apple_rename = {'Title': 'Name', 'Total_Number_of_Ratings': 'Rating Count', 'Total_Average_Rating': 'Rating', 'Primary_Genre': 'Category', 'Price_USD': 'Price', 'Age_Rating': 'Age Rating'}

apple_drop = ['_id', 'IOS_App_Id', 'Developer_Name', 'Developer_IOS_Id', 'IOS_Store_Url', 'Seller_Official_Website', 'Average_Rating_For_Version', 'Number_of_Ratings_For_Version', 'Original_Release_Date', 'Current_Version_Release_Date', 'All_Genres', 'Languages', 'Description']

google_drop = ['App Id','Installs', 'Minimum Installs', 'Maximum Installs', 'Free', 'Currency', 'Size',  'Minimum Android', 'Developer Id', 'Developer Website', 'Developer Email', 'Released', 'Last Updated', 'Privacy Policy', 'Ad Supported', 'In App Purchases', 'Editors Choice']

google_rename = {'App Name': 'Name', 'Content Rating': 'Age Rating'}

google_genre_games = {
    'Category': 'Action', 
    'Category': 'Adventure', 
    'Category': 'Arcade', 
    'Category': 'Board', 
    'Category': 'Card', 
    'Category': 'Casino', 
    'Category': 'Dice', 
    'Category': 'Educational', 
    'Category': 'Music', 
    'Category': 'Puzzle', 
    'Category': 'Racing', 
    'Category': 'Role Playing', 
    'Category': 'Simulation', 
    'Category': 'Strategy', 
    'Category': 'Trivia', 
    'Category': 'Word', 
    'Category': 'Casual'}


google_genre_games2 = {'Action',
'Adventure','Arcade','Board','Card','Casino','Dice','Educational','Music','Puzzle','Racing','Role Playing','Simulation','Strategy','Trivia','Word', 'Casual', 'Sports'}

google_content_rating = ['Everyone' 'Teen' 'Mature 17+' 'Everyone 10+']

apple_content_rating = ['17+' '12+' '4+' '9+']


def repopulate():
    csvops.filter_cols(ginput, goutput, google_drop)
    csvops.format_cols(goutput, goutput, google_rename, 'Android')
    csvops.genre_rename(goutput, google_genre_games2, goutput)
    csvops.drop_empty(goutput, ["Rating Count"], goutput)
    csvops.sort_rows(goutput, 'Rating Count', goutput)
    csvops.trim_rows(goutput, goutput, 1000)
    csvops.to_int(goutput, "Rating Count", goutput)
    dbops.import_csv_to_db('android', goutput, 'db2cw')

    csvops.filter_cols(ainput, aoutput, apple_drop)
    csvops.format_cols(aoutput, aoutput, apple_rename, 'iOS')
    csvops.drop_empty(aoutput, ["Rating Count"], aoutput)
    csvops.sort_rows(aoutput, 'Rating Count', aoutput)
    csvops.trim_rows(aoutput, aoutput, 1000)
    csvops.to_int(aoutput, "Rating Count", aoutput)
    dbops.import_csv_to_db('ios', aoutput, 'db2cw')



def repopulate_thru_df():
    df_android = dbops.csv_to_df(ginput)
    df_ios = dbops.csv_to_df(ainput)

    dfops.filter_cols(df_android, google_drop)
    dfops.format_cols(df_android, google_rename, 'Android')
    dfops.genre_rename(df_android, google_genre_games2)
    dfops.drop_empty(df_android, ["Rating Count"])
    dfops.sort_rows(df_android, 'Rating Count')
    dfops.trim_rows(df_android, 1000)
    dfops.to_int(df_android, "Rating Count")
    dbops.import_df_to_db(df_android, 'db2cw', 'android')

    dfops.filter_cols(df_ios, apple_drop)
    dfops.format_cols(df_ios, apple_rename, 'iOS')
    dfops.drop_empty(df_ios, ["Rating Count"])
    dfops.sort_rows(df_ios, 'Rating Count')
    dfops.trim_rows(df_ios, 1000)
    dfops.to_int(df_ios, "Rating Count")
    dbops.import_df_to_db(df_ios, 'db2cw', 'ios')

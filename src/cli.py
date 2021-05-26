from numpy import dtype
import operations as ds
import database as db
from populate_db import repopulate_thru_df

import ast



operations = ['Exit', 'Regression', 'Prediction', 'Genre Popularity', 'Genre Love', 'Genre Saturation', 'Correlation', 'Repopulate DBs']

def start_menu():
    print("\nWelcome! Choose operation:")
    print("1. Regression")
    print("2. Genre Popularity")
    print("3. Genre Love")
    print("4. Genre Saturation")
    print("5. Correlation")
    print("6. Mode")
    print("7. Repopulate DBs")
    print("8. Compare most downloaded among genre")
    print("0. Exit")
    return int(input("Enter the number of action: "))


def os_choice():
    while True:
        variable = int(input("Choose OS (1 for Android, 2 for iOS): "))
        if variable == 1:
            return 'android'
        elif variable == 2:
            return 'ios'
        else:
            print("Enter correct choice (num 1 or 2): ")

def regression():
    cols = ["Rating", "Rating Count", 'Price']

    for i in range(len(cols)):
        print(f'[{i}] {cols[i]}')
    while True:
        variable = int(input("Choose variable: "))        
        if variable < -1 or variable > len(cols) - 1:
            print('Enter correct choice: ')
        else:
            return cols[variable]

def choose_val_of_list(list):
    for i in range(len(list)):
        print(f'[{i}] {list[i]}')
    while True:
        variable = int(input("Choose variable: "))        
        if variable < -1 or variable > len(list) - 1:
            print('Enter correct choice: ')
        else:
            return list[variable]  


def prediction_choice(os):
    dict = db.get_columns_as_dict('db2cw', os)
    dict.pop('_id')
    dict.pop('Name')
    dict.pop('Platform')
    dict.pop('Rating Count')
    # dictVals = dict.copy()
    # print(dict)
    for key, value in dict.items():
        print((f'{key}'))
        val = ''
        if value == dtype('float64'):
            while type(val) != type(2.2):
                try:
                    val = ast.literal_eval(input("Enter the float: "))
                except Exception as err:
                    print("That's no float.")
        elif value == dtype('int64'):
            while type(val) != type(2):
                try:
                    val = ast.literal_eval(input("Enter the int: "))
                except Exception as err:
                    print("That's no int.") 
        else:
            val = input("Enter the string: ")
        dict[key] = val
    ds.popularity_prediction(dict, os, 'db2cw')


def main():
    os = ''
    while True:
        action = start_menu()
        #Regression
        cols = ["Rating", "Rating Count", 'Price']

        if action == 1:
            os = os_choice()

            y = choose_val_of_list(cols)
            x = choose_val_of_list(cols)

            ds.regression(os, y, x)


        elif action == 2:
            os = os_choice()
            ds.genre_popularity(os)

        elif action == 3:
            os = os_choice()
            ds.genre_love(os)

        elif action == 4:
            os = os_choice()
            ds.genre_saturation(os)

        elif action == 5:
            os = os_choice()
            ds.correlation(os, 'db2cw')

        elif action == 6:
            os = os_choice()
            cols = db.get_columns('db2cw', os)
            cols.remove('_id')
            cols.remove('Name')
            cols.remove('Platform')
            cols.remove('Rating Count')

            choice = choose_val_of_list(cols)
            ds.get_mode(os, 'db2cw', choice)


        elif action == 7:
            print('This may take a moment, remain patient...')
            repopulate_thru_df()

        elif action == 8:
            os = os_choice()
            ds.genre_max_download(os)

        elif action == 0:
            print("Farewell!")
            break
        #wrong choice
        else:
            print("Enter correct choice (num 0 to 6): ")

if __name__ == '__main__':
    main()

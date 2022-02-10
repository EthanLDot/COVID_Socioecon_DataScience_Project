import pandas as pd

#importing functions from Collar_Cleaning_code.py
from Collar_Cleaning_code import *

def read_labor_data():
    try:
        #retrieve and print csv
        labor_data = pd.read_csv('Cleaned Data\state_labor_data.csv')
        print(labor_data)
    except FileNotFoundError:
        #if csv file does not exist make it
        clean_labor_data()
        read_labor_data()

read_labor_data()
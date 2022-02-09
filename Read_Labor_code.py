import pandas as pd
# importing  all the
# functions defined in test.py
from Collar_Cleaning_code import *

def read_labor_data():
    try:
        labor_data = pd.read_csv('Cleaned Data\state_labor_data.csv')
        print(labor_data)
    except FileNotFoundError:
        clean_labor_data()
        read_labor_data()

read_labor_data()
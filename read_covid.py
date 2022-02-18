import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_covid_data(month: int, day: int, year: int):
    #retrieve cleaned csv
    covid_data_url = r".\Cleaned Data\state_covid_data.csv"
    covid_data = pd.read_csv(covid_data_url)
    
    #reformat date parameter to match data values in csv, then get all data from specific date
    date_filter = formatDate(month, day, year)
    covid_data = covid_data[covid_data["submission_date"] == date_filter]
    covid_data.sort_values("state", inplace=True)
    covid_data.reset_index(inplace=True, drop=True)
    
    return covid_data

def formatPreZero(num: int) -> str:

    #adds '0' char to any integer less than 10 to match formatting
    if num >= 10:
        return str(num)
    
    return "0" + str(num)
    
#reformat date parameter to match data values in csv    
def formatDate(month: int,  day: int, year: int) -> str:
    return f"{year}/{formatPreZero(month)}/{formatPreZero(day)}"
import pandas as pd

def clean_labor_data():
    #Read excel file, renames first column to States and take out null rows
    raw_collar = pd.read_excel("Raw_Data/collar_dataset_raw.xlsx", header = 4)
    raw_collar.rename(columns={"Unnamed: 0": "State"}, inplace=True)
    raw_collar = raw_collar.dropna()

    #Take out data from 2021 and only keep 2020
    raw_collar = raw_collar[["State", "Dec.\n2020", "Dec.\n2020.1", "Dec.\n2020.2"]]

    non_states = ["Virgin Islands", "District of Columbia", "Puerto Rico"]

    #Removes all non official states from dataset
    for region in non_states:
        raw_collar = raw_collar[raw_collar["State"].str.contains(region)==False]

    #Reset index to start at 0
    raw_collar = raw_collar.reset_index(drop = True)

    #Original raw data has different columns stacked on top of each row, so we need to reorder the dataset.
    #Block 1 contains total, constructing and mining data
    block1 = raw_collar[:50]
    block1.columns = ["State", "Total", "Constructing", "Mining"]

    #Block 2 contains Trade, Financial and Professional
    block2 = raw_collar[50:100]
    block2.columns = ["State", "Trade", "Financial", "Prof"]

    #Block 3 contains Education, Leisure and Government
    block3 = raw_collar[100:]
    block3.columns = ["State", "Education", "Leisure", "Gov"]

    collar = block1.merge(block2, on="State")
    collar = collar.merge(block3, on="State")
    collar.to_csv('Cleaned Data/state_labor_data.csv')

clean_labor_data()
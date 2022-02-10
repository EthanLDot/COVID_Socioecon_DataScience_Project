import pandas as pd

#Copied from https://gist.github.com/rogerallen/1583593
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

def clean_labor_data():
    #Read excel file, renames first column to States and take out null rows
    raw_labor_data = pd.read_excel("/Raw Data/collar_dataset_raw.xlsx", header = 4)
    raw_labor_data.rename(columns={"Unnamed: 0": "State"}, inplace=True)
    raw_labor_data = raw_labor_data.dropna()

    #Take out data from 2021 and only keep 2020
    raw_labor_data = raw_labor_data[["State", "Dec.\n2020", "Dec.\n2020.1", "Dec.\n2020.2"]]
    
    non_states = ["Virgin Islands", "District of Columbia", "Puerto Rico"]

    #Removes all non official states from dataset
    for region in non_states:
        raw_labor_data = raw_labor_data[raw_labor_data["State"].str.contains(region)==False]

    #Reset index to start at 0
    raw_labor_data = raw_labor_data.reset_index(drop = True)

    #eliminated extra characters in state names
    raw_labor_data["State"] = raw_labor_data["State"].str.replace('\d+', '')
    raw_labor_data["State"] = raw_labor_data["State"].str.replace('(', '')
    raw_labor_data["State"] = raw_labor_data["State"].str.replace(')', '')

    #Convert state names into codes (First two letters of each state name)
    raw_labor_data["State"] = raw_labor_data["State"].apply(lambda state_name: us_state_to_abbrev[state_name])

    #Original raw data has different columns stacked on top of each row, so we need to reorder the dataset.
    #Block 1 contains total, constructing and mining data
    block1 = raw_labor_data[:50]
    block1.columns = ["State", "Total", "Constructing", "Mining"]

    #Block 2 contains Trade, Financial and Professional
    block2 = raw_labor_data[50:100]
    block2.columns = ["State", "Trade", "Financial", "Professional"]

    #Block 3 contains Education, Leisure and Government
    block3 = raw_labor_data[100:]
    block3.columns = ["State", "Education", "Leisure", "Gov"]

    #merge all blocks into one dataframe
    labor_data = block1.merge(block2, on="State")
    labor_data = labor_data.merge(block3, on="State")

    #We only need data on white collar and blue collar, so we can combine each job sector to their respective group.
    labor_data["White_col"] = labor_data["Constructing"] + labor_data["Mining"] + labor_data["Trade"]
    labor_data["Blue_col"] = labor_data["Trade"] + labor_data["Financial"] + labor_data["Professional"] + labor_data["Education"] + labor_data["Leisure"] + labor_data["Gov"]

    #Get rid of all other columns except State, White_col, Blue_col and Total
    labor_data.drop(columns = ["Constructing", "Mining", "Trade", "Financial", "Professional", "Education", "Leisure", "Gov"], inplace=True)
    #export as csv
    labor_data.to_csv('./Cleaned Data/state_labor_data.csv')

clean_labor_data()
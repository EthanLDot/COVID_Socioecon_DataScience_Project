import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#delete this line when moving code to notebook, along with all imports
from read_covid import *

covid_data = pd.read_csv(r".\Cleaned Data\state_covid_data.csv")
labor_data = pd.read_csv(r".\Cleaned Data\state_labor_data.csv")
soci_data = pd.read_csv(r".\Cleaned Data\clean_socioeconomic_data.csv")

month_year_covid_data = read_covid_data(3, 15, 2021)
#do something
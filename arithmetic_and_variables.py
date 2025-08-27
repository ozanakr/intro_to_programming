print("Hello, world!")

# change the message
print("3 + 4")
print("7")

# print(1+2) It wont print here because of the comment indicator

# create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(str(total_secs) + " seconds")

# set the value of the births_per_min variable
births_per_min = 250

# set the value of the births_per_day variable
births_per_day = births_per_min * mins_per_hour * hours_per_day

import pandas as pd

titanic_data = pd.read_csv("train.csv")
print(titanic_data.head())

# number of total passengers
total_passenger = len(titanic_data)
print(total_passenger)

# number of passengers who survived
survived = (titanic_data["Survived"] == 1).sum()
print(survived)

# number of passengers under 18
minors = (titanic_data.Age < 18).sum()
print(minors)

# fill in the value of the survived_fraction variable
survived_fraction = survived / total_passenger
print(survived_fraction)

# fill in the value of the minors_fraction variable
minors_fraction = minors / total_passenger
print(minors_fraction)
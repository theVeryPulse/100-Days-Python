# SKILLS: pandas
import pandas as pd    # conventional name

# with open('weather_data.csv', 'r') as file:
data = pd.read_csv('weather_data.csv')    # read csv with a panda method

temp_list = data['temp'].to_list()    # cast the Series of 'temp' to a list

print(data['temp'].mean(0))    # calculate mean value using a pandas method on a series object

# find the day with the highest temperature
print('Day with the highest temperature', data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']    # extract a row rather than a column of the DataFrame
print(monday)

monday_temp = int(monday.temp.iloc[0])    # extract the value of an attribute
monday_temp_F = (monday_temp * 9 / 5) + 32    # conversion of Celsius into Fahrenheit
print(monday_temp_F)



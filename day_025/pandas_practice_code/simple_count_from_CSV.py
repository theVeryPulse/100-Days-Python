import pandas as pd

# count how many squirrels there are of each primary fur colour

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

count_data = pd.DataFrame(data_dict)
count_data.to_csv('squirrels count by fur color.txt')

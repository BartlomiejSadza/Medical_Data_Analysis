# Find out the average age of the patients in the dataset.
# Analyze where a majority of the individuals are from.
# Look at the different costs between smokers vs. non-smokers.
# Figure out what the average age is for someone who has at least one child in this dataset.
# ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

import csv

data = []

with open('insurance.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Finding out the average age of the patients in the dataset.
def average_age(data):
    total_age = 0
    for row in data[1:]:
        total_age += int(row[0])
    return round(total_age / len(data[1:]), 1)

# print(f'The average age of this dataset is: | {average_age(data)} |')

# Analyzing where a majority of the individuals are from.
def majority(data):
    regions = {}
    for row in data[1:]:
        region = row[-2]
        if region in regions:
            regions[region] += 1
        else:
            regions[region] = 1
    sorted_regions = sorted(regions.items(), key=lambda item: item[1], reverse=True)
    return sorted_regions

# print('Majority of the individuals in descending order are from:')
# for region, value in majority(data):
#     print(f'{region} | {value} individuals')


# Looking at the different costs between smokers vs. non-smokers.

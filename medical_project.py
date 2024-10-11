# Description: This is a simple project that analyzes a dataset of medical insurance costs. The dataset contains the following columns:
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
def smoking(data):
    
    smokers = []
    non_smokers = []
    
    for row in data[1:]:
        status = row[-3]
        if status == 'no':
            non_smokers.append(float(row[-1]))
        else:
            smokers.append(float(row[-1]))

    average_smokers = round(sum(smokers) / len(smokers), 0)
    average_non_smokers = round(sum(non_smokers) / len(non_smokers), 0)

    return f'The average cost for smokers is: | {average_smokers}$ | and for non-smokers is: | {average_non_smokers}$ | which is a difference of | {average_smokers - average_non_smokers}$ (WHICH IS HUGE!) |'

# print(smoking(data))



# Figuring out what the average age is for someone who has at least one child in this dataset.
def average_age_with_children(data):
    total_age = 0
    count = 0
    total_age_without_children = 0
    count_without_children = 0
    for row in data[1:]:
        childs = int(row[3])
        if childs > 0:
            total_age += int(row[0])
            count += 1
        else:
            total_age_without_children += int(row[0])
            count_without_children += 1

    average_age_with_children = round(total_age / count, 1)
    average_age_without_children = round(total_age_without_children / count_without_children, 1)

    return f'The average age for someone who has at least one child is: | {average_age_with_children} | and for someone who does not have any children is: | {average_age_without_children} |'

# print(average_age_with_children(data))

# Analyzing the average BMI for males vs. females.
def average_bmi_by_gender(data):
  male_bmi = []
  female_bmi = []
  
  for row in data[1:]:
    gender = row[1]
    bmi = float(row[2])
    if gender == 'male':
      male_bmi.append(bmi)
    else:
      female_bmi.append(bmi)
  
  average_male_bmi = round(sum(male_bmi) / len(male_bmi), 1)
  average_female_bmi = round(sum(female_bmi) / len(female_bmi), 1)
  
  return f'The average BMI for males is: | {average_male_bmi} | and for females is: | {average_female_bmi} |'


# Analyzing the average insurance charges by region.
def average_charges_by_region(data):
  region_charges = {}
  
  for row in data[1:]:
    region = row[-2]
    charges = float(row[-1])
    if region in region_charges:
      region_charges[region].append(charges)
    else:
      region_charges[region] = [charges]
  
  average_charges = {region: round(sum(charges) / len(charges), 1) for region, charges in region_charges.items()}
  
  return f'Average insurance charges by region: {average_charges}'

# print(average_charges_by_region(data))

# Analyzing the correlation between BMI and insurance charges.
def bmi_vs_charges(data):
  bmi_charges = []
  
  for row in data[1:]:
    bmi = float(row[2])
    charges = float(row[-1])
    bmi_charges.append((bmi, charges))
  
  bmi_charges.sort()
  
  return bmi_charges

# print(bmi_vs_charges(data))


print(f'The average age of this dataset is: | {average_age(data)} |')
print('\n')
print('Majority of the individuals in descending order are from:')
for region, value in majority(data):
    print(f'{region} | {value} individuals')
print(average_charges_by_region(data))
print('\n')
print(average_bmi_by_gender(data))
print('\n')
print(average_age_with_children(data))
print('\n')
print(smoking(data))

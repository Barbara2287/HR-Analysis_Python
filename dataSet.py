import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQd6sTzHzHzw0xelP8z-gCOtcL9nxxeZTQBOppOBdvtNyttuh0iP1hmEam0XtnXT2xylGvPF2duZbB4/pub?gid=1500491733&single=true&output=csv'
dataHR = pd.read_csv(url)
print(dataHR)

# Transform the DataFrame into a list of lists
values_to_update = [dataHR.columns.values.tolist()] + dataHR.values.tolist()
valor = values_to_update

#Info of a specific column
print(dataHR.info())

#Check out the first 5 records
print(dataHR.head)
print(dataHR.tail())


# 1. Attrition vs. Gender: Compare attrition rates between genders.
#Stacked bar chart to illustrate the number of employees staying and leaving based on their gender.
Attition_Gender = pd.crosstab(dataHR['Gender'], dataHR['Attrition'])

Attition_Gender.plot(kind='bar', stacked=True)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Attrition by Gender')
plt.show()

# 2. Attrition vs. Marital Status: Explore whether employees marital status is linked to attrition.
#A grouped bar chart could be useful in this context.

Attition_MaritalStatus = pd.crosstab(dataHR['MaritalStatus'], dataHR['Attrition'])

Attition_MaritalStatus.plot(kind='bar', stacked=True)
plt.xlabel('MaritalStatus')
plt.ylabel('Count')
plt.title('Attrition by Marital Status')
plt.show()

#3. Attrition vs. Age: Investigate if employees age is associated with attrition.
#Group ages into ranges such as 18-25, 26-35, 36-45, etc.
#Define the age range boundaries.

age_bins = [18, 25, 35, 45, 55, 65, 100]

# Define the tags
age_labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']

# Group the ages into ranges and assign labels
dataHR['Age_Group'] = pd.cut(dataHR['Age'], bins=age_bins, labels=age_labels)
Attition_Age = pd.crosstab(dataHR['Age_Group'], dataHR['Attrition'])

# Create a stacked bar chart
Attition_Age.plot(kind='bar', stacked=True)
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Attrition by Age')
plt.show()

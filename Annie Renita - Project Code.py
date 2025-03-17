import pandas as pd
import matplotlib.pyplot as plt

#Reading the input file
df = pd.read_csv('full_data.csv')
# Checking for missing values
print('The number of missing values in the data set columns are as follows:\n',df.isnull().sum())

#Since there are missing values. We are dropping the rows that are containing NaN values using dropNA funtion.
df=df.dropna()
# Checking the distribution of values in dataset
my_data=df['intent']
print('The distribution of values in the dataset provided of Suicide in US: ',df['intent'].apply(lambda x: len(x.split(' '))).sum())
df.intent.value_counts().plot(kind='bar')
plt.show()
# Making the dataset from multi class to binary class
df.loc[df.intent == "Homicide", "intent"] = "Other"
df.loc[df.intent == "Undetermined", "intent"] = "Other"
df.loc[df.intent == "Accidental", "intent"] = "Other"

#Creating a histogram to see the number of suicides in a particular age range. Hence creating
# a new df which has only ages of people who died of suicide
new_df=df.loc[df.intent == 'Suicide']
# Finding the age of the youngest and oldest person
column=new_df['age']
max_value = column.max()
print('The age of the oldest person who committed suicide in the US is ',max_value,'.')
min_value=column.min()
print('The age of the oldest person who committed suicide in the US is ',min_value,'.')
df[['age']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=1.0)
plt.show()
# Plot a pie chart to see the number of suicides based on sex
new_df.sex.value_counts().plot(kind='pie')
plt.figure(figsize=(8,8), dpi = 80)
plt.show()
# Plot a bar graph to see the number of suicides based on race
new_df.race.value_counts().plot(kind='bar')
plt.show()
# Plot a pie chart to see the number of suicides based on education
new_df.education.value_counts().plot(kind='pie')
plt.show()
# Plot a bar graph to see the number of suicides based on place
new_df.place.value_counts().plot(kind='bar')

# Plot a bar graph to see the number of suicides based on race and education
fig,ax = plt.subplots(figsize=(15,8))
new_df.groupby(['race','education']).count()['intent'].unstack().plot(kind='bar',ax=ax)
plt.show()


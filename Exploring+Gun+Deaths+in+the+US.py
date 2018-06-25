
# coding: utf-8

# In[4]:


import csv

f = open("guns.csv", 'r')
csvreader = csv.reader(f)

data = list(csvreader)
headers = data[0]
print(headers)
data = data[1::]
idx = 0
while idx < 4:
    print(data[idx])
    idx += 1


# In[5]:


years = [int(row[1]) for row in data]
year_counts = {}
for element in years:
    if element in year_counts:
        year_counts[element] += 1
    else:
        year_counts[element] = 1
        
print(year_counts)


# In[6]:


import datetime

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
dates[:5]

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1

date_counts


# In[7]:


sex = [(row[5]) for row in data]
sex_counts = {}
race = [(row[7]) for row in data]
race_counts = {}
for element in sex:
    if element not in sex_counts:
        sex_counts[element] = 1
    else:
        sex_counts[element] += 1
for element in race:
    if element not in race_counts:
        race_counts[element] = 1
    else:
        race_counts[element] += 1

print(race_counts)
print(sex_counts)
    


# So far, the data suggests that men and people of color experience the largest amounts of gun deaths, but I would want to see the distribution of gun death by sex within each race. Also, the dates suggest a stagnation of gun deaths which can be problematic since the number of deaths should be decreasing if current policies and practices for crime resolution are effective. There also seems to be more gun deaths in the summer than other seasons.

# In[8]:


import csv

open_file = open("census.csv", 'r')
csvreader = csv.reader(open_file)

dataB = list(csvreader)
headersB = dataB[0]
census = dataB[1::]

print(census)


# In[12]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[13]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}

for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# It appears that Black/Hispanic Americans face a large amount of gun violence in comparison to other races with White Americans and Asian/Pacific Islanders facing the lowest probability.

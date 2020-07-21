import requests, json
import pprint
import time
import os.path
from os import path
from tqdm import tqdm
for i in tqdm(range(0, 1), desc ="Downloading from RAPIDAPI..."): 
    time.sleep(.1) 



filename = 'mydata.json'
file_created_time = (os.stat(filename).st_mtime)
now = time.time()

if((now-file_created_time)/60 >15 ):
    print ("the file is old please delete it")
    if os.path.exists(filename):
        os.remove(filename)
        print ("the file is old and its removed")


if not path.isfile(filename):
    print ('Connecting to RapidAPI...Please wait')
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "b66d08d003msh377736ab1cce037p1e7447jsne2720223524e"
        }
    response = requests.request("GET", url, headers=headers)
    
    with open(filename, 'w') as f:
        json.dump(response.json(), f)
else :
    print ("file exists, locally" )
    with open(filename) as f:
        data = json.load(f)



#def get_data():
#The stats shown to user will contain number of 
#active cases, critical cases, number of recovered cases, total number of cases and deaths. 
with open('mydata.json') as f:
  data = json.load(f)

response_results = data['response']
stats_dictionary = {}
sort_dictionary = {}
#template =  ["country", "population", "total_cases","active_cases", "recovered_cases", "total_deaths"]
template =  ["totalcases", "details"]

for result in response_results:
    
    country = result['country']
    population = result['population']
    cases = result['cases']
    total_cases = cases['total']
    active_cases = cases['active']
    #critical_cases = cases['recovered']
    recovered_cases = cases['recovered']
    deaths = result['deaths']
    total_deaths = deaths['total']
    
    stats_dictionary_item = {}
    key_template =  ["country", "population", "total_cases","active_cases", "recovered_cases", "total_deaths"]
    item_template = [country,population,total_cases,active_cases,recovered_cases,total_deaths]
    for i in range(len(key_template)):
        stats_dictionary_item[key_template[i]] = item_template[i]
  
    stats_dictionary[item_template[0]] = stats_dictionary_item
    sort_dictionary [item_template[0]] = total_cases
    


ordered_dictionary = {}
invalid_keys = ('Asia','North-America','All','South-America','Europe','South-Africa','Africa')
for key, value in sorted(sort_dictionary.items(), key=lambda x: x[1], reverse=True):
    if(key in invalid_keys):
        continue
    else: ordered_dictionary[key] = value

        
top_count = 5
topcountries_dictionary = {}
#print(country,population,total_cases,active_cases,recovered_cases,total_deaths)

#for counter in range (1,top_count +1):
   #topcountries_dictionary [] = '' 
   
    
#for items in stats_dictionary:
#    print(items,stats_dictionary[items])
    #for key in stats_dictionary[items]

top_five_countries = list()

key = 0
for value in ordered_dictionary:
    if (key < 5):
        top_five_countries.append(str(value))
        key = key + 1
    else: break

for item in top_five_countries:
    print (item)
    print(stats_dictionary.get(item))
       




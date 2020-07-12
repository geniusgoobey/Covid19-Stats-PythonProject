import requests, json
import pprint

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b66d08d003msh377736ab1cce037p1e7447jsne2720223524e"
    }
response = requests.request("GET", url, headers=headers)
print ('Connecting to RapidAPI...Please wait')
with open('mydata.json', 'w') as f:
    json.dump(response.json(), f)


with open('mydata.json') as f:
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

for counter in range (1,top_count +1):
   #topcountries_dictionary [] = '' 
   print(counter)
    
for items in stats_dictionary:
    print(items,stats_dictionary[items])
    #for key in stats_dictionary[items]
        
for value in ordered_dictionary:
    print(value)
  
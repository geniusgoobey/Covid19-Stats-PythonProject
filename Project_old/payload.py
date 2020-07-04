import requests, json
import pprint

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b66d08d003msh377736ab1cce037p1e7447jsne2720223524e"
    }
#response = requests.request("GET", url, headers=headers)

#with open('mydata.json', 'w') as f:
 #   json.dump(response.json(), f)


with open('mydata.json') as f:
  data = json.load(f)

for i in data['response']: 
    print("Country = " + i["country"])
    print(i["cases"]["total"])  
    print(i["cases"]["new"])  
    print(i["cases"]["active"])  
    print(i["cases"]["recovered"])  
    print(i["deaths"]["total"])

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

print(data['response'][0]['country'])
print(data['response'][0]['cases']['total'])




#jsonobj = response.json()
#print(response.json()['response'][0]['country'])
#print(response.json()['response'][1]['country'])
#print(response.json()['response'][0]['cases'])

#pprint.pprint(response.json()['continent'])

#print(json.dumps(jsonobj))

#{'get': 'statistics', 'parameters': [], 'errors': [], 'results': 227, 'response': [{
    #[
    # {'continent': 'Asia', 'country': 'China', 'population': 1439323776, 'cases': {'new': '+26', 'active': 331, 'critical': 13, 'recovered': 78413, '1M_pop': '58', 'total': 83378}, 'deaths': {'new': None, '1M_pop': '3', 'total': #4634}, 'tests': {'1M_pop': None, 'total': None}, 'day': '2020-06-22', 'time': '2020-06-22T01:15:07+00:00'}, 
    # {'continent': 'Europe', 'country': 'Italy', 'population': 60463939, 'cases': {'new': '+224', 'active': 20972, 'critical': 148, 'recovered': 182893, '1M_pop': '3944', 'total': 238499}, 'deaths': {'new': '+24', '1M_pop': '573', 'total': 34634}, 'tests': {'1M_pop': '82435', 'total': 4984370}, 'day': '2020-06-22', 'time': '2020-06-22T01:15:06+00:00'},
import requests, json, os, time
from os import path
from tqdm import tqdm
class RapidAPI :
   
    def __init__(self):
        path_to_script = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(path_to_script,  'covidstats_rawdata.json') 
        self.url = "https://covid-193.p.rapidapi.com/statistics"
        self.headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "b66d08d003msh377736ab1cce037p1e7447jsne2720223524e"
        }



    def __FileRefresh__(self):
        filename = self.filename
        if (path.isfile(self.filename)):
            file_created_time = (os.stat(filename).st_mtime)
            now = time.time()
            if((now-file_created_time)/60 >15 ):
                print ("CovidStats data stored locally in " + filename + " has expired, datasource needs to be refreshed. \n")
                if os.path.exists(filename):
                    os.remove(filename)
                    print ("Expired data purged successfully. \n")
                    return True
            else: 
                #print("File exists.")
                return False
        else : 
            return True



    def __fetchCovidStats__(self):
        if(self.__FileRefresh__()):
            print ('Connecting to RapidAPI.COM...Please wait...\n')
            response = requests.request("GET", self.url, headers=self.headers)
            print('Response received from RapidAPI.COM \n')
            for i in tqdm(range(0, 10), desc ="Downloading Stats RAPIDAPI..."): 
                time.sleep(.05)
                i = i +1
            print("\n")
            with open(self.filename, 'w') as f:
            #with open(os.path.join(sys.path[0], self.filename), 'w') as f:
                json.dump(response.json(), f)
            print("covidstats_rawdata.json, datasource created successfully. \n")
        else :
            print ("covidstats_rawdata.json exists. Connecting to local datasource. \n" )
        with open(self.filename) as f:
             data = json.load(f)
        stats_dictionary = {}
        top_five_countries = list()
        stats_dictionary,top_five_countries = self.__getSortedStatsByCountry__(data)
        #print (top_five_countries)
        return stats_dictionary,top_five_countries

               

    def __getSortedStatsByCountry__(self,data):
        response_results = data['response']
        stats_dictionary = {}
        sort_dictionary = {}
        ordered_dictionary = {}
        #template =  ["totalcases", "details"]
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
       
        invalid_keys = ('Asia','North-America','All','South-America','Europe','South-Africa','Africa')
        for key, value in sorted(sort_dictionary.items(), key=lambda x: x[1], reverse=True):
            if(key in invalid_keys):
                continue
            else: ordered_dictionary[key] = value
        top_count = 5
        top_five_countries = list()
        key = 0
        for value in ordered_dictionary:
            if (key < top_count):
                top_five_countries.append(str(value))
                key = key + 1
            else: break
        return stats_dictionary, top_five_countries
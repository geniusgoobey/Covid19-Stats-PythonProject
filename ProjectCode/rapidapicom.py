import requests, json, os, time
from os import path
from tqdm import tqdm
class RapidAPI :
    '''
    RapidAPI Class contains all the functions and methods required to fetch data from RAPIDAPI.COM

    '''
   
    def __init__(self):
        '''
        initialise the header and token authentication keys required to connect to RAPIDAPI
        '''
        path_to_script = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(path_to_script,  'covidstats_rawdata.json') 
        self.url = "https://covid-193.p.rapidapi.com/statistics"
        self.headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "b66d08d003msh377736ab1cce037p1e7447jsne2720223524e"
        }



    def file_refresh(self):
        '''
        This method checks if raw covid statistics data fetched is still valid or has expired.
        Method returns 
        'True' if new data needs to be fetched from RAPIDAPI. 
        'False' if fetched data (saved locally) is valid and can be used.  
        '''
        try:
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
                    # File exits and data is still valid
                    return False
            else : 
                #File doesn't exits create the file
                return True
        except : return True



    def fetch_covid_stats(self):
        '''
        This is main method which connects to RAPIDAPI.COM and fetches the covid statistics data 
        and saves it locally in a JSON file
        '''
        try:
            if(self.file_refresh()):
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
            stats_dictionary,top_five_countries = self.get_sortedstats_by_country(data)
            #print (top_five_countries)
            return stats_dictionary,top_five_countries
        except:
            print("Error occured while connecting to RAPIDAPI. Press Enter key to continue..." , end = " ")
            input()


               

    def get_sortedstats_by_country(self,data):
        '''
        This function combes through the raw data returned by RAPIDAPI.COM's Covid API. 
        It unpacks the raw data, sorts depending on the total number of cases per country.
        It retuns top 5 most covid positive countries list along with processed Covid Data
        '''
        response_results = data['response']
        stats_dictionary = {}
        sort_dictionary = {}
        ordered_dictionary = {}
        
        #read through raw data returns from the Response object and fetch required information.
        for result in response_results:
            country = result['country']
            population = result['population']
            cases = result['cases']
            total_cases = cases['total']
            active_cases = cases['active']
            critical_cases = cases['critical']
            new_cases = cases['new']
                       
            recovered_cases = cases['recovered']
            deaths = result['deaths']
            total_deaths = deaths['total']
            
            stats_dictionary_item = {}
            key_template =  ["country", "population", "total_cases","active_cases", "recovered_cases", "total_deaths","critical_cases","new_cases"]
            item_template = [country,population,total_cases,active_cases,recovered_cases,total_deaths,critical_cases,new_cases]
            for i in range(len(key_template)):
                stats_dictionary_item[key_template[i]] = item_template[i]
        
            stats_dictionary[item_template[0]] = stats_dictionary_item
            sort_dictionary [item_template[0]] = total_cases

        # The Raw Data contains infromation aggregated at Continent level, which needs to be ignored.         
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
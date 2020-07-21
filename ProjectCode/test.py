import os.path
import time
from os import path
from tqdm import tqdm
from rapidapicom import RapidAPI
from mapplot import PlotChart
os.system('cls')

stats_dictionary = {}
top_five_countries = list()
start = 0
try:
    while (True):
        print('Welcome to CovidStats Main Program\n')
        print("Type 'Start' to begin the program, type 'Quit' to exit the program \n")
        usercode = str.upper(input())
        if(usercode =='QUIT'):
            print("Exiting the program. Thank You. \n")
            break
        elif(usercode=='START'):
            while (True):
                os.system('cls')
                print('Welcome to CovidStats \n')
                print("type 'Quit' anytime to exit to main program\n")
                
                for j in tqdm(range(0, 5), desc ="Fetching the Top 5 Counties with highest recorded Covid cases...Please Wait."): 
                    time.sleep(.05)
                    j = j +1
                print("\n")
                obj = RapidAPI()
                stats_dictionary,top_five_countries = obj.__fetchCovidStats__()
                userinput = ''
                print("Top 5 Counties with highest recorded Covid cases are : ", top_five_countries)
                print("\n Enter the number associated with the Country to see the Covid Stats\n")
                i = 1
                for item in top_five_countries:
                    print( i , " - " , item)
                    i = i + 1
                print("Please enter a value: ")
                userinput = str.upper(input())
                if(userinput.isdigit()):
                    value = int(userinput)
                    if(value >=1 and value<=5):
                        selected_country = top_five_countries[value-1]
                        print (selected_country)
                        print(stats_dictionary.get(selected_country))
                        chartObj = PlotChart()
                        chartObj.__draw__(stats_dictionary.get(selected_country))
                    else:
                        print ("Invalid Entry. Please enter a value between 1 and 5 only. Press Enter key to continue... \n")
                        input()
                        continue
                else:
                    if(userinput =='QUIT'):
                        print("Exiting Covid Stats sub program. Thank You. \n")
                        break
                    else: 
                        print ("Invalid Entry. Press Enter key to continue... \n")
                        input()
                        continue
        else: 
            print('Invalid Entry. Accepted values ''start'' or ''quit''  Press Enter key to continue... \n')
            input()
            os.system('cls')
except KeyboardInterrupt:
    print ("Interrupt key detected. Terminating program now.  Thank You.")
    exit()
except :
    print ("Unexpected Error Occured. Terminating program now. Thank You.")
    exit()
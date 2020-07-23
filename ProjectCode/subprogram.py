import os.path
import time
from os import path
from tqdm import tqdm
from rapidapicom import RapidAPI
from mapplot import PlotChart
os.system('cls')
import matplotlib.pyplot as plt


class Subprogram :
    '''
    This Class contains the logic to drive the Command line interactions with users.
    '''

    def sub_program(self):
        '''
        This Program interacts with the user, displays available countries for selection, 
        accepts user inputs and displays covid statistics according to the selections made by user.
        '''
        try:
            stats_dictionary = {}
            top_five_countries = list()
            while (True):
                os.system('cls')
                        
                print('Welcome to CovidStats \n')
                print("type 'Quit' anytime to exit to main program\n")
                        
                for j in tqdm(range(0, 5), desc ="Fetching the Top 5 Counties with highest recorded Covid cases...Please Wait."): 
                    time.sleep(.05)
                    j = j +1
                print("\n")
                rapidapi_obj = RapidAPI()
                stats_dictionary,top_five_countries = rapidapi_obj.fetch_covid_stats()
                userinput = ''
                print("Top 5 Counties with highest recorded Covid cases are : ", top_five_countries)
                print("\n Enter the number associated with the Country to see the Covid Stats\n")
                i = 1
                for item in top_five_countries:
                    print( i , " - " , item)
                    i = i + 1
                print("Please enter a value: ", end =" ")
                userinput = str.upper(input())
                if(userinput.isdigit()):
                    value = int(userinput)
                    if(value >=1 and value<=5):
                        selected_country = top_five_countries[value-1]
                        print (selected_country)
                        print(stats_dictionary.get(selected_country))
                        plt.close("all")
                        chart_object = PlotChart()
                        chart_object.draw_piechart(stats_dictionary.get(selected_country))
                    else:
                        print ("Invalid Entry. Please enter a value between 1 and 5 only. Press Enter key to continue...", end =" ")
                        input()
                        plt.close("all")
                        continue
                elif(userinput =='QUIT'):
                    print("Exiting Covid Stats sub program. Thank You. \n")
                    plt.close("all")
                    break
                else:
                    print ("Invalid Entry. Please enter a value between 1 and 5 only. Press Enter key to continue...", end =" ")
                    input()
                    plt.close("all")
                    continue
        except KeyboardInterrupt:
            print ("User requested to end the program. Terminating sub program now.")
            plt.close("all")
            exit()
        except :
            print ("Unexpected Error Occured. Terminating sub program now.")
            plt.close("all")
            exit()

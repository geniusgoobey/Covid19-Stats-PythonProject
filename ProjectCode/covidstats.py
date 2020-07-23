import os.path
from tqdm import tqdm
from rapidapicom import RapidAPI
from subprogram import Subprogram
from mapplot import PlotChart
import matplotlib.pyplot as plt


os.system('cls')
try:
    while (True):
        print('Welcome to CovidStats Main Program\n')
        print("Type 'Start' to begin the program, type 'Quit' to exit the program \n")
        usercode = str.upper(input())
        if(usercode =='QUIT'):
            print("Exiting the program. Thank You. \n")
            break
        elif(usercode=='START'):
            #fork obj for sub program
            print("call subprogram")
            child_prog_obj = Subprogram()
            child_prog_obj.sub_program()
        else: 
            print('Invalid Entry. Accepted values are "start" or "quit"  Press Enter key to continue...', end =" ")
            input()
            plt.close("all")
            os.system('cls')


except KeyboardInterrupt:
    print ("User requested to end the program. Terminating program now. Thank You.")
    plt.close("all")
    exit()
except :
    print ("Error Occured. Terminating program now. Thank You.")
    plt.close("all")
    exit()



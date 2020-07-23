import matplotlib.pyplot as plt
from datetime import date

class PlotChart:

     '''
     PlotChart Class contains methods required to plot the PIE charts using the Matplotlib module.
     '''

     def draw_piechart (self,drawobject):

       '''
          This method plots the PIE chart showing the Covid statistics for user selected country.
       '''
       try:
            #Format the numbers to be displayed
            Active = "Active Cases : " + "{:,}".format(drawobject["active_cases"])
            Recovered  = "Recovered Cases : " + "{:,}".format(drawobject["recovered_cases"])
            newObj = drawobject["new_cases"]
            new_Count = int(newObj.replace("+", ""))
            new_Label = "New Cases : " + "{:,}".format(new_Count)
            Critical = "Critical Cases : " + "{:,}".format(drawobject["critical_cases"])
            Deaths = "Total Deaths: " + "{:,}".format(drawobject["total_deaths"])
            #Create labels to be displayed in Legends section of the graph
            labels = [Active,Recovered,new_Label,Critical,Deaths]
            #Create a values list with the data required to plot the graph, obtained from drawobject
            values = [drawobject["active_cases"], drawobject["recovered_cases"] , new_Count,drawobject["critical_cases"], drawobject["total_deaths"]]
            fig = plt.figure(5, figsize=(10,7))
            ax = fig.add_subplot(121)
            myTitle = "Covid Stats for " + str(drawobject["country"] +". Total Population: " + "{:,}".format(drawobject["population"]))
            ax.set_title(myTitle)
            ax.axis('equal')
            #set custom colors for the graph
            colors = ["#F6728099" ,"#99B898","#355C7D","#E8175D","#474747"]
            explode = [0.01,0.01,0.01,0.01,0.01]
            pie = ax.pie(values, startangle=0,colors=colors, explode=explode)
            ax2 = fig.add_subplot(122)
            ax2.axis("off") 
            title = "Stats : " + date.today().strftime ('%d-%b-%Y') + "\n"
            ax2.legend(pie[0],labels, loc="right",title=title,fancybox=True)
            fig.show()
       except:
            print("Error Occured while plotting Chart. Press Enter key to continue") 
            input()
        
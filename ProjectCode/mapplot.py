import matplotlib.pyplot as plt

class PlotChart:

    def __draw__ (self,drawobject):
        plt.figure(figsize=(5,5))
        #plt.style.use('grayscale')
        myTitle = "Covid Stats for " + str(drawobject["country"])
        plt.title(myTitle)
        #drawobject
        #{'country': 'USA', 'population': 331102850, 'total_cases': 3898550, 'active_cases': 1952923, 'recovered_cases': 1802338, 'total_deaths': 143289}
        #key_template =  ["country", "population", "total_cases","active_cases", "recovered_cases", "total_deaths"]

        #labels = ["USA","CHINA","INDIA","CANADA","Turkey"]
        labels = ["active_cases", "recovered_cases", "total_deaths"]
        #values = [25,10,50,40,30]
        values = [drawobject["active_cases"], drawobject["recovered_cases"],drawobject["total_deaths"]]
        explode = [0.02,0.02,0.02]
        colors = ["cadetblue","lightgreen","crimson"]
        plt.pie(values, labels=labels, autopct = "%.1f%%",explode = explode, colors=colors)
        plt.show()
        #print(plt.style.available)
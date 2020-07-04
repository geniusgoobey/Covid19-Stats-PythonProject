import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
labels = ["USA","CHINA","INDIA","CANADA","Turkey"]
values = [25,10,50,40,30]
explode = [0.05,0.05,0.05,0.05,0.05]
colors = ["c","b","g","r","y"]
plt.pie(values, labels=labels, autopct = "%.1f%%",explode = explode, colors=colors)
plt.show()
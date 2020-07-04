import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
#plt.style.use('grayscale')
test = "My Covid Stats for Country"
plt.title(test)

labels = ["USA","CHINA","INDIA","CANADA","Turkey"]
values = [25,10,50,40,30]
explode = [0.02,0.02,0.02,0.02,0.02]
colors = ["lightcoral","cadetblue","lightseagreen","crimson","powderblue"]
plt.pie(values, labels=labels, autopct = "%.1f%%",explode = explode, colors=colors)
plt.show()

print(plt.style.available)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

data = pd.read_excel("2023_population.xlsx")
plt.figure(figsize=(9,9))
ex =  [0.1, 0, 0, 0,0,0,0,0,0,0]


c = [ "#06172e", "#07233e", "#08304e", "#053e5d", "#004c6d", "#296080",
     "#447494", "#5e89a9", "#769fbe", "#8fb5d3"]

plt.pie(data["world_%"], colors=c, labels=data["country"],autopct='%1.1f%%',
        textprops={'size': 'large',
                   "fontweight": "bold",
                   "color":"white"},
        explode = ex, shadow = True)

plt.title("TOP-10 MOST POPULATED COUNTRIES", size=16, fontweight="bold")
plt.savefig("myImage.png", format="png", dpi=1000)
plt.show()

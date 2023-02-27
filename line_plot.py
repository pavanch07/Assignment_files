
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("green_gases.xlsx")

#plt.style.use('dark_background')

a = list(data.columns)
b = [0, "-mD", "-ko", "-b1", "-rs", "--"]
plt.figure(figsize=(13,8))

for i in range(1, len(a)):
    plt.plot(data[a[0]], data[a[i]], b[i], label=a[i], markersize=3)

plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.legend(loc="upper right", fontsize="large")

plt.title("GREENHOUSE GASES GRAPH", size=14,fontweight="bold")
plt.xlabel("YEARS from 1990 - 2020", fontsize = 14)
plt.ylabel("Green gases quantity in atmosphere", fontsize = 15)

plt.savefig("myImage.png", format="png", dpi=1000)

plt.show()






















"""plt.figure()

plt.plot(d["Year"], d["Carbon dioxide"], label="co2", marker="2")
plt.plot(d["Year"], d["Methane"], "-wo", label="Methane", markersize=3)
plt.plot(d["Year"], d["Nitrous oxide"], "-b1", label="Nitrous oxide", markersize=4)
plt.plot(d["Year"], d["Hydrofluorocarbons"], "-rs", label="Hydrofluorocarbons", markersize=3)
plt.plot(d["Year"], d["Total_greenhouse_gas"], "--", label="Total_greenhouse_gas",)

#plt.plot( d["Year"],d["Perfluorocarbons"], label = "Perfluorocarbons", marker = "1")
#plt.plot( d["Year"],d["Sulphur hexafluoride"], label = "Sulphur hexafluoride", marker = "v")


plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.legend(loc="upper right", fontsize="x-small",)

plt.title("GREENHOUSE GASES IN ATMOSPHERE", size = 14)
plt.xlabel("YEARS from 1990 - 2020")
plt.ylabel("Green gases quantity in atmosphere")

plt.show()
"""

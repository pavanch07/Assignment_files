import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel("india_corona.xlsx")


fig, (ax1, ax2) = plt.subplots(nrows=2,
                               ncols=1,
                               figsize=(15, 10))

ax1.bar(df["month"], df["cases"], color="brown")
ax2.bar(df["month"], df["deaths"], color="blue")

fig.text(0.5, 0.04, 'N.o of Deaths over 12 months', ha='center',
         va='center', fontsize=20)
fig.text(0.5, 0.49, 'N.o of Cases over 12 months', ha='center',
         va='center', fontsize=20)
fig.text(0.06, 0.5, 'Number of cases', ha='center',
         va='center', rotation='vertical', fontsize=23)
fig.text(0.5, 0.93, 'CORONA CASES & DEATHS',
         ha='center', va='center', fontsize=25)
plt.savefig("myImage.png", format="png", dpi=1000)
plt.show()

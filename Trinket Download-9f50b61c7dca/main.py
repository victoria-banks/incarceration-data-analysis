import pandas as pd 
import matplotlib.pyplot as plt 

hi = pd.read_csv("incarceration.csv")
hi["gap"] = hi['Black']- hi['White']

plt.figure()
plt.plot(hi["Year"], hi["Black"], label = 'Black')
plt.plot(hi["Year"], hi["White"], label = 'White')

plt.xlabel("Year")
plt.ylabel("Incarceration rates per 100,000")
plt.title("Incarceration rates by race (2005-2025)")
plt.legend()
plt.show()

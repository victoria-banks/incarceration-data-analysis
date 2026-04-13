import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("disenfranchisement_data.csv")
df["Value"] = df["Value"].str.replace("%", "").astype(float)

racedf = df[df["Table"] == "Rate of Disenfranchisement by Race/Ethnicity (2022)"]

plt.figure(figsize=(8,5))
bars = plt.bar(racedf["Category"], racedf["Value"])

plt.ylabel("Percent Disenfranchised")
plt.title("Rate of Disenfranchisement by Race/Ethnicity (2022)")
plt.xticks(rotation=45)

for bar in bars:
  height = bar.get_height()
  plt.text(bar.get_x() + bar.get_width()/2, height,
    f"{height:.2f}%", ha='center', va='bottom')

plt.tight_layout()
plt.show()

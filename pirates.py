import pandas as pd
import matplotlib.pyplot as plt

pirate_attack_data = {
    "Number of Pirate Attacks": ["445", "439", "297", "264", "245", "246", "191", "180", "201", "162", "195", "132", "115", "120", "116"],
    "Year": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
}

df = pd.DataFrame(pirate_attack_data)

plt.figure(figsize=(10, 6))
bars = plt.barh(df["Number of Pirate Attacks"], df["Year"], color="Navy")

plt.xlabel("Year")
plt.ylabel("Number of Pirate Attacks")
plt.title("Number of Pirate Attacks Each year (2010-2024)")

plt.show()
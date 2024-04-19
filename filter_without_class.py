import pandas as pd

df = pd.read_csv('data/pokemon.csv')
# print(df.info())

df_filtered = df[df["Type 1"] == "Grass"]
#print(df_filtered)

df_filtered = df_filtered[df_filtered["Type 2"] == "Flying"]
print(df_filtered)

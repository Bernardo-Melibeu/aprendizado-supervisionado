import pandas as pd
from funcs import faz_opinion

df_original=pd.read_csv("data\winequalityN.csv")
#branco
df_white=df_original.loc[df_original["type"]=="white"].copy()
faz_opinion(df_white)
df_white.dropna(inplace=True)
#tinto
df_red=df_original.loc[df_original["type"]=="red"].copy()
faz_opinion(df_red)
df_red.dropna(inplace=True)
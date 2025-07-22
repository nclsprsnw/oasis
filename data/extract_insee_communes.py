
# !pip install pandas
# il s'agit de transformer le fichier des codes insee des communes pour le réduire à nos besoind
# en entrée le fichier 20230823-communes-departement-region.csv doit être dans le repertoire courant
# en sortie nous obtenons le fichier ref_espace_communes.csv qui sera notre reference pour le projet Oasis
import pandas as pd
#
df_insee=pd.read_csv("./20230823-communes-departement-region.csv")# Fichier source de M. Badaoui
#print("Raw describe")
#display(df_insee.describe())
df_insee.drop(columns=["ligne_5","article"], inplace=True) # retrait des colonnes jugées inutiles "ligne_5","article" 
#print("Before duplicate removing")
#display(df_insee.describe())
df_insee.drop_duplicates(subset=["latitude","longitude"],inplace=True) # retrait des doublons communes par coordonnées GPS
#print("After duplicate removing")
#display(df_insee.describe())
df_insee=df_insee[df_insee["code_postal"]<96000] # retrait via code postal de Monaco et les DOM-TOM
#print("After removing Monaco et DOM-TOM")
#display(df_insee.describe())
#df_insee.info()
#print()
#print("number of NAN values :",df_insee.isna().sum().sum())

#display((df_insee.head(10)))
#print()
#df_insee.tail(100)
df_insee.to_csv("./ref_espace_communes.csv")
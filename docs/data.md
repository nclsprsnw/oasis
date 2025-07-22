# Information sur les sources de données
Cette page donne les sources de données utilisées pour ce projet.

## Information géographique

Pour relier les données entre les sources, nous nous appuyons sur l'identifiant des communes au sens de l'INSEE. Pour cela, nous utilisons commen reference pour le projet, le dataset enrichi du site Data Gouv pour les communes au sens INSEE identifiant Data Gouv : 5ced14688b4c4114480ce688
Le lien suivant amène sur le page du dataset [Communes de france - Base des codes postaux 5ced14688b4c4114480ce688](https://www.data.gouv.fr/datasets/communes-de-france-base-des-codes-postaux/informations)

A partir du fichier  20230823-communes-departement-region.csv, nous avons extrait le fichier  ref_espace_communes.csv en executant le script python [extract_insee_communes.py](../data/extract_insee_communes.py)
**Attention:** 
en 2021, il y a eu le fusion de 5 communes en 2.
[Nouvelles communes](https://fr.wikipedia.org/wiki/Liste_des_communes_nouvelles_créées_en_2021)

### projection de Lambert
Passage de X, Y à lat, lon

### regrouppement des stations de pollution

Il faut associer les stations de mesure à des communes.


## Evènements naturels

Collecte des données géo-environnementales
Par zone géographique (code postal, commune, maille GPS…) :

* Inondation (zone PPRI, fréquence historique)
* Incendies de forêt (base Prométhée, surfaces brûlées)
* Séismes (zonage sismique, magnitude max observée)
* Glissements de terrain
* Canicules / sécheresse (indice SPI, température extrême)
* Altitude, proximité de plans d’eau, couverture végétale
* Score de vulnérabilité urbaine (si disponible)

Le tableau ci-dessous donne des sources pour le projet.



La colonne Used sert à définir si elles sont utilisées dans le projet (Y : utilisée, N: non utilisée)


| Nom de la base                                    | Thématique                          | Accès données                                                                                            | URL API / Doc API                                                            | Used |
|---------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------|
| Météo-France Données publiques                    | Climat, température                 | https://meteo.data.gouv.fr/datasets/6569b3d7d193b4daf2b43edc                                                                               |                                          |      |
| BDIFF (Base de Données des Incendies Forêts)      | Feux de forêt                       | https://bdiff.agriculture.gouv.fr/incendies?sort=i.annee&direction=asc&page=7#tab                                                                        |                             |      |                                                   |      |
| Laboratoire Central de Surveillance de la Qualité de l'Air | Pollution de l'air  |https://www.data.gouv.fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1/ | | Y |



## Données sur la valeur immobilière des biens

### Indicateurs Immobiliers par commune et par année (prix et volumes sur la période 2014-2024)

https://explore.data.gouv.fr/fr/datasets/63dd1cc420bf925d5d1d8b1e/?INSEE_COM__contains=80#/resources/1b85be7c-17ce-42dc-b191-3b8f3c469087

### Indicateurs Immobiliers par commune et par année (prix et volumes sur la période 2014-2023)
https://www.data.gouv.fr/datasets/indicateurs-immobiliers-par-commune-et-par-annee-prix-et-volumes-sur-la-periode-2014-2023/
Indicateurs Immobiliers par commune et par année (prix et volumes sur la période 2014-2024)
#### Description
Ce jeu de données centralise pour chaque année (entre 2014 et 2023) plusieurs variables agrégées sur le marché de l'immobilier résidentiel à l'échelle des communes:

Le nombre de mutations
Le nombre de ventes de maisons et d'appartements
La proportion de ventes de maisons et d'appartements
Le prix moyen des biens vendus
Le prix moyen au m2 des biens vendus
La surface moyenne des biens vendus
Le champ d'identification (et de jointure) des communes est basée sur le code INSEE (COG) de l'année.

Ces données sont dérivées d'un traitement de la base DVF géolocalisée, voici les mutations prises en comptes:

Mutation monoventes (pas de ventes en lots)
Prix entre 15 000 € et 10 000 000 €
Surfaces des appartements (entre 10m² et 250m²) et surfaces des maisons (entre 10m² et 400m²)
Prix au m² entre 330 €/m² et 15 000 €/m²
La méthodologie en détail est expliquée ici > https://journals.openedition.org/cybergeo/39583

### Indices du prix des logements et des loyers publiés par l’INSEE
https://www.insee.fr/fr/statistiques?debut=0&idprec=8576105&theme=30&conjoncture=56

### Demandes de valeurs foncières DVF
https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres/

## informations sociales complémentaires

### Plan de relance - Projets industriels : liste, géolocalisation et description synthétique des projets
https://data.economie.gouv.fr/explore/dataset/plan-de-relance/map/?location=5,46.43786,4.4165&basemap=jawg.light

### Transport : 

- en commun https://transport.data.gouv.fr/stats?locale=en
- aérien https://www.data.gouv.fr/reuses/carte-de-localisation-des-aeroports/
- ferroviaire https://ressources.data.sncf.com/explore/dataset/lignes-par-region-administrative/map/?location=6,46.69508,2.48494&basemap=jawg.transports
- autoroutes https://www.data.gouv.fr/datasets/autoroutes-dans-openstreetmap/

### Carte de la densité des professionnels de santé en France
https://www.data.gouv.fr/reuses/carte-de-la-densite-des-professionnels-de-sante-en-france/
Pour @FAYCEL  la carte des régions par genre https://www.ined.fr/fr/tout-savoir-population/chiffres/france/structure-population/regions/




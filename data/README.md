# Information sur les sources de données
Cette page donne les sources de données utilisées pour ce projet.

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

### Cartographie des zones inondables des Territoires à risque important d'inondation (TRI)
https://www.data.gouv.fr/reuses/cartographie-des-zones-inondables-des-territoires-a-risque-important-dinondation-tri/

### changement climatique :
https://www.data.gouv.fr/datasets/donnees-changement-climatique-sim-quotidienne/

### sécheresse :
https://www.data.gouv.fr/datasets/donnee-secheresse-propluvia/

### incendie :
https://www.data.gouv.fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours/

### Densité des professionnels de santé par département :
https://cdonline.articque.com/share/display/professionnels-de-sante

### Zones prévention incendies de forêts 🥵  97 pages de data
https://www.data.gouv.fr/datasets/?q=zone+incendies&page_size=20&page=1


La colonne Used sert à définir si elles sont utilisées dans le projet (Y : utilisée, N: non utilisée)


| Nom de la base                                    | Thématique                          | Accès données                                                                                            | URL API / Doc API                                                            | Used |
|---------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------|
| Météo-France Données publiques                    | Climat, température                 | https://meteo.data.gouv.fr                                                                               | https://meteo.data.gouv.fr/page/api                                           |      |
| Copernicus Climate Data Store (CDS)               | Climat, températures, sécheresse    | https://cds.climate.copernicus.eu                                                                        | https://cds.climate.copernicus.eu/api-how-to                                  |      |
| ECA&D (European Climate Assessment & Dataset)     | Températures historiques            | https://www.ecad.eu                                                                                      | https://www.ecad.eu/download/ensembles/download.php                           |      |
| ONERC (Indicateurs climat France)                 | Climat, indicateurs nationaux       | https://www.ecologie.gouv.fr/onerc                                                                       | Pas d’API publique                                                            |      |
| BDIFF (Base de Données des Incendies Forêts)      | Feux de forêt                       | https://bdiff.agriculture.gouv.fr                                                                        | https://bdiff.agriculture.gouv.fr/opendata/apidoc                             |      |
| Prométhée                                         | Feux de forêt (Sud, Méditerranée)   | https://www.promethee.com/feux                                                                           | Pas d’API publique                                                            |      |
| EFFIS (European Forest Fire Info System)          | Feux de forêt (Europe)              | https://effis.jrc.ec.europa.eu                                                                           | https://effis.jrc.ec.europa.eu/about-effis/data-and-services                  |      |
| Météo des Forêts (Météo-France)                   | Risque feux, sécheresse des forêts  | https://meteofrance.com/actualites-et-dossiers/risque-feux-de-foret                                      | Pas d’API publique                                                            |      |
| Vigicrues / SCHAPI                                | Inondations, crues                  | https://www.vigicrues.gouv.fr                                                                            | https://www.vigicrues.gouv.fr/api                                             |      |
| BDHI (BRGM)                                       | Inondations historiques             | https://bdhi.fr                                                                                          | Pas d’API publique                                                            |      |
| Banque Hydro                                      | Hydrométrie (débits, hauteurs)      | https://hydro.eaufrance.fr                                                                               | https://hydro.eaufrance.fr/api-doc                                            |      |
| GéoRisque – Cartorisque                           | Cartes aléas (inondation, mouvements)| https://www.georisques.gouv.fr                                                                           | https://georisques.gouv.fr/api-doc                                            |      |
| INRAE – Portail RésEAU                            | Sécheresse hydrologique             | https://hydro.eaufrance.fr/page/hydroportail                                                             | Pas d’API publique dédiée                                                     |      |
| Météo-France – Indice d’humidité des sols         | Sécheresse des sols                 | https://www.data.gouv.fr/fr/datasets/indice-dhumidite-des-sols-en-france-metropolitaine/                 | Pas d’API publique                                                            |      |
| SISE-Eaux – Outils sécheresse                     | Arrêtés, restrictions sécheresse    | https://propluvia.developpement-durable.gouv.fr                                                          | https://propluvia.developpement-durable.gouv.fr/propluviapublic/              |      |
| BRGM – GéoRisque (Mouvements/risques)             | Glissements, sismique, radon        | https://www.georisques.gouv.fr                                                                           | https://georisques.gouv.fr/api-doc                                            |      |
| Tempêtes historiques                              | Grands vents, tempêtes              | https://www.data.gouv.fr/fr/datasets/base-de-donnees-tempetes-historiques-en-france/                     | Pas d’API publique                                                            |      |
| hubEau (eaufrance)                                | Eau, hydrométrie, nappes, qualité   | https://hubeau.eaufrance.fr                                                                                 | https://hubeau.eaufrance.fr/page/api                                          |      |
| data.gouv.fr                                      | Données publiques généralistes      | https://www.data.gouv.fr                                                                                 | https://www.data.gouv.fr/fr/pages/api/                                        |      |
| GéoServices IGN                                   | Cartographie, fonds, orthos         | https://geoservices.ign.fr                                                                               | https://geoservices.ign.fr/documentation                                      |      |


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




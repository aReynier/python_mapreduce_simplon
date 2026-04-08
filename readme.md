# Python Mapreduce
Ceci est un exercice simple de suivre la logique d'un mapReduce au moyen d'un script python sans framework ni librairie.

La contexte de ce script est celui d'une plate-forme de streaming. Nous avons les logs des films visionnés et nous souhaitons obtenir les deux listes suivantes:
- Le nombre total de vues par films
- La durée totale visionnée par genre

Il suit la logique suivante:
- map: les données sont mappées
- shuffle: les données sont regroupées par paires clé-valeur
- reduce: cette fase applique la logique voulue


## Installer le dépôt
Cloner le dépôt:
```
git clone https://github.com/aReynier/python_mapreduce_simplon.git
```

Installation d'environnement recommandé
Le nom d'environnement choisi ici est:
```
mapreduce_env
```

## Lancer le script
Pour lancer le script python:
```
python script.py
```
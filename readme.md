# Project

Ce projet consiste à entrainer et à deployer un classifieur binaire des reviews en fonction de leurs contenues.

``` Autheurs: Yves SAIDO  ```

Ce depot contient deux dossiers principales: app et notebook.
- Le dossier app: contient l'api et notebook contient toutes notes.

## Lancer l'api

- Se placer à la racine de projet
- cd app
- lancer la commande pip install -r requirements.txt pour installer tous les modules necessaires
- lancer la commande: ``` source env.sh ```
- lancer : ``` flask run ```


## Exemple d'une requete ( Vous pouvez utiliser postman)

- Curl: ``` curl -X POST -d '{"review" : "Ceci est un test pour verifier le bon fonctionnement de l api", "title" : "test", "stars" : "4" }' localhost:5000/predict/ ```


## Error

- Les erreurs sont gerées de sorte à renvoyer un fichier json qui vous dit que votre requete n'est pas correcte et vous envoie à consulter la doc.

## Test

- Se placer dans le dossier app.
- Lancer : ``` python3 testAPI.py```
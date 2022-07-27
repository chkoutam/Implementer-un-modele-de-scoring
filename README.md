# Implementer-un-modele-de-scoring

## Objectifs

La société financière d’offre de crédit à la consommation Prêt à dépenser souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).
Selon les chargés de relation client, les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l’entreprise veut incarner. De ce fait, Prêt à dépenser décide donc de développer un Dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement. 

## Mission

Notre mission sera donc de développer un algorithme de classification permettant de refuser ou d’accorder un prêt à un client en interagissant facilement avec un Dashboard. Le Dashbord sera donc le socle de transparence pour expliquer la décision de la société. 


## Organisation du code
Le git comporte deux dossiers:

### 1.Modélisation,
DAns le dossier modélisation, se trouvent toutes les notebooks permettant l'étude de l'EDA à la modélisation. Ainsi, on trouve les notebooks suivants: 

- EDA pour l'analyse exploratoire
- Préprocessing: pour le nettoyage et les différentes imputations
- Features enginnering pour la création de variables, mais aussi la création des variables statistiques interéssentes
- Et bien sur le notebook de la modélisation, permettant de tester plusieurs modèles, mais aussi plusieurs métriques

### 2.Dashboard
Dans le dossier Dashboard, se trouve principalement: 
- Un fichier dashboard.ipynb qui explique ce qui va être fait sur le dashboard
- un fichier python dashboard.py qui permet de lancer le dashboard interractif fait sur stramlit et qui se 
- un fichier python API.py permettant de lancer l'API mlflow et de le deployer
connectera automatiquement à l'API afin de bien présenter les différents paramètres de l'application.
- Un fichier InterractionAPI.py qui permet d'interagir avec l'API sans passer par le Dashboard

## Note
Vous trouverez aussi la note méthodologie du Dashboard ansi qu'une présentation de l'ensemble de l'étude
"""Interraction avec l'API: en local ou sur le web
Auteur: Check KOUTAME
Local URL: http://127.0.0.1:5000
aws  : 'http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/invocations'
Il faut d'abord que le modèle soit en ligne ou en local avant de l'interroger
Pour le deploiement du modèle (en ligne ou local) se référer à API.py
"""

# ====================================================================
# Version : 0.0.1 - CK 27/07/2022
# ====================================================================

__version__ = '0.0.1'

# ====================================================================
# Chargement des librairies
# ====================================================================

import pickle
import mlflow
import mlflow.sklearn
import os 
import json
import requests

# ====================================================================
# Interraction en locale ou en ligne - sur python
# ====================================================================

# Saisie le client dont vous voulez faire la prédiction
client_id=100001


Interraction=False
# Interraction en locale: True; Interraction sur aws: False
if Interraction==True:
    MLFLOW_URI = 'http://127.0.0.1:5000/invocations'  
else:
    # Lien sur le web où est hebergé le model comme étant un service
    MLFLOW_URI = 'http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/invocations' 
    


# Fonction de requesti auprès de l'API deloyé sur aws
def request_prediction(model_uri, data):
    headers = {"Content-Type": "application/json"}

    data_json = {'data': data}
    response = requests.request(
        method='POST', headers=headers, url=model_uri, json=data_json)

    if response.status_code != 200:
        raise Exception(
             "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()

# Fonction qui permet d'afficher les résultats du  client
def Affiche_Defaillance(pred):
    print(f'Pour le client: {client_id}')
    if pred==0:
        print("proba=0: Non défaillant")
    else:
        print("proba=1: Défaillant")

# Chargement des données    
FILE_TEST_SET = 'resources/data/test_set.pickle'
    
# Import du dataframe des informations sur le prêt du client
with open(FILE_TEST_SET, 'rb') as df_test_set:
    test_set = pickle.load(df_test_set)

X_test_client = test_set[test_set['SK_ID_CURR'] == client_id]
X_test_pred = X_test_client.drop('SK_ID_CURR', axis=1)

# Conversion des données en format jason 
data = X_test_pred.to_json(orient='records')
data = json.loads(data)
pred = request_prediction(MLFLOW_URI, data)[0]
Affiche_Defaillance(pred)


# ====================================================================
# Interraction en locale ou en ligne - A partir d'un terminal
# ====================================================================
# En local:attention ici il faut copier d'abord data en format jason et le copier à la place de <data>
#curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d <data>

        
# En ligne
#curl http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/invocations  -H 'Content-Type: application/json' -d <data>
        
        
        
        
        
        
        
    
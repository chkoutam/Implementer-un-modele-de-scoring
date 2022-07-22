"""API : Dashboard de Crédit Score
Deploiement de l'API REST mlflow en local
Auteur: Check KOUTAME
Source: 
Local URL: http://127.0.0.1:5000
Lancement en local depuis une console anaconda prompt : 
    -cd C:\\Users\\koutame\\Desktop\\Formation Data science\\Projet 7\\Dashbord
    -python API.py
    -Dans le terminal:mlflow models serve -m mlflow_model/ 
"""

# ====================================================================
# Version : 0.0.1 - CRE CK 14/07/2022
# ====================================================================

__version__ = '0.0.1'

# ====================================================================
# Chargement des librairies
# ====================================================================

import pickle
import mlflow
import mlflow.sklearn
import os 


# Chargement du meilleur modèle
fic_best_model = 'resources/modele/best_model.pickle'
with open(fic_best_model, 'rb') as df_best_model:
    best_model = pickle.load(df_best_model)
best_model

# Signature du modèle : Ici  nous allons directement utiliser le meilleur modèle
# Voir notebook API pour utiliser la signature


# Sauvegarde du modèle
isdir = os.path.isdir("mlflow_model") 
if isdir: 
    print("le nom du modèle existe déjà, vous pouvez le déloyer")
else: 
    #mlflow.sklearn.save_model(best_model, 'mlflow_model')
    mlflow.sklearn.save_model(best_model, 'mlflow_model')

#Chargement du modèle
#mlflow.sklearn.log_model(best_model, "mlflow_model")
mlflow.sklearn.log_model(best_model, "mlflow_model")

#Affichage du nom du de l'exeriment utilisé
print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


# Dans le terminal: 
#mlflow models serve -m mlflow_model/
"""API : Dashboard de Crédit Score
Deploiement de l'API REST mlflow en local et en ligne sur aws
Auteur: Check KOUTAME
Local URL: http://127.0.0.1:5000
aws  : http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/invocations
Lancement en local depuis une console anaconda prompt : 
    -python API.py
    -Se placer dans le même repertoir que le package qui a été crée avec mlflow à l'ETAPE 1
    -Continuer avec l'ETAPE 2 
"""

# ====================================================================
# Version : 0.0.1 - CRE CK 14/07/2022
# Version : 0.0.2 - CRE CK 27/07/2022 - Ajout du deploiement sur le web
# ====================================================================

__version__ = '0.0.2'

# ====================================================================
# Chargement des librairies
# ====================================================================

import pickle
import mlflow
import mlflow.sklearn
import os 


# ====================================================================
# ETAPE1: Création du packages mlflows ainsi que les dependencis à installer
# ====================================================================

# Chargement du meilleur modèle
fic_best_model = 'resources/modele/best_model.pickle'
with open(fic_best_model, 'rb') as df_best_model:
    best_model = pickle.load(df_best_model)


    
# Sauvegarde du modèle avec les artifacts mlflows - étape très importante
isdir = os.path.isdir("mlflow_model") 

if isdir: 
    print("le nom du modèle existe déjà, vous pouvez le déloyer")
else: 
    mlflow.sklearn.save_model(best_model, 'mlflow_model')
    #Chargement du modèle pour la mise en ligne
    mlflow.sklearn.log_model(best_model, "mlflow_model")
    #Affichage du nom du de l'exeriment utilisé
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    
# ====================================================================
# ETAPE2: Deploiement du modèle mlflow
# ====================================================================
    
#Deploiement en local: http://127.0.0.1:5000

    # Deploiement en local dans le terminal: 
    # mlflow models serve -m mlflow_model/  

#Deploiement en ligne sur aws :http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/

    #Suivi des modifications sur le modèle
        #mlflow.set_tracking_uri("http://ec2-34-239-54-113.compute-1.amazonaws.com:5000/")
        #tracking_uri = mlflow.get_tracking_uri()
    # Deploiement en ligne sur  dans le compte aws:
    # >Le model est stocké sur un bucket S3://mlflow
    # >Créer une instance t2micro gratuite
        # Ajout un groupe de sécurité avec un port à 5000
    # >Créer un IAM donner les droits d'accès à notre ec2
    # >Sur un PowerShell
        #- cd ~/.ssh
        # - ssh -i "cle-ec2-modele_deploiement.pem" ubuntu@ec2-34-227-171-98.compute-1.amazonaws.com
        #  Install pipenv to run a virtual environment with mlflow (it's cleaner this way): pip install pipenv
        #sudo apt update
        #sudo apt install python3-pip
        #install pipenv
            #sudo pip3 install pipenv
            #sudo pip3 install virtualenv
            #export PATH=$PATH:/home/[your_user]/.local/bin/
    #install the dependencies to run the mlflow server
        #pipenv install mlflow
        #pipenv install awscli
        #pipenv install boto3
    #Deploiement
        #mlflow models serve -m mlflow_model/ -p 5000 -h 0.0.0.0
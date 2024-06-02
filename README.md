<!--suppress HtmlUnknownAnchorTarget, HtmlDeprecatedAttribute -->
<p style="text-align:center">
  <img src="img/logo_light.png#gh-light-mode-only" alt="logo-light" />
</p>


---
## Accès rapide
#### 1. [Objectifs](#objectifs)
#### 2. [Développement local](#dev)

---

<a name="objectifs"></a>
# Objectifs 
**Livrable P13 OC D-A Python : Mettre à l'échelle une application Django en utilisant une architecture modulaire**

_Testé sous Windows 10 - Python 3.11 - Django 3.0_

Plusieurs domaines du site **OC Lettings** ont été améliorés à partir du projet
[Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR) :

1) Réduction de la dette technique

   - Corriger les erreurs de linting
   - Corriger la pluralisation des noms de modèles dans le site d'administration


2) Refonte de l'architecture modulaire

   - Créer 3 applications *lettings*, *profiles* et *home* pour séparer les fonctionnalités de l'application
   - Convertir *oc_lettings_site* en projet Django
   - Développer une suite de tests


3) Ajout d'un pipeline CI/CD avec Gitlab

   1) *Compilation* : exécuter le linting et la suite de tests (sur toutes les branches)
   2) *Conteneurisation* : construire et push une image du site avec [Docker](https://www.docker.com) (si étape i. réussie, branche *master* uniquement)


4) Surveillance de l'application et suivi des erreurs via [Sentry](https://sentry.io/welcome/)

<a name="dev"></a>
# Développement local

## Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell 
exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

## Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://gitlab.com/sf5810217/oc_lettings.git`

## Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement virtuel `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python` (MacOS et Linux) ou `(Get-Command python).Path` (Windows)
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip` (MacOS et Linux) ou `(Get-Command pip).Path` (Windows)
- Pour désactiver l'environnement, `deactivate`

<a name="env"></a>
## Variables d'environnement : fichier *.env*
Pour générer un fichier *.env* à compléter, créer un fichier .env à la racine du projet.

Exemple de fichier *.env* généré :

```
DJANGO_SECRET_KEY=`votre clef secrète`
SENTRY_DSN=`votre sentry dsn`
DEBUG=True
ALLOWED_HOSTS=['*']
```

Vous pouvez modifier le fichier en ajoutant :
- l'URL du projet Sentry après `SENTRY_DSN=` (voir [Sentry](#sentry))
- `DEBUG=0` (*False*) ou `DEBUG=1` (*True*) (*False* par défaut)

## Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `pip install --requirement requirements.txt`
- Effectuer les migrations `python manage.py migrate`
- Charger les données initiales `python manage.py loaddata data.json`
- Lancer le serveur `python manage.py runserver`
- Aller sur http://127.0.0.1:8000/ dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

## Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `flake8`

## Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `python manage.py test`

## Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

## Site d'administration

- Aller sur http://127.0.0.1:8000/admin/
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

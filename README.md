# 🎬 Projet 3 – Analyse TMDB avec Pandas et Tkinter

## 📌 Objectif

Ce projet est une application graphique développée avec **Tkinter** permettant d'effectuer une **analyse de données** sur un fichier CSV (`tmdb-movies.csv`) contenant des informations sur des films.  
Il exploite la puissance de **Pandas** pour manipuler les données.

---

## 🗃️ Données utilisées

- 📁 Fichier CSV :  
  https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv

---

## ⚙️ Fonctionnalités

- 📂 Chargement d’un fichier CSV
- 🗓️ Tri des films par date de sortie décroissante
- ⭐ Filtrage des films ayant une note supérieure à 7.5
- 💰 Détection des films avec les revenus les plus hauts et les plus bas
- 🧮 Calcul du revenu total de tous les films
- 🏆 Top 10 des films les plus rentables (revenu – budget)
- 🎬 Identification du réalisateur ayant réalisé le plus de films
- 🎭 Acteur ayant joué dans le plus de films
- 📊 Statistiques sur les genres (nombre de films par genre)

---

## 🚀 Lancement de l’application

### 1. Cloner le projet

```bash
git clone https://github.com/NguyenChiThanhNice/PROJECT-3-DATA-ENGINEER/


2. Créer un environnement virtuel
python -m venv env
source env/bin/activate  # sous Linux/Mac
env\Scripts\activate     # sous Windows

3. Installer les dépendances
pip install pandas
✅ Tkinter est généralement déjà installé avec Python.

4. Lancer l'application
python3 NGUYEN_Chi_Thanh_LV1_Project_03.py
🗂️ Structure du projet
Fichier	Rôle
NGUYEN_Chi_Thanh_LV1_Project_03.py	Interface graphique + traitements Pandas
tmdb-movies.csv	Jeu de données utilisé
README.md	Documentation du projet

💡 Évolutions possibles
Ajouter des visualisations avec Matplotlib ou Seaborn

Exporter des rapports .xlsx ou .log

Ajouter des filtres avancés (par année, genre, etc.)

👤 Auteur
Chi Thanh NGUYEN
Étudiant en ingénierie de données
📧 Contact : ncthanh.agro@gmail.com / Tel. (+33)7 52 62 97 03

# Car Recommendation System 🚗

Un système de recommandation de voitures basé sur les caractéristiques techniques et le modèle du véhicule. L'utilisateur peut obtenir des suggestions de voitures similaires en fonction d’un modèle et de filtres facultatifs (type de carburant, prix maximum).

---

## 📁 Dataset
Le projet utilise le dataset **Vehicle Dataset from CarDekho** provenant de Kaggle :  
[https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)  

Colonnes importantes :
- `Make` : Marque du véhicule  
- `Model` : Modèle du véhicule  
- `Year` : Année de fabrication  
- `Fuel Type` : Type de carburant  
- `Transmission` : Type de boîte de vitesses  
- `Price` : Prix en ₹  
- `Engine`, `Max Power`, `Length`, `Width`, `Height`, `Seating Capacity`, `Fuel Tank Capacity` : Caractéristiques techniques

---

## 🛠️ Installation

1. Cloner le dépôt :
```bash
git clone <URL_DU_REPO>
cd <NOM_DU_PROJET>
Installer les dépendances :

bash
Copier le code
pip install streamlit pandas scikit-learn numpy
🚀 Lancer l’application
bash
Copier le code
streamlit run app.py
🔧 Utilisation
Entrez le modèle de voiture dans le champ prévu.

Appliquez les filtres facultatifs sur la barre latérale :

Type de carburant

Prix maximum

Nombre de recommandations à afficher

Cliquez sur Recommander pour voir les voitures similaires.

Exemple de sortie :

markdown
Copier le code
🚙 Voitures similaires à Amaze :
- Honda Amaze
  - 🛢️ Carburant : Petrol
  - ⚙️ Transmission : Manual
  - 📅 Année : 2019
  - 💰 Prix : 600000
⚙️ Fonctionnement du code
Chargement et nettoyage du dataset : suppression des textes dans les colonnes numériques et remplissage des valeurs manquantes.

Transformation des données : normalisation des nombres et encodage des catégories.

Calcul de similarité : cosine similarity entre toutes les voitures.

Recommandation : recherche des modèles similaires selon filtres.

Interface Streamlit : interaction utilisateur simple.

🔗 Liens utiles
Dataset Kaggle : Vehicle Dataset from CarDekho

Streamlit : https://streamlit.io
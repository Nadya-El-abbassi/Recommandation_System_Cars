# app.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# === 1. Charger le dataset ===
data = pd.read_csv("cars.csv")

# === 2. Nettoyage des colonnes numériques ===
def extract_number(value):
    """Extrait la première valeur numérique d'une chaîne (ex: '87 bhp @ 6000 rpm' -> 87)."""
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        match = re.search(r"[\d\.]+", value)
        if match:
            try:
                return float(match.group())
            except:
                return 0
    return 0

cols_to_clean = [
    'Price', 'Year', 'Kilometer', 'Engine', 'Max Power',
    'Length', 'Width', 'Height', 'Seating Capacity', 'Fuel Tank Capacity'
]

for col in cols_to_clean:
    if col in data.columns:
        data[col] = data[col].apply(extract_number)

# === 3. Nettoyage des colonnes catégorielles ===
categorical_features = ['Fuel Type', 'Transmission', 'Make', 'Drivetrain']

for col in categorical_features:
    if col in data.columns:
        data[col] = data[col].astype(str).fillna("Unknown")

# === 4. Remplir les valeurs manquantes ===
data = data.fillna(0)

# === 5. Définir les colonnes pour transformation ===
numeric_features = [
    'Price', 'Year', 'Kilometer', 'Engine', 'Max Power',
    'Length', 'Width', 'Height', 'Seating Capacity', 'Fuel Tank Capacity'
]

# === 6. Transformer les données ===
ct = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

X = ct.fit_transform(data)

# === 7. Calculer la similarité ===
similarity = cosine_similarity(X)

# === 8. Fonction de recommandation ===
def get_recommendations(model_name, n=5, fuel_filter=None, price_max=None):
    model_name = model_name.lower()
    matches = data[data['Model'].str.lower().str.contains(model_name, na=False)]
    
    if matches.empty:
        return []
    
    car_index = matches.index[0]
    distances = similarity[car_index]
    similar_indices = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1: n+1]

    recommended_cars = []
    for i in similar_indices:
        car = data.iloc[i[0]]
        if fuel_filter and car['Fuel Type'] != fuel_filter:
            continue
        if price_max and car['Price'] > price_max:
            continue
        recommended_cars.append(car)
    return recommended_cars

# === 9. Interface Streamlit ===
st.title(" Système de recommandation de voitures")
st.write("Trouvez des voitures similaires selon le modèle et vos préférences !")

model_input = st.text_input("Entrez le modèle de voiture :", "Amaze")

st.sidebar.header("Filtres facultatifs")
fuel_filter = st.sidebar.selectbox("Type de carburant", [None] + sorted(list(data['Fuel Type'].unique())))
price_max = st.sidebar.number_input("Prix maximum (en ₹)", min_value=0, value=0)
if price_max == 0:
    price_max = None

num_results = st.sidebar.slider("Nombre de recommandations", min_value=1, max_value=10, value=5)

if st.button("Recommander"):
    recommendations = get_recommendations(model_input, n=num_results, fuel_filter=fuel_filter, price_max=price_max)
    
    if not recommendations:
        st.warning("Aucune voiture trouvée correspondant à ce modèle et filtres.")
    else:
        st.subheader(f"🚙 Voitures similaires à **{model_input.capitalize()}** :")
        for car in recommendations:
            st.markdown(f"""
            **{car['Make']} {car['Model']}**
            - 🛢️ Carburant : {car['Fuel Type']}
            - ⚙️ Transmission : {car['Transmission']}
            - 📅 Année : {int(car['Year'])}
            - 💰 Prix : {int(car['Price'])}
            """)


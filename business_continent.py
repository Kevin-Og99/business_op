import streamlit as st
import pandas as pd

# Charger les données
df = pd.read_csv("Dataset of all public companies cleaned SQL (1).csv")
df = df.dropna(subset=['continent', 'sector', 'employees', 'revenues'])
df['employees'] = df['employees'].astype(int)
df['revenues'] = df['revenues'].astype(float)

st.title("💼 Simulateur de Revenu d'Investissement Digital")

continent = st.selectbox("Choisir un continent", df['continent'].unique())
sector = st.selectbox("Choisir un secteur", df[df['continent'] == continent]['sector'].unique())
employees = st.slider("Nombre d'employés", 10, 5000, 100)

# Calcul de la simulation
filtered = df[(df['continent'] == continent) & (df['sector'] == sector)]
avg_rev_per_emp = (filtered['revenues'] / filtered['employees']).mean()
simulated_revenue = round(avg_rev_per_emp * employees, 2)

st.metric("📊 Revenu estimé", f"{simulated_revenue:,.0f} $")

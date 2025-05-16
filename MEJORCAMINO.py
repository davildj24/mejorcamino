#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import networkx as nx
import pandas as pd

st.set_page_config(page_title="EXSA S.A. - Prototipo Matemáticas Discretas")

st.title("🧠 Prototipo - Matemáticas Discretas en Logística de explosivos")
st.markdown("Simulación de decisiones logísticas usando lógica proposicional, álgebra de Boole, relaciones binarias y teoría de grafos.")

# --- Sección 1: Lógica Proposicional y Álgebra de Boole ---
st.header("1️⃣ Validación de salida de camión (Lógica y Boole)")

permiso = st.checkbox("✅ Permiso de tránsito")
ruta_disponible = st.checkbox("✅ Ruta disponible")
carga = st.slider("📦 Carga (toneladas)", 0, 20, 5)
capacidad_max = 10

puede_salir = permiso and ruta_disponible and (carga <= capacidad_max)

st.write("**Resultado:**", "🟢 Puede salir" if puede_salir else "🔴 No puede salir")
st.code(f"Salida = Permiso ∧ RutaDisponible ∧ (Carga ≤ CapacidadMax) = {puede_salir}")

# --- Sección 2: Teoría de Grafos ---
st.header("3️⃣ Mapa de Rutas Logísticas - En minutos (Teoría de Grafos)")

G = nx.DiGraph()

# Nodos (Almacenes)
G.add_nodes_from(["A", "B", "C", "D", "E"])

# Aristas (Rutas con peso)
G.add_weighted_edges_from([
    ("A", "B", 60),
    ("A", "C", 20),
    ("C", "A", 20),
    ("C", "D", 40),
    ("D", "E", 30),
])

source = st.selectbox("📍 Selecciona el almacén de origen", G.nodes, index=0)
target = st.selectbox("🏁 Selecciona el almacén de destino", G.nodes, index=3)

try:
    path = nx.dijkstra_path(G, source=source, target=target)
    cost = nx.dijkstra_path_length(G, source=source, target=target)
    st.success(f"Ruta más corta: {' → '.join(path)} (Costo: {cost})")
except nx.NetworkXNoPath:
    st.error("No hay ruta disponible entre esos almacenes.")

# Mostrar grafo
st.subheader("🔍 Vista del grafo")
st.graphviz_chart("""
digraph G {
    A -> B [label="60"]
    A -> C [label="20"]
    C -> A [label="20"]
    B -> C [label="30"]
    C -> D [label="40"]
    D -> E [label="30"]
}
""")


# In[ ]:





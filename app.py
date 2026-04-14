import streamlit as st
import pandas as pd
import plotly.express as px

# configuración de página
st.set_page_config(
    page_title="Dashboard Videojuegos",
    page_icon="🎮",
    layout="wide"
)

# título
st.title("Analisis de ventas de videojuegos")
st.markdown("Esplora las ventas goblales de los videojuegos mas populares de la historia")

# cargar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("vgsales.csv")
    return df

df = cargar_datos()

# ── SIDEBAR — FILTROS ────────────────────────────────────────────────────────
st.sidebar.header("Filtros")

plataformas = sorted(df["Platform"].unique())
plataformas_sel = st.sidebar.multiselect(
    "Plataforma",
    options=plataformas,
    default=plataformas
)

generos = sorted(df["Genre"].dropna().unique())
generos_sel = st.sidebar.multiselect(
    "Género",
    options=generos,
    default=generos
)

año_min, año_max = int(df["Year"].min()), int(df["Year"].max())
rango_años = st.sidebar.slider(
    "Rango de años",
    min_value=año_min,
    max_value=año_max,
    value=(año_min, año_max)
)

# ── FILTRADO ─────────────────────────────────────────────────────────────────
df_filtrado = df[
    (df["Platform"].isin(plataformas_sel)) &
    (df["Genre"].isin(generos_sel)) &
    (df["Year"].between(rango_años[0], rango_años[1]))
]

# ── KPIs ─────────────────────────────────────────────────────────────────────
st.subheader("Resumen")
col1, col2, col3, col4 = st.columns(4)

col1.metric(" Total juegos", f"{len(df_filtrado):,}")
col2.metric(" Ventas globales (M)", f"{df_filtrado['Global_Sales'].sum():.1f}")

mejor_juego = df_filtrado.loc[df_filtrado["Global_Sales"].idxmax(), "Name"] if not df_filtrado.empty else "—"
col3.metric(" Juego #1", mejor_juego)

mejor_publisher = df_filtrado.groupby("Publisher")["Global_Sales"].sum().idxmax() if not df_filtrado.empty else "—"
col4.metric(" Publisher líder", mejor_publisher)

st.divider()

# ── TABLA ────────────────────────────────────────────────────────────────────
st.subheader("Dataset completo")
st.dataframe(df_filtrado)

# ── GRÁFICO 1: Top 10 Publishers ─────────────────────────────────────────────
st.subheader("Top 10 Publishers por ventas globales")

top_publishers = (
    df_filtrado.groupby("Publisher")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_publishers,
    x="Global_Sales",
    y="Publisher",
    orientation="h",
    color="Global_Sales",
    color_continuous_scale="Blues",
    labels={"Global_Sales": "Ventas (millones)", "Publisher": "Publisher"},
)
fig1.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ── GRÁFICO 2: Ventas por región ─────────────────────────────────────────────
st.subheader("Ventas por región")

regiones = {
    "Norteamérica": df_filtrado["NA_Sales"].sum(),
    "Europa": df_filtrado["EU_Sales"].sum(),
    "Japón": df_filtrado["JP_Sales"].sum(),
    "Otros": df_filtrado["Other_Sales"].sum(),
}
df_regiones = pd.DataFrame(list(regiones.items()), columns=["Región", "Ventas"])

fig2 = px.pie(
    df_regiones,
    names="Región",
    values="Ventas",
    color_discrete_sequence=px.colors.sequential.Blues_r,
    hole=0.4
)
st.plotly_chart(fig2, use_container_width=True)

st.divider()


# ── GRÁFICO 3: Evolución por año ─────────────────────────────────────────────
st.subheader("Evolución de ventas globales por año")

ventas_año = (
    df_filtrado.groupby("Year")["Global_Sales"]
    .sum()
    .reset_index()
    .sort_values("Year")
)

fig3 = px.line(
    ventas_año,
    x="Year",
    y="Global_Sales",
    markers=True,
    labels={"Global_Sales": "Ventas globales (M)", "Year": "Año"},
    color_discrete_sequence=["#1f77b4"]
)
fig3.update_traces(line_width=2.5)
st.plotly_chart(fig3, use_container_width=True)

st.divider()


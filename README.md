# Dashboard de Ventas de Videojuegos

Dashboard interactivo construido con Python y Streamlit para explorar las ventas globales de los videojuegos más populares de la historia.

## Funcionalidades

- Filtros interactivos por plataforma, género y rango de años
- KPIs con métricas resumen (total juegos, ventas globales, juego #1, publisher líder)
- Top 10 Publishers por ventas globales
- Distribución de ventas por región (Norteamérica, Europa, Japón, Otros)
- Evolución de ventas globales por año
- Tabla del dataset completo con filtros aplicados

##  Stack

- Python 3.13
- Streamlit
- Pandas
- Plotly Express

## Estructura

streamlit-app/
├── app.py          # Aplicación principal
├── vgsales.csv     # Dataset de ventas de videojuegos
└── README.md

## Cómo correr el proyecto

1. Clona el repositorio
git clone https://github.com/santyherrera12/dashboard-videojuegos
cd dashboard-videojuegos

2. Crea y activa el entorno virtual
python -m venv venv
venv\Scripts\activate

3. Instala las dependencias
pip install streamlit pandas plotly

4. Corre la app
streamlit run app.py

## Dataset

Video Game Sales — Kaggle
https://www.kaggle.com/datasets/gregorut/videogamesales

## Autor

**Santiago Herrera Tafur**  
Ingeniero de Sistemas | Máster en Big Data — Universidad Europea de Madrid  
[LinkedIn](https://www.linkedin.com/in/santiago-herrera-tafur-463887161) · [GitHub](https://github.com/santyherrera12)

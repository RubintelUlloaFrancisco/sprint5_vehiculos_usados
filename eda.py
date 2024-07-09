import streamlit as st
import pandas as pd
import io
from visualizations import *

def app():
    st.title("Análisis Exploratorio de Datos (EDA)")
    
    # Cargar datos
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Datos cargados exitosamente")
        
        # Análisis de datos básicos
        st.header("Análisis Básico de Datos")
        st.write("Descripción de los datos:")
        st.write(df.describe())
        st.write("Información de los datos:")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        
        # Seleccionar tipo de gráfico
        chart_type = st.selectbox(
            "Selecciona el tipo de gráfico",
            [
                "Gráfico de Barras", "Gráfico Circular (Pie)", "Gráfico de Líneas",
                "Histograma", "Box Plot (Diagrama Caja)", "Gráfico de Área",
                "Gráfico de Violin", "Gráfico de Dispersión", "Gráfico de Burbuja",
                "Heatmap (Mapa de calor)", "Análisis de Series Temporales", "Gráfico de Radar",
                "Gráfico de Densidad", "Gráfico de Gantt", "Gráficos de Venn",
                "Gráficos de Red", "Mapa de Árbol", "Gráfico de Densidad en 3D",
                "Gráfico de Coordenadas Paralelas", "PCA (Análisis de Componentes Principales)",
                "Agrupación de Datos (KMeans)", "Gráfico de Cascada", "Análisis de Pareto",
                "Gráfico de Dispersión en 3D", "Gráfico de Superficie", "Gráfico de Contorno en 3D"
            ]
        )

        if chart_type == "Gráfico de Barras":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_bar_chart(df, x_col, y_col)
        elif chart_type == "Gráfico Circular (Pie)":
            names = st.selectbox("Selecciona la columna de nombres", df.columns)
            values = st.selectbox("Selecciona la columna de valores", df.columns)
            plot_pie_chart(df, names, values)
        elif chart_type == "Gráfico de Líneas":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_line_chart(df, x_col, y_col)
        elif chart_type == "Histograma":
            x_col = st.selectbox("Selecciona la columna", df.columns)
            plot_histogram(df, x_col)
        elif chart_type == "Box Plot (Diagrama Caja)":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_box_plot(df, x_col, y_col)
        elif chart_type == "Gráfico de Área":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_area_chart(df, x_col, y_col)
        elif chart_type == "Gráfico de Violin":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_violin_plot(df, x_col, y_col)
        elif chart_type == "Gráfico de Dispersión":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_scatter_plot(df, x_col, y_col)
        elif chart_type == "Gráfico de Burbuja":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            size_col = st.selectbox("Selecciona la columna de tamaño", df.columns)
            plot_bubble_chart(df, x_col, y_col, size_col)
        elif chart_type == "Heatmap (Mapa de calor)":
            plot_heatmap(df)
        elif chart_type == "Análisis de Series Temporales":
            date_col = st.selectbox("Selecciona la columna de fecha", df.columns)
            value_col = st.selectbox("Selecciona la columna de valor", df.columns)
            plot_time_series(df, date_col, value_col)
        elif chart_type == "Gráfico de Radar":
            categories = st.multiselect("Selecciona las categorías", df.columns)
            values = st.multiselect("Selecciona los valores", df.columns)
            plot_radar_chart(df, categories, values)
        elif chart_type == "Gráfico de Densidad":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_density_chart(df, x_col, y_col)
        elif chart_type == "Gráfico de Gantt":
            task_col = st.selectbox("Selecciona la columna de tareas", df.columns)
            start_col = st.selectbox("Selecciona la columna de inicio", df.columns)
            end_col = st.selectbox("Selecciona la columna de fin", df.columns)
            plot_gantt_chart(df, task_col, start_col, end_col)
        elif chart_type == "Gráficos de Venn":
            sets = st.multiselect("Selecciona los conjuntos", df.columns)
            names = st.multiselect("Selecciona los nombres de los conjuntos", df.columns)
            plot_venn_chart(sets, names)
        elif chart_type == "Gráficos de Red":
            source_col = st.selectbox("Selecciona la columna de origen", df.columns)
            target_col = st.selectbox("Selecciona la columna de destino", df.columns)
            plot_network_graph(df, source_col, target_col)
        elif chart_type == "Mapa de Árbol":
            path = st.selectbox("Selecciona la ruta", df.columns)
            values = st.selectbox("Selecciona los valores", df.columns)
            plot_treemap(df, path, values)
        elif chart_type == "Gráfico de Densidad en 3D":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            z_col = st.selectbox("Selecciona la columna Z", df.columns)
            plot_3d_density_chart(df, x_col, y_col, z_col)
        elif chart_type == "Gráfico de Coordenadas Paralelas":
            dimensions = st.multiselect("Selecciona las dimensiones", df.columns)
            plot_parallel_coordinates(df, dimensions)
        elif chart_type == "PCA (Análisis de Componentes Principales)":
            n_components = st.slider("Selecciona el número de componentes", 2, len(df.columns))
            plot_pca(df, n_components)
        elif chart_type == "Agrupación de Datos (KMeans)":
            n_clusters = st.slider("Selecciona el número de clusters", 2, 10)
            plot_kmeans(df, n_clusters)
        elif chart_type == "Gráfico de Cascada":
            x_col = st.selectbox("Selecciona la columna X", df.columns)
            y_col = st.selectbox("Selecciona la columna Y", df.columns)
            plot_waterfall_chart(df, x_col, y_col)

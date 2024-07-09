import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import networkx as nx

# Sección de gráficos básicos
def plot_bar_chart(df, x_col, y_col):
    fig = px.bar(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_pie_chart(df, names, values):
    fig = px.pie(df, names=names, values=values)
    st.plotly_chart(fig)

def plot_line_chart(df, x_col, y_col):
    fig = px.line(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_histogram(df, x_col):
    fig = px.histogram(df, x=x_col)
    st.plotly_chart(fig)

def plot_box_plot(df, x_col, y_col):
    fig = px.box(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_area_chart(df, x_col, y_col):
    fig = px.area(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_violin_plot(df, x_col, y_col):
    fig = px.violin(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_scatter_plot(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_bubble_chart(df, x_col, y_col, size_col):
    fig = px.scatter(df, x=x_col, y=y_col, size=size_col)
    st.plotly_chart(fig)

# Sección de gráficos avanzados
def plot_heatmap(df):
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

def plot_time_series(df, date_col, value_col):
    df[date_col] = pd.to_datetime(df[date_col])
    fig = px.line(df, x=date_col, y=value_col)
    st.plotly_chart(fig)

def plot_radar_chart(df, categories, values):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))
    st.plotly_chart(fig)

def plot_density_chart(df, x_col, y_col):
    fig = px.density_contour(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

def plot_gantt_chart(df, task_col, start_col, end_col):
    fig = px.timeline(df, x_start=start_col, x_end=end_col, y=task_col)
    st.plotly_chart(fig)

def plot_venn_chart(sets, names):
    from matplotlib_venn import venn2, venn3
    if len(sets) == 2:
        venn2(sets, set_labels=names)
    elif len(sets) == 3:
        venn3(sets, set_labels=names)
    plt.show()
    st.pyplot()

def plot_network_graph(df, source_col, target_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=50, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
    st.pyplot()

def plot_treemap(df, path, values):
    fig = px.treemap(df, path=path, values=values)
    st.plotly_chart(fig)

def plot_3d_density_chart(df, x_col, y_col, z_col):
    fig = px.density_contour(df, x=x_col, y=y_col, z=z_col)
    st.plotly_chart(fig)

def plot_parallel_coordinates(df, dimensions):
    fig = px.parallel_coordinates(df, dimensions=dimensions)
    st.plotly_chart(fig)

def plot_pca(df, n_components):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df)
    fig = px.scatter_matrix(components, dimensions=range(n_components))
    st.plotly_chart(fig)

def plot_kmeans(df, n_clusters):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters)
    df['cluster'] = kmeans.fit_predict(df)
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], color='cluster')
    st.plotly_chart(fig)

def plot_waterfall_chart(df, x_col, y_col):
    fig = go.Figure(go.Waterfall(x=df[x_col], y=df[y_col]))
    st.plotly_chart(fig)

def plot_pareto_chart(df, x_col, y_col):
    df_sorted = df.sort_values(by=y_col, ascending=False)
    cumulative_sum = df_sorted[y_col].cumsum()
    cumulative_percentage = 100 * cumulative_sum / df[y_col].sum()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df_sorted[x_col], y=df_sorted[y_col], name='Count'), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_sorted[x_col], y=cumulative_percentage, name='Cumulative Percentage'), secondary_y=True)
    st.plotly_chart(fig)

def plot_3d_scatter(df, x_col, y_col, z_col):
    fig = px.scatter_3d(df, x=x_col, y=y_col, z=z_col)
    st.plotly_chart(fig)

def plot_surface_chart(df, x_col, y_col, z_col):
    fig = go.Figure(data=[go.Surface(z=df.pivot(index=y_col, columns=x_col, values=z_col).values)])
    st.plotly_chart(fig)

def plot_3d_contour(df, x_col, y_col, z_col):
    fig = go.Figure(data=[go.Contour(x=df[x_col], y=df[y_col], z=df[z_col])])
    st.plotly_chart(fig)

def plot_stacked_bar_chart(df, x_col, y_col, color_col):
    fig = px.bar(df, x=x_col, y=y_col, color=color_col)
    st.plotly_chart(fig)

def plot_sankey_chart(df, source_col, target_col, value_col):
    fig = px.sankey(df, node_color='blue', link_color='green', source=source_col, target=target_col, value=value_col)
    st.plotly_chart(fig)

def plot_stacked_density_chart(df, x_col, color_col):
    fig = px.density_contour(df, x=x_col, color=color_col)
    st.plotly_chart(fig)

def plot_scatter_matrix(df, dimensions):
    fig = px.scatter_matrix(df, dimensions=dimensions)
    st.plotly_chart(fig)

def plot_divided_network_graph(df, source_col, target_col, group_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    groups = df[group_col].unique()
    for group in groups:
        nodes = df[df[group_col] == group][source_col]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, label=group)
    nx.draw_networkx_edges(G, pos)
    st.pyplot()

def plot_3d_scatter_matrix(df, dimensions):
    fig = px.scatter_matrix(df, dimensions=dimensions)
    st.plotly_chart(fig)

def plot_divided_flow_network_graph(df, source_col, target_col, group_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    groups = df[group_col].unique()
    for group in groups:
        nodes = df[df[group_col] == group][source_col]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, label=group)
    nx.draw_networkx_edges(G, pos)
    st.pyplot()

def plot_smoothed_scatter(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, trendline="lowess")
    st.plotly_chart(fig)

def plot_3d_surface(df, x_col, y_col, z_col):
    fig = go.Figure(data=[go.Surface(z=df.pivot(index=y_col, columns=x_col, values=z_col).values)])
    st.plotly_chart(fig)

def plot_polar_chart(df, r_col, theta_col):
    fig = px.line_polar(df, r=r_col, theta=theta_col)
    st.plotly_chart(fig)

def plot_3d_parallel_coordinates(df, dimensions):
    fig = px.parallel_coordinates(df, dimensions=dimensions)
    st.plotly_chart(fig)

def plot_conditional_scatter(df, x_col, y_col, condition_col):
    fig = px.scatter(df, x=x_col, y=y_col, color=condition_col)
    st.plotly_chart(fig)

def plot_population_pyramid(df, age_col, population_col, gender_col):
    fig = px.bar(df, x=population_col, y=age_col, color=gender_col, orientation='h')
    st.plotly_chart(fig)

def plot_multi_axis_radar(df, categories, values):
    fig = go.Figure()
    for i in range(len(values)):
        fig.add_trace(go.Scatterpolar(r=values[i], theta=categories, fill='toself'))
    st.plotly_chart(fig)

def plot_stacked_violin(df, x_col, y_col, color_col):
    fig = px.violin(df, x=x_col, y=y_col, color=color_col, box=True, points="all")
    st.plotly_chart(fig)

def plot_colored_parallel_coordinates(df, dimensions, color_col):
    fig = px.parallel_coordinates(df, dimensions=dimensions, color=color_col)
    st.plotly_chart(fig)

def plot_colored_network_graph(df, source_col, target_col, color_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    colors = df[color_col].unique()
    for color in colors:
        nodes = df[df[color_col] == color][source_col]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color, label=color)
    nx.draw_networkx_edges(G, pos)
    st.pyplot()

def plot_star_scatter(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, symbol=y_col)
    st.plotly_chart(fig)

def plot_weighted_network_graph(df, source_col, target_col, weight_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col, edge_attr=weight_col)
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, weight_col)
    nx.draw(G, pos, with_labels=True, edge_color=list(weights.values()), edge_cmap=plt.cm.Blues)
    st.pyplot()

def plot_scatter_with_smoothing_line(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, trendline="lowess")
    st.plotly_chart(fig)

def plot_scatter_with_confidence_regions(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, error_y=y_col)
    st.plotly_chart(fig)

def plot_network_with_node_size(df, source_col, target_col, size_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    sizes = df[size_col].values * 100
    nx.draw(G, pos, with_labels=True, node_size=sizes)
    st.pyplot()

def plot_network_with_node_attributes(df, source_col, target_col, attribute_col):
    G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
    pos = nx.spring_layout(G)
    attributes = df[attribute_col].unique()
    for attribute in attributes:
        nodes = df[df[attribute_col] == attribute][source_col]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, label=attribute)
    nx.draw_networkx_edges(G, pos)
    st.pyplot()
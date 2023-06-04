import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from app.database.dataframe import create_dataframe
from app.services.dataset_regression import predict_model

st.set_option("deprecation.showPyplotGlobalUse", False)


def load_page():
    df = create_dataframe()

    st.header("Neuromorphic Computing and Supercomputers")

    st.subheader("Dataset Information")

    sns.scatterplot(x="humidity_dht", y="temperature_ext", data=df)

    plt.title("Relação humidity_dht x temperature_ext")
    st.pyplot()

    plt.figure(figsize=(10, 10))
    sns.heatmap(df.corr(), annot=True, cmap="crest")
    plt.title("Correlação Dados")
    st.pyplot()

    st.divider()

    st.subheader("Prediction Data")

    pred_temp_ext, pred_humidity = predict_model(df)

    st.success(f"Previsao da Temperatura Externa: {pred_temp_ext}")
    st.success(f"Previsao da Umidade: {pred_humidity}")

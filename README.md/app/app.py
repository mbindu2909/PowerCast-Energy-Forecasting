import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("PowerCast: Energy Consumption Forecasting")

uploaded_file = st.file_uploader("Upload Energy Dataset", type=["csv","txt"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, sep=";")

    st.write("Dataset Preview")
    st.write(data.head())

    data['Global_active_power'] = pd.to_numeric(
        data['Global_active_power'], errors='coerce'
    )

    fig, ax = plt.subplots()

    data['Global_active_power'].head(1000).plot(ax=ax)

    st.pyplot(fig)
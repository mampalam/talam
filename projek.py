import streamlit as st
import pandas as pd
import pickle

st.write("""
# Advertising Sale Prediction App

This app predicts the **Advertising Sale** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Newspaper = st.sidebar.slider('Newspaper', 0, 80, 50)
    TV = st.sidebar.slider('TV', 0, 250, 50)
    Radio = st.sidebar.slider('Radio', 0, 80, 50)
    data = {'Newspaper': Newspaper,
            'TV': TV,
            'Radio': Radio,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("ads.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

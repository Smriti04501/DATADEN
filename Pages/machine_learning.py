import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def app():
    st.markdown('''### Get the hint, don't leave the footprint!''')
    st.markdown('''We are already living in the era of climate change and losses. One of the major contibutors of greenhouse gases are the car engines. While the amount of CO2 released by cars also depends on fuel type and fuel efficiency, *the engine type of the car hs a very significant direct impact on the carbon emissions.*''')

    for i in range(2):
        st.write(' ')
    st.write('Select the engine size and get the amount of CO2 emitted by your engine: ')

    df = pd.read_csv(r'data/Cars_dataset_model.csv')
    X = df[['Engine_Size']]
    y = df[['CO2_Emissions']]

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=101)

    st.write(' ')
    engine_size = st.slider('Engine size:', 1.0, 8.4)  # The values are min and max

    reg = LinearRegression()
    reg.fit(X_train,y_train)
    y_predict = reg.predict([[engine_size]])

    st.write(f"CO2 Emissions: ", y_predict)





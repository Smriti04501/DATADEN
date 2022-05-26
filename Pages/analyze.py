from cmath import nan
from datetime import date
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from sys import prefix
import glob, os

def app():
    st.markdown('''###  Analyze your data!''')
    st.markdown('''**Analyze the columns of your dataset using *univariate and multivariate barplots, scatterplots and lineplots*.**''')

    uploaded_file = st.sidebar.file_uploader("Upload your file here:", type=['csv'])
    functions = ["Overview", "Plot (Univariate)", "Plot (Multivariate)", "Notemaker"]

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        def describe(data):
            global num_category, str_category
            num_category = [feature for feature in data.columns if data[feature].dtypes != "O"]
            str_category = [feature for feature in data.columns if data[feature].dtypes == "O"]
            column_with_null_values = data.columns[data.isnull().any()]
            return data.describe(), data.shape, data.columns, num_category, str_category, data.isnull().sum(), data.dtypes.astype(
                "str"), data.nunique(), str_category, column_with_null_values

        describe, shape, columns, num_category, str_category, null_values, dtypes, unique, str_category, column_with_null_values = describe(
            data)

        multi_function_selector = st.sidebar.multiselect("Explore the dataset: ",
                                                         functions)

        st.subheader("Dataset Preview")
        st.dataframe(data)
        for i in range(3):
            st.text(" ")

        columns = data.columns

        if "Overview" in multi_function_selector:
            st.subheader("Dataset Description")
            st.write(describe)
            for i in range(3):
                st.text(" ")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.text("Basic Information")
                st.write("Dataset Name")
                st.text(uploaded_file.name)

                st.write("Dataset Size(MB)")
                number = round((uploaded_file.size * 0.000977) * 0.000977, 2)
                st.write(number)

                st.write("Dataset Shape")
                st.write(shape)

            with col2:
                st.text("Dataset Columns")
                st.write(columns)

            with col3:
                st.text("Numeric Columns")
                st.dataframe(num_category)

            with col4:
                st.text("String Columns")
                st.dataframe(str_category)

            col5, col6, col7, col8 = st.columns(4)

            with col6:
                st.text("Columns Data-Type")
                st.dataframe(dtypes)

            with col7:
                st.text("Counted Unique Values")
                st.write(unique)

            with col5:
                st.write("Counted Null Values")
                st.dataframe(null_values)

        # =============================================================================================================================

        if "Plot (Univariate)" in multi_function_selector:

            multi_bar_plotting = st.sidebar.multiselect("Enter name or select the column which you want to plot: ",
                                                        str_category)
            for i in range(len(multi_bar_plotting)):
                column = multi_bar_plotting[i]
                st.markdown("#### Bar Plot for {} column".format(column))
                bar_plot = data[column].value_counts().reset_index().sort_values(by=column, ascending=False)
                st.bar_chart(bar_plot)

        # =======================================================================================================================================

        if "Plot (Multivariate)" in multi_function_selector:
            chart_select = st.sidebar.selectbox(label='Select the chart type',
                                                options=['Barplot', 'Scatterplot', 'Lineplot'])

            if chart_select == 'Barplot':
                st.sidebar.subheader('Enter queries to plot:')
                X_value = st.sidebar.selectbox('X axis', options=columns)
                Y_value = st.sidebar.selectbox('Y axis', options=columns)
                plot = px.bar(data_frame=data, x=X_value, y=Y_value)
                #plot.update_traces(marker_color='red')
                plot.update_layout(autosize=False, paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', width=500, height=600)
                st.plotly_chart(plot, use_container_width=True)

            if chart_select == 'Scatterplot':
                st.sidebar.subheader('Enter queries to plot:')
                X_value = st.sidebar.selectbox('X axis', options=columns)
                Y_value = st.sidebar.selectbox('Y axis', options=columns)
                plot = px.scatter(data_frame=data, x=X_value, y=Y_value)
                #plot.update_traces(marker=dict(color='red'))
                plot.update_layout(autosize=False, paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', width=500, height=600)
                st.plotly_chart(plot, use_container_width=True)

            if chart_select == 'Lineplot':
                st.sidebar.subheader('Enter queries to plot:')
                X_value = st.sidebar.selectbox('X axis', options=columns)
                Y_value = st.sidebar.selectbox('Y axis', options=columns)
                plot = px.line(data_frame=data, x=X_value, y=Y_value)
                #plot.update_traces(marker_color='red')
                plot.update_layout(autosize=False, paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', width=500, height=600)
                st.plotly_chart(plot, use_container_width=True)


        # =========================================================================================================================================

        if "Notemaker" in multi_function_selector:
            title_container = st.container()
            col1, col2, col3 = st.columns([50, 3, 22])
            image = Image.open('Pictures/Notemaker Illustration.png')
            with title_container:
                with col1:
                    st.subheader('Welcome to DataDen NoteMaker!')
                    st.write(
                        "DataDen NoteMaker helps you note down insights derived from analysis. Click on 'Download the note' to generate your note in text format to view offline.")
                    st.write(" ")
                    note = st.text_area('Take down points here:', height=300)
                    st.download_button('Download the note', note)
                with col2:
                    st.write(" ")
                with col3:
                    for i in range(6):
                        st.write(" ")
                    st.image(image, use_column_width=True)

    # =========================================================================================================================================

    #Use sample/example dataset to explore the website
    else:
        with open('data/Cars_dataset_model.csv', 'rb') as f:
            st.sidebar.download_button(
                label="Download Sample Data and Use It",
                data=f,
                file_name='Sample',
                help="Download sample data & use it to explore this web app."
            )



import plotly.express as px
import seaborn as sns
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def app():
    st.markdown('### Data Analysis Report')
    st.write('Get the detailed data analysis report of your dataset here.')

    uploaded_file = st.sidebar.file_uploader("Upload your file here:", type=['csv'])
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv

        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st_profile_report(pr)
        export = pr.to_html()
        st.download_button(label="Download Full Report", data=export, file_name='report.html')
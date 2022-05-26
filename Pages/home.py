import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns

def app():

    # Inserting and centre aligning logo
    image = Image.open('Pictures/Illustration1.png')

    st.markdown('''*DataDen* is a holistic one-stop solution for automotive businesses to analyze customer & company data through intuitive statistical & graphical reports. This user-friendly application is designed for better comprehension of data which can further be used to improvise the business models, enhance customer experience and take other major decisions to determine the future control points hence promote growth of the company.''')

    for i in range(9):
        st.write(" ")
    col1, col2, col3 = st.columns([70,3,27])
    with col1:
        st.write(
        """
        ### **What's in store**?
        - Display univariate and multivariate interactive plots for different features separately.
        - Generate the complete univariate data analysis report of data at once using the 'Report' feature.
        - Save interactive plots and/or the complete report generated after analysis for viewing offline.
        - Notemaker - Mark observations or notedown anything else during app usage and download it.
        - Let's C about Carbon- Check out the amount of CO2 emitted by a car by entering it's engine size.
        """)
        with col2:
            st.write(' ')
    with col3:
        st.image(image, width=350)
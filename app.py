import streamlit as st
from multipage import MultiPage
from PIL import Image
import plotly.express as px
import seaborn as sns
from Pages import home, analyze, report, machine_learning

app = MultiPage()

st.set_page_config(page_title='DataDen',layout='wide')
hide_menu_style='''
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)

image3 = Image.open('Pictures/Logo.png')
st.sidebar.image(image3, width=280)

st.sidebar.header('Get started!')

# Pages of the application here
app.add_page('Home', home.app)
app.add_page("Analyze", analyze.app)
app.add_page("Report", report.app)
app.add_page("Let's C about Carbon", machine_learning.app)

# The main app
app.run()
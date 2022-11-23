import streamlit as st
from utilities.standard_template import Page, get_info
from utilities.land import land_page
import analysis.preprocessing
import analysis.exploration
import warnings
 
warnings.filterwarnings("ignore")

# PAGE CONFIGURATION, CHANGE NAME AND ICON

st.set_page_config(layout="wide",page_title='AIViz')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.sidebar:
    choice = st.selectbox('Choose Algorithm Category',[
                                                " --- Choose --- ",
                                                "Clustering",
                                                "Classification",
                                                "Regression",
                                                "Data Exploration",
                                                "Data Preprocessing",
                                                "Others"
                                            ])
    get_info(choice)

if choice in ['Clustering', 'Classification', 'Regression']:
    Page(choice).render()
    
elif choice == 'Data Preprocessing':
    analysis.preprocessing.render()

elif choice == 'Data Exploration':
    analysis.exploration.render()

else:
    land_page()
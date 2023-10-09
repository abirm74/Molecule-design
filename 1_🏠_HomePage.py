import streamlit as st
import json
from streamlit_lottie import st_lottie
import toml
import requests
from PIL import Image
from streamlit.components.v1 import html
import base64


st.set_page_config(
    page_icon="🏠"

)
with open("logo.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.sidebar.markdown(
        f"""
        <div style="display:table;margin-top:-75%;margin-left:-2%;">
            <img src="data:image/png;base64,{data}" width="250" height="80">
        </div>
        """,
        unsafe_allow_html=True,
    )

# st.sidebar.image("logo.png", width=300)
# Set page title
# Logo image
image = Image.open('homeimage.png')

new_image = image.resize((800, 120))

st.image(new_image, use_column_width=True)

# Page title


# Set page header and sub-header



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_Project = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_pc68hnwh.json")

    
st_lottie(
    lottie_Project,
    speed=1,
    loop=True,
    width=True,
)
st.markdown(
    f'<div style="text-align: left;color: #101913;margin-top:-80px">A molecule design is an engineering/scientific construction that combines two or more components to generate a new biological agent.<br></br>Chemists employ technical expertise and do manual experimentation with the molecule design, introducing and removing functional groups – groupings of atoms and bonds with specified qualities. Even when using methods that anticipate ideal desired attributes, chemists must still perform each modification step manually. This can take a long time at each stage and yet not yield molecules with the appropriate characteristics.<br></br>A molecule is a group of two or more atoms that together create the smallest recognizable unit into which a pure material may be split while retaining its content and chemical characteristics. Molecules are identified by the element symbol and a subscript indicating the number of atoms.<br></br>When it comes to the pharmaceutical industry, molecule design is a valuable asset. Whenever a new cancer medicine is introduced, it marks the efforts of scientists who have spent years working behind the scenes to build and test a new molecule design.<br></br>The purpose of modifying a molecule design is to make the medicine as effective as feasible while remaining safe and simple to manufacture. This type of work involves the construction of each alternative molecular structure for testing, which is a time-consuming operation even if researchers only intend to tweak a single carbon atom, researchers must select among thousands of different possibilities to build this structure.</div>',
    unsafe_allow_html=True)


generation_url = "https://assets1.lottiefiles.com/packages/lf20_6k5szniz.json"
bioactivity_url = "https://assets7.lottiefiles.com/packages/lf20_dzu4dzms.json"

# Define the animation descriptions
generation_desc = "Molecule Generation descp"
bioactivity_desc = "Bioactivity Prediction desc"

# Create a two-column layout with the Lottie animations and descriptions
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st_lottie(load_lottieurl(generation_url), speed=1, width=300, height=300)
    st.markdown(
    f'<div style="text-align: left; margin-top: -20px;color: #101913;">you can use our application to generate new molecules. Try it ! </div>',
    unsafe_allow_html=True)
    


with col2:
    st_lottie(load_lottieurl(bioactivity_url), speed=1, width=300, height=300)
    st.markdown(
    f'<div style="text-align: left; margin-top: -20px;color: #101913;">you can use our application to predict the bioactivity of molecules. Try it ! </div>',
    unsafe_allow_html=True)
    # Define the button
    # Define the button
    # Define the button
    # Redirect to the target page in a new tab
# js = "window.open('http://localhost:8501/BioactivityPrediction?page=BioactivityPrediction')"
# html = '<button onclick="{}" target="_blank" style="cursor: pointer;background-color: #BAC6A9;color:white;border:None; margin-left:420px;">Go to BioactivityPrediction</button>'.format(js)
# st.components.v1.html(html, height=50)

# js = "window.open('http://localhost:8501/BioactivtyGeneration?page=BioactivityPrediction')"
# html = '<button onclick="{}" target="_blank" style="cursor: pointer;background-color: #BAC6A9;color:white;border:None; margin-right:420px;margin-: -200px;">Go to BioactivityGeneration</button>'.format(js)
# st.components.v1.html(html, height=50)
col4, col5 = st.columns([4,5])


with col4:
    js2 = "window.open('http://localhost:8501/Bioactivity_Prediction?page=BioactivityPrediction')"
    html2 = '<button onclick="{}" target="_blank" style="cursor: pointer;background-color: #BAC6A9;color:white;border:None;margin-left:50px;">Go to BioactivityGeneration</button>'.format(js2)
    st.components.v1.html(html2, height=50)
with col5:  
    js1 = "window.open('http://localhost:8501/Molecule_Generation?page=BioactivityPrediction')"
    html1 = '<button onclick="{}" target="_blank" style="cursor: pointer;background-color: #BAC6A9;color:white;border:None;margin-left:110px;">Go to BioactivityPrediction</button>'.format(js1)
    st.components.v1.html(html1, height=50)
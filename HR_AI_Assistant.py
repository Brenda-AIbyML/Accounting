# -*- coding: utf-8 -*-
"""
  Copyright 2024 AIBYML.COM

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
from PIL import Image
import streamlit_elements as Elements
from util.functions.path import get_file_path, get_dir_name, util_str, data_str, pages_str
from util.functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path
from pages.BrainStorm import discuss
from pages.Email_Construct import emailconstruct
from pages.DB_Query import query
from pages.Staff_HandBook import compliancy
from pages.Recruit_Assistant import recruitassist
#from pages.Subscription import subscription
#from pages.Training_AI import finetune
from util.Personal_AIA import AIA

img= Image.open(
  get_file_path(
      "aibyml_logo.ico",
      dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
      )
  )
  
#st.set_page_config(page_title="AIAgent", page_icon=img, layout="wide")

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):

        st.sidebar.markdown("## Shared AI Assistant")

        app = st.sidebar.selectbox(
            "Basic Human Resource Services", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()

def homepage():
    database_link_dict = {
        "ChatGPT for HR(2024)": "https://www.aihr.com/blog/chatgpt-for-hr-guide/",
    }

    for link_text, link_url in database_link_dict.items():
        create_st_button(link_text, link_url, st_col=st.sidebar)
    
left_topbar, right_topbar = st.columns([0.40,0.60])
        
left_topbar.markdown("#### [AIbyML](http://www.aibyml.com)")
    
tab1, tab2, tab3, tab4, tab5, tab6, = right_topbar.tabs([":blue[Home Page]", ":blue[Recruit]", ":blue[Staff HandBook]", ":blue[Email Reply]", ":blue[Staff Info Query]", ":blue[Brainstorm]",])

left_col, centre_left_col, centre_col, centre_right_col, right_col = st. columns([0.25,0.05,0.4,0.05,0.25])

img1 = Image.open(
    get_file_path(
        "AIA.png",
        dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
    )
)
right_col.markdown(" ")
right_col.markdown(" ")
right_col.image(img1, output_format="png", use_column_width ="auto")

centre_col.markdown("### AI Assistants enhance work performance")
centre_col.markdown("### Assist you better than a secretary")
centre_col.markdown("### Think of using AI Assistants to save cost")
centre_col.markdown("### AI Assistants owned by your company")

img2 = Image.open(
    get_file_path(
        "AIbyMLcom.png",
        dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
    )
)
left_col.markdown(" ")
left_col.markdown(" ")
left_col.image(img2, output_format="png", use_column_width = "auto")
st.markdown(":rainbow[No identifable record of users will be retained by AIbyML.com]")
if st.toggle("Want to know more about personal AI service", key=1001):
  with tab1:
        homepage()
        video_file = open('TalkingPhoto.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)    
  AIA()

#":blue[Employee Q&A]"
#":blue[Build Your AI]",
st.markdown('   ')
#st.markdown("<h1 style='text-align: center; color: purple;'>Human Resource AI Assistant</h1>", unsafe_allow_html=True)
st.markdown('   ')

with tab2:
    recruitassist()

with tab3:
    compliancy()
    
with tab4:
    emailconstruct()

with tab5:
    query()

with tab6:
    discuss()


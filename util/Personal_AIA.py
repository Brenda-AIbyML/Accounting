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
from util.functions.path import get_file_path, get_dir_name, util_str, data_str, pages_str
from util.functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path
from util.pages.Training_AI import finetune
from util.pages.Subscription import subscription
from util.pages.Terms_of_Services import tos
from util.pages.Privacy_Policy import privacy

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):

        st.sidebar.markdown("## Personal AI Assistant")

        app = st.sidebar.selectbox(
            "AIbyML.com Services", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()

def AIA():
        
    st.markdown("---")
    st.markdown("## Business Intelligence AI Assistant can")
    st.markdown("#### 👉🏼 Save your time to dig up clients")
    st.markdown("#### 👉🏼 Fast to develop plan fit your client")
    st.markdown("#### 👉🏼 Increase your capacity")
    st.markdown("#### 👉🏼 Tool for business development")
    
    st.markdown("---")

    left_col, right_col = st.columns(2)

    left_col.markdown('## Subscription to Personal AI Services:')
    left_col.markdown('#### ✦ Prompt Design or Fine Tune')
    left_col.markdown('#### ✦ on Your Cloud Account')
    left_col.markdown('#### ✦ on YOUR OWN HARDWARE')
    
    st.markdown("---")

    right_col.markdown('## Why Ours Not ChatGPT')
    right_col.markdown('#### ✦ AI with Your skills')
    right_col.markdown('#### ✦ No leak company data')
    right_col.markdown('#### ✦ Robust Cybersecurity protection')

    st.markdown("---")

    left_info_col, right_info_col = st.columns(2)

    left_info_col.markdown(
        f"""
        ### Contact us
        Please feel free to contact us with any issues, comments, or questions.

        ##### [Linkedin](www.linkedin.com/in/uxdatascienceaipolicy)
        - Email:  <admin@aibyml.com>
        - GitHub: https://github.com/AIBIZSERVICE

        """,
        unsafe_allow_html=True,
    )

    right_info_col.markdown(
        """
        ### Subscription Fee
        
        - Free one-time setup fee of US$50 (not including hardware)
        - Free first 2 monthly fee of US$30 (much cheaper than hire an HR officer)
        - Including building your AI and future added features
        - Including Cloud instance service and US$10 Paid LLM Services
        
        """
    )

    right_info_col.markdown(
        """
        ### License
        Apache License 2.0
        """
    )

    app = MultiApp()

    app.add_app("Training Your AI", finetune)
    app.add_app("Subscribe Personal AI", subscription)
    app.add_app("Privacy Policy", privacy)
    app.add_app("Terms of Services", tos)

    app.run()

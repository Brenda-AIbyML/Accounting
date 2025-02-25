# -*- coding: utf-8 -*-
"""
  Copyright 2022 Mitchell Isaac Parker

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

import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from pages.recruit.HRAIA_utils import *
import uuid
from util.functions.path import pages_str, data_str, get_file_path
from util.functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path


def recruitassist():

    #Creating Unique ID

    if 'unique_id' not in st.session_state:
        st.session_state['unique_id'] ='Office Admin'
    
    load_dotenv()
    
    st.title("Help Recruit...🕵️‍♂️ ")
    st.markdown("#### :rainbow[I can help you screening the applicant's resume]")
    
    st.session_state.prompt_history = []
    st.session_state.df = None
    
    left_col, right_col = st.columns([3, 1])
    
    job_description = left_col.text_area("👈🏼 Upload 'RESUMES' at the sidebar ", placeholder = "Please paste the 'JOB DESCRIPTION' here...", key="1")
    
    document_count = right_col.slider("Number of 'RESUMES' are extracted", 2, 30, 4)
    
    # Upload the Resumes (pdf files)
    
    pdf = st.file_uploader("Upload resumes here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

    submit=st.button("Help me to filter out right candidates")

    if submit:
        with st.spinner('Wait for it...'):
            st.write("Your unique ID")
            
            #Creating a unique ID, so that we can use to query and get only the user uploaded documents from PINECONE vector store
            #st.session_state['unique_id']=uuid.uuid4().hex
            st.write(st.session_state['unique_id'])            
            
            #Create a documents list out of all the user uploaded pdf files
            final_docs_list=create_docs(pdf,st.session_state['unique_id'])

            docs = split_docs(final_docs_list)
            
            #Displaying the count of resumes that have been uploaded
            st.write("*Resumes uploaded* :"+str(len(docs)))
            
            #Create embeddings instance
            embeddings=create_embeddings_load_data()

            #Push data to Vector Store
            db=push_to_store(embeddings,docs)

            #Fecth relavant documents from Vector Store
            relavant_docs=get_similar_docs(job_description,document_count,db, embeddings,st.session_state['unique_id'])

            #st.write(relavant_docs)

            #Introducing a line separator
            st.write(":heavy_minus_sign:" * 30)

            #For each item in relavant docs - we are displaying some info of it on the UI
            for item in range(len(relavant_docs)):
                
                st.subheader("👉 "+str(item+1))

                #Displaying Filepath
                st.write("**File** : "+relavant_docs[item].metadata['name'])

                #Introducing Expander feature
                with st.expander('Show me 👀'): 
                    #Gets the summary of the current item using 'get_summary' function that we have created which uses LLM & Langchain chain
                    summary = get_summary(relavant_docs[item])
                    st.write("**Summary** : "+summary)

        st.success("Hope I was able to save your time❤️")

if __name__ == "__main__":
  recruitassist()



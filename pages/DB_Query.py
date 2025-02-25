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
        
    reference: https://python.langchain.com/docs/use_cases/csv#sandboxed-code-execution

"""
import streamlit as st
import getpass
import os
import re
import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

def query():
  st.title("Staff File Enquery")
  if os.path.exists('titanic.db'):
    os.remove('titanic.db')
  if os.path.exists('myfile.db'):
    os.remove('myfile.db')
  st.session_state.openai_key = os.environ["OPENAI_API_KEY"]

  
  # Using LangSmith is recommended but not required. Uncomment below lines to use.
  # os.environ["LANGCHAIN_TRACING_V2"] = "true"
  # os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
  # st.write("please input api key in the system")
  if st.toggle("Use the default titanic data file to experiment with the AI services", key =702):
      
    df = pd.read_csv("titanic.csv")
    engine = create_engine("sqlite:///titanic.db")
    df.to_sql("titanic", engine, index=False)
    st.write("number of observations ", df.shape[0])
    st.write("the dataset data variable name: ", df.columns.tolist())
    db = SQLDatabase(engine=engine)
  
    # DB name and list of details
    st.write("SQLITE FILE NAME:: ", db.get_usable_table_names())
    db.run("SELECT * FROM titanic WHERE Age < 2;")
  
    # Create a SQL agent to interact with DB
    # Use the agent_executor to generate the code in sqlite to get the result
  
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
    inquery_input = st.text_area('Enter your inquiry in English about the data file', height=100, key=700, placeholder = "e.g. what's the average age of survivors")
    st.write(agent_executor.invoke({"input": inquery_input}))
  
    if st.button("Clear your sqlite file 'titanic' before upload your data", key = 703):
      os.remove("titanic.db")
  else:
    df = st.file_uploader("Upload a csv or xlsx format staff file", type=['csv','xlsx'], accept_multiple_files=False, key=701)
    if df is not None:
    # create sqlite dataset
      df2 = pd.read_csv(df)
      engines = create_engine("sqlite:///myfile.db")
      df2.to_sql("myfile", engines, index=False)
      st.write("number of observations: ", df2.shape[0])
      st.write("the dataset data variable names: ", df2.columns.tolist())
      db2 = SQLDatabase(engine=engines)
    
      # DB name and list of details
      st.write("SQLITE FILE NAME: ", db2.get_usable_table_names())
    
      # Create a SQL agent to interact with DB
      # Use the agent_executor to generate the code in sqlite to get the result
    
      llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
      agent_executor = create_sql_agent(llm, db=db2, agent_type="openai-tools", verbose=True)
      inquery_input = st.text_area('Enter your inquiry in English about a category of staff or any individual staff', height=100, key=600, placeholder = "e.g. what's the average age of salary")
      st.write(agent_executor.invoke({"input": inquery_input}))
    
      st.write("Use multi csv files for enquery, please subscribe to the personal AI services")
      if st.button("Clear your sqlite file before leave", key = 704):
        os.remove('myfile.db')

if __name__ == "__main__":
  query()    

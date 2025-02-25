import streamlit as st
from langchain.agents.agent_toolkits import GmailToolkit
from langchain.prompts import PromptTemplate
#from langchain.llms import CTransformers
#from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
#from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType,initialize_agent
import smtplib
import ssl
import os

# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main#Function to get the response back

def getLLMResponse(email_topic,email_style):
        
    #llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',config={'max_new_tokens': 256,'temperature': 0.01})
    llm =  ChatOpenAI(temperature=.9, model="gpt-3.5-turbo-0125")    

    # Define a simple prompt template as a Python string
   
    #Template for building the PROMPT Input Variables
    multiple_input_prompt = PromptTemplate(
            input_variables=["topic", "style"], template = "Write an email with {style} style and includes topic:{topic}."
    )

    #Creating the final PROMPT
    prompt = multiple_input_prompt.format(
            style=email_style,
            topic=email_topic,
    )    
    
    response = llm.predict(text=prompt) 
    return response

def getLLMResponseDetail(email_topic,email_sender,email_recipient,email_style):
    llm =  ChatOpenAI(temperature=.9, model="gpt-3.5-turbo-0125")  

    email_template = f"""\
        Subject: Write an email with {style} style and include topic: {topic}.
        
        Sender: {sender}
        Recipient: {recipient}
        
       Yours sincerely
       {sender}
        """
    multiple_input_prompt = PromptTemplate(
        input_variables=["style", "topic", "sender", "recipient"], template = email_template
    )        
    prompt = multiple_input_prompt.format(
        style=email_style,
        topic=email_topic,
        sender=email_sender,
        recipient=email_receipient
    )   
    response = llm.predict(text=prompt) 
    return response

def emailconstruct():

    st.title("Email Generation...✉️ ")
    st.markdown("#### Give me some instruction, I can construct a personal email for you.")
    form_input = st.text_area('Enter the email topic', height=100, placeholder="email admin@aibyml.com sought which AI fits your need", key=101)
    if form_input is not None: 
        if st.button("Choose the style of the Email", key = 102):
           email_style = st.selectbox('Writing Style', ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'), index=0, key = 4)
        else:
           email_style = "Neutral"
        content = getLLMResponse(form_input,email_style)
        st.write("Just copy the response: to your email account")
        if content is not None:
            st.write(content)    
   
if __name__ == "__main__":
  emailconstruct()

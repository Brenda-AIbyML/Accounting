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

import pandas as pd

import streamlit as st


def finetune():
    
    st.markdown("## Training Your AI Assistant")

    st.write("---")
    
    with st.sidebar:
        video_file = open('TalkingPhoto_PAI.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    
    st.markdown("#### Train an AI, follow these steps:")

    st.write("- Prepare your data: You need to prepare a diverse set of demonstration conversations that are similar to the conversations you will ask your AI to respond in actual situation. Each example in the dataset should be a conversation in the same prompt format. One can pay an one time fee to [AIbyML.com](http://www.aibyml.com) to set up for your company either in cloud or in your standalone AI device")

    st.write("- Create a fine-tuning job: You can create a fine-tuning job through API including in the setup services")

    st.write("- Monitor the job: You can monitor the status of the  fine-tuning job, and cancel a job if necessary. [AIbyML.com](http://www.aibyml.com) has the service in offer")

    st.write("- Use the fine-tuned model: Once the job has succeeded, you can use the fine-tuned model by specifying it as a parameter in the corresponding API.")

    st.write("- Analyze your fine-tuned model: [AIbyML.com](http://www.aibyml.com) provides training metrics computed over the course of training. You can also generate samples from both the base model and the fine-tuned model on a test set, and compare the samples side by side.")

    st.write("- Iterate on data quality and quantity: If the results from a fine-tuning job are not as expected, consider adjusting the training dataset. [AIbyML.com](http://www.aibyml.com) provide consultancy services to assist you to improve the result")

if __name__ == "__main__":
   finetune()

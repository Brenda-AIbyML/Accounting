# HResourceAIA

This is a prototype on Accounting Artificial Intelligence Assistant
It is a good practise to create a virtual environment to experiment the code
At terminal > python3 -V (check python3 verison)
> python3 -m venv ~/Accounting
> (no error means virtual environment been created)

Step 0: activate the virtual environment
> source ~/Accounting/bin/activate
(Accounting) ...> cd ~/Accounting (succeed and then go to the ~/Accounting directory)
 
Step 1: RUN > pip install -r requirements.txt

Step 2: echo all keys in the os environment
>  echo "export OPENAI_API_KEY='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'" >> ~/.zsh
source ~/.zsh

Step 3: RUN > python3 -m streamlit run HR_AI_Assitant.py

# Accounting Assistant Application

This application is a tool for accounting students and professionals to interact with AI models for accounting studies, assignment creation, and document analysis.

It is a good practise to create a virtual environment to experiment the code At terminal > python3 -V (check python3 verison)

## Virtual Environment

python3 -m venv ~/Accounting (no error means virtual environment been created)

Step 0: activate the virtual environment

source ~/Accounting/bin/activate

(Accounting) ...> cd ~/Accounting (succeed and then go to the ~/Accounting directory)

## Project Structure

The project has been refactored to separate the processing logic from the user interface:

- `proc_mode.py`: Contains all the processing functions, utilities, and logic
- `ACApp_v1_modifed.py`: Contains the user interface and application flow

## Features

- **Simple Chat**: Basic conversational interface with the AI model
- **Advanced Chat**: Advanced conversational interface with additional model parameters
- **Reading Q&A**: Upload accounting documents and ask questions about them
- **Assignment Assistant**: Guided workflow for creating accounting assignments:
  - Planning stage for outlining assignment structure
  - Drafting stage for creating the content
  - Critique stage for receiving feedback
  - Revision process for improving the assignment

## Setup Instructions

1. **Install Required Packages**

Step 1: RUN > pip install -r requirements.txt

Step 2: echo all keys in the os environment (copy #"..." in .env) on teminal > (push return, if no error come out, it is ok)

OR

   ```bash
   pip install streamlit langchain-community langchain ollama numpy pandas matplotlib wordcloud
   ```

2. **Start Ollama Server**
   The application uses Ollama as the backend for AI models. Make sure Ollama is installed and running.

3. **Image Setup (Optional)**
   For the full visual experience, create an 'images' folder and add:
   - Nineveh.jpg
   - divinity.png

4. **Run the Application**
   ```bash
   streamlit run acapp.py
   ```

## Working with the Application

### Simple and Advanced Chat

- Choose a model from the dropdown in the sidebar
- In Advanced Chat, adjust temperature and top-p settings
- Type your accounting questions in the chat input

### Financial Accounting Report or Cost Accounting Report Q&A

1. Upload accounting reports (PDF, DOCX, TXT)
2. Wait for processing to complete
3. Ask questions about the uploaded reports
4. View document analysis including word cloud and statistics

### Assignment Assistant

1. Enter assignment details (topic, area, academic level, length, tone)
2. Create an assignment plan
3. Edit or refine the plan as needed
4. Generate a draft based on the plan
5. Request critique of the draft
6. Revise the draft based on critique (up to 5 revisions)
7. Finalize and download the completed assignment

## Folders Created by the Application

- `draftplan`: Stores saved assignment plans
- `draftwriting`: Stores saved assignment drafts

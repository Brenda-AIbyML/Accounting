import streamlit as st
import os
from proc_mode import *

# Set page configuration
st.set_page_config(
    page_title="Assistant to Accounting Studies",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create a directory for the images if it doesn't exist
image_dir = "images"
os.makedirs(image_dir, exist_ok=True)

# Paths to the image files
nineveh_path = os.path.join(image_dir, "Nineveh.jpg")
bible_path = os.path.join(image_dir, "divinity.png")

# Check if images exist, if not create placeholder text
nineveh_exists = os.path.exists(nineveh_path)
bible_exists = os.path.exists(bible_path)

if nineveh_exists and bible_exists:
    # Apply background image styles
    add_bg_from_local(nineveh_path, ".nineveh-bg")
    add_bg_from_local(bible_path, ".bible-bg")

# Custom CSS for styling
# Add CSS styling for the UI
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #1E3A8A;
    }
    .accounting-subtitle {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #4B5563;
    }
    .parameter-info {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .parameter-title {
        font-weight: bold;
        color: #1E3A8A;
    }
    .chat-area {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .stChatMessage {
        background-color: white !important;
    }
    .document-summary {
        background-color: rgba(240, 240, 245, 0.9);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #1E3A8A;
        margin: 10px 0;
        font-size: 0.95rem;
    }
    .document-list {
        margin-top: 15px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 5px;
    }
    .assignment-area {
        background-color: rgba(245, 245, 250, 0.9);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #4B5563;
        margin: 15px 0;
    }
    .plan-section {
        background-color: rgba(235, 245, 255, 0.9);
        padding: 12px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .draft-section {
        background-color: rgba(235, 255, 240, 0.9);
        padding: 12px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .critique-section {
        background-color: rgba(255, 245, 235, 0.9);
        padding: 12px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stage-indicator {
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    .revision-indicator {
        font-size: 0.8rem;
        color: #4B5563;
        text-align: right;
    }
    .plan-editor {
        background-color: rgba(240, 245, 250, 0.95);
        border: 1px solid #c0c0c0;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .plan-actions {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }
    .saved-plan-item {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 5px;
        border-left: 3px solid #1E3A8A;
        margin-bottom: 8px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .saved-plan-item:hover {
        background-color: rgba(235, 245, 255, 0.9);
    }
    .plan-timestamp {
        font-size: 0.8rem;
        color: #6B7280;
        margin-top: 3px;
    }
    .plan-selected {
        background-color: rgba(220, 235, 255, 0.9);
        border-left: 3px solid #1E40AF;
    }
    .plan-load-section {
        background-color: rgba(245, 245, 250, 0.9);
        padding: 12px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px dashed #c0c0c0;
    }
    .editor-header {
        font-weight: bold;
        margin-bottom: 8px;
        color: #1E3A8A;
    }
    .stTextArea > div {
        border-radius: 8px;
        border-color: #c0c0c0;
    }
    .primary-button {
        background-color: #1E3A8A;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .secondary-button {
        background-color: #E5E7EB;
        color: #1F2937;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .file-list {
        max-height: 300px;
        overflow-y: auto;
        margin-top: 10px;
        padding-right: 10px;
    }

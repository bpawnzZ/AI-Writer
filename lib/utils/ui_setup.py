import os
import typing
import streamlit as st
from typing import Optional

from .file_processor import load_image
from .content_generators import content_planning_tools, ai_writers
from .alwrity_utils import ai_agents_team, ai_social_writer
from .seo_tools import ai_seo_tools


def setup_ui() -> None:
    """
    Sets up the Streamlit UI with custom CSS and logo.
    
    Handles potential file loading errors and provides fallback UI configuration.
    """
    try:
        css_file_path = os.path.join('lib', 'workspace', 'alwrity_ui_styling.css')
        with open(css_file_path, 'r', encoding='utf-8') as f:
            custom_css = f.read()
        st.set_page_config(page_title="Alwrity", page_icon="🚀", layout="wide")
        st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found. Using default Streamlit styling.")
        st.set_page_config(page_title="Alwrity", page_icon="🚀", layout="wide")
    except Exception as err:
        st.error(f"Unexpected error in UI setup: {err}")

    try:
        image_base64 = load_image("lib/workspace/alwrity_logo.png")
        st.markdown(f"""
        <div class='main-header'>
            <img src='data:image/png;base64,{image_base64}' alt='Alwrity Logo' style='height: 50px; margin-right: 10px; vertical-align: middle;'>
            Welcome to Alwrity!
        </div>
        """, unsafe_allow_html=True)
    except Exception as err:
        st.error(f"Could not load logo: {err}")
        st.title("Alwrity")


def setup_tabs() -> None:
    """
    Sets up the main tabs in the Streamlit app with error handling.
    """
    try:
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            ["📅Content Planning", " 📝🤖AI Writers", "🤝🤖Agents Teams", "🛠️🔍AI SEO tools", "📱AI Social Tools", " 💬Ask Alwrity"])
        
        with tab1:
            content_planning_tools()

        with tab2:
            ai_writers()

        with tab3:
            ai_agents_team()

        with tab4:
            ai_seo_tools()

        with tab5:
            ai_social_writer()

        with tab6:
            st.subheader("Chat with your Data, Chat with any Data.. COMING SOON !")
            st.markdown("Create a collection by uploading files (PDF, MD, CSV, etc), or crawl a data source (Websites, more sources coming soon.")
            st.markdown("One can ask/chat, summarize and do semantic search over the uploaded data")
    except Exception as err:
        st.error(f"Error setting up tabs: {err}")

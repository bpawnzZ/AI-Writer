import streamlit as st
import os
import json
import base64
from datetime import datetime

from lib.utils.config_manager import save_config
from lib.utils.ui_setup import setup_ui, setup_tabs  # Combined imports
from lib.utils.api_key_manager import check_all_api_keys
from dotenv import load_dotenv
from lib.utils.content_generators import ai_writers, content_planning_tools, blog_from_keyword, story_input_section, essay_writer, ai_news_writer, ai_finance_ta_writer, write_ai_prod_desc, do_web_research, competitor_analysis, ai_agents_content_planner
from lib.utils.seo_tools import ai_seo_tools
from lib.utils.alwrity_utils import ai_agents_team, ai_social_writer
from lib.utils.file_processor import load_image, read_prompts, write_prompts
from lib.utils.voice_processing import record_voice

# Rest of the file remains the same...

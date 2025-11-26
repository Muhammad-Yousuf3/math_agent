import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_KEY = os.getenv("GEMINI_API_KEY")

# We use the OpenAI compatible endpoint for Gemini
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME = "gemini-2.5-flash"

# System instructions for the math agent
SYSTEM_PROMPT = """You are the world's best math problem solver. 
You break down problems into step-by-step logical parts.
You always verify your calculations.
You are helpful, precise, and encouraging.
When appropriate, use Python code to calculate complex results to ensure accuracy.
"""

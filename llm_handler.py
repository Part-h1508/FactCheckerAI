# imports
import google.generativeai as genai
import os
from dotenv import load_dotenv

# load the env file
load_dotenv()

# get api key
api_key = os.getenv("GEMINI_API_KEY")

# simple check
if api_key is None:
    print("API key not found, check .env file")

# configure model
genai.configure(api_key=api_key)

# using flash model (fast + free tier friendly)
model = genai.GenerativeModel("gemini-2.0-flash")

# function to send prompt to model
def analyze(prompt):

    response = model.generate_content(prompt)

    return response.text
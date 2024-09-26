import google.generativeai as genai

import os

# Manually set the API key in the script
os.environ["GEMINI_API_KEY"] = "AIzaSyDasEWGvHbC8AINZAsNZOQBtgaAom17A2Q"  # Replace with your actual API key
print(os.getenv("GEMINI_API_KEY"))  # This should now print the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)
config = types.GenerateContentConfig(
    system_instruction="Ты - дружелюбный ментор по программированию для детей. Объясняй всё на примерах из Minecraft или Roblox. Пиши коротко."
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Объясни, что такое переменная в программировании.",
    config=config
)

print(response.text)
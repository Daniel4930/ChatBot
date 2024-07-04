import google.generativeai as genai
import os

def start_model():
    genai.configure(api_key=os.getenv("GEMINI_APIKEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat()
    return chat

def chatting(chat_session, user_prompt):
    response = chat_session.send_message(user_prompt)
    return response.text
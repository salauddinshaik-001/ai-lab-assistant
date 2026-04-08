import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# Function with memory support
def get_response(user_input, chat_history):
    try:
        # Build conversation context
        history_text = ""
        for role, msg in chat_history:
            history_text += f"{role}: {msg}\n"

        prompt = f"""
You are an AI Lab Assistant for a Computer Science student.

Conversation so far:
{history_text}

Student: {user_input}
Assistant:
"""

        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"
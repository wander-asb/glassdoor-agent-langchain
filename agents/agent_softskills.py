from langchain_together import ChatTogether
from prompts.prompt_softskills import prompt_softskills
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
model = os.getenv("MODEL_SELECTION")

llm = ChatTogether(model=model, together_api_key=api_key)

def agent_softskills(summary):
    print("Extraindo Soft Skills a partir do Agente Especialista Tech...\n")
    response = (prompt_softskills | llm).invoke({"summary": summary})
    return response.content

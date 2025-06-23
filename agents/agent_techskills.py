from langchain_together import ChatTogether
from prompts.prompt_techskills import prompt_techskills
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
model = os.getenv("MODEL_SELECTION")

llm = ChatTogether(model=model, together_api_key=api_key)

def agent_techskills(summary):
    print("Extraindo Tech Skills a partir do Agente Especialista de SoftSkills\n")
    response = (prompt_techskills | llm).invoke({"summary": summary})
    return response.content

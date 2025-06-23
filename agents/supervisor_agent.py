from langchain_together import ChatTogether
from prompts.prompt_diagnostico import prompt_diagnostico
from dotenv import load_dotenv
from services.linkedin_service import get_jobs
import os

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
model = os.getenv("MODEL_SELECTION")


llm = ChatTogether(model=model, together_api_key=api_key)

def supervisor_agent(job_title):
    print("🔍 Buscando vagas no Glassdoor...\n")
    job_descriptions = get_jobs(job_title)

    combined_text = "\n\n---\n\n".join(job_descriptions)

    print("Gerando resumo consolidado das vagas...\n")
    response = (prompt_diagnostico | llm).invoke({
        "job_descriptions": combined_text,
        "job_title": job_title
    })

    return response.content

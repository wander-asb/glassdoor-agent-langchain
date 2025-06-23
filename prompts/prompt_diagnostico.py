from langchain_core.prompts import ChatPromptTemplate

prompt_diagnostico = ChatPromptTemplate.from_template(
    """
    Você é um analista de vagas de emprego. Abaixo estão as descrições das 10 primeiras vagas para a posição de {job_title} no Glassdoor:
    
    {job_descriptions}

    Seja objetivo e liste as principais informações que são comuns entre as vagas. Não adicione texto fora do JSON.
    """
)

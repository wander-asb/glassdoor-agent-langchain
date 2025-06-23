from langchain_core.prompts import ChatPromptTemplate

prompt_techskills = ChatPromptTemplate.from_template(
    """
    Você é um especialista em mercado de tecnologia.

    Com base estritamente nas descrições de vagas recentes e requisitos apresentados, liste apenas os nomes das 10 principais tecnologias, ferramentas e hard skills para profissionais de dados.

    Regras:
    - Não inferir ou inventar nenhum item que não esteja explicitamente presente nas descrições.
    - Liste exatamente 10 itens únicos, sem repetições.
    - Retorne apenas os nomes, separados por vírgula, sem explicações ou textos adicionais.

    Exemplo de resposta esperada:
    Python, SQL, Tableau, Power BI, Hadoop, Spark, AWS, Docker, Git, Kafka
    """
)

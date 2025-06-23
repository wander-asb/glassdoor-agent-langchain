from langchain_core.prompts import ChatPromptTemplate

prompt_softskills = ChatPromptTemplate.from_template(
    """
    Você é um especialista em análise de mercado de trabalho.

    Com base estritamente nas descrições de vagas recentes, perfis e tendências, liste as 10 principais soft skills mais demandadas atualmente para profissionais da área de tecnologia.

    Regras:
    - Não inferir ou inventar nenhuma habilidade que não esteja explicitamente presente nas descrições.
    - Liste exatamente 10 itens únicos, sem repetições.
    - Retorne apenas os nomes das soft skills, separados por vírgula, sem explicações ou textos adicionais.

    Exemplo de resposta esperada:
    Comunicação, Trabalho em equipe, Resolução de problemas, Adaptabilidade, Pensamento crítico, Proatividade, Organização, Gestão de tempo, Colaboração, Flexibilidade
    """
)


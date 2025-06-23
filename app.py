from agents.agent_techskills import agent_techskills
from agents.agent_softskills import agent_softskills
from agents.supervisor_agent import supervisor_agent

def agente_orquestrador(job_title):
    summary = supervisor_agent(job_title)
    techskills = agent_techskills(summary)
    softskills = agent_softskills(summary)
    return {
        "Resumo das Vagas": summary,
        "Tech Skills": techskills,
        "Soft Skills": softskills
    }


def main():
    job_title = input("Digite o cargo/vaga: ")

    resultado = agente_orquestrador(job_title)
    print("\n===== Resultado final do Supervisor de Vagas =====")
    print(resultado)

if __name__ == "__main__":
    main()
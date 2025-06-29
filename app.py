from flask import Flask, request, jsonify
from agents.agent_techskills import agent_techskills
from agents.agent_softskills import agent_softskills
from agents.supervisor_agent import supervisor_agent

app = Flask(__name__)

def agente_orquestrador(job_title):
    summary = supervisor_agent(job_title)
    techskills = agent_techskills(summary)
    softskills = agent_softskills(summary)
    return {
        "Resumo das Vagas": summary,
        "Tech Skills": techskills,
        "Soft Skills": softskills
    }

@app.route("/", methods=["GET"])
def health_check():
    return jsonify(message="API está rodando! Use /analisar para enviar cargo."), 200

@app.route("/analisar", methods=["POST"])
def analisar():
    data = request.get_json()
    job_title = data.get("job_title")

    if not job_title:
        return jsonify(error="Campo 'job_title' é obrigatório"), 400

    resultado = agente_orquestrador(job_title)
    return jsonify(resultado), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


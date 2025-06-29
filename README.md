# 📊 Job Analyzer API

API de análise de descrições de vagas com LLMs, utilizando agentes orquestradores baseados em LangChain. O objetivo é extrair um resumo estruturado de requisitos técnicos e comportamentais de vagas de emprego a partir do título da posição.

---

## 🚀 Tecnologias

- **[LangChain](https://www.langchain.com/)** – para orquestração dos agentes de linguagem.
- **[Flask](https://flask.palletsprojects.com/)** – API leve e flexível.
- **[Gunicorn](https://gunicorn.org/)** – servidor WSGI para produção.
- **[Docker](https://www.docker.com/)** – containerização da aplicação.
- **[Playwright](https://playwright.dev/python/)** – raspagem de descrições de vagas (ex: LinkedIn).
- **Python 3.12+**

---

## 🧠 Funcionalidade

Dado um `job_title`, o sistema:

1. Raspas as primeiras 10 vagas com Playwright (ex: LinkedIn).
2. Envia as descrições para um agente supervisor (LangChain) que coordena a análise.
3. Gera um JSON estruturado com:
   - Hard Skills
   - Soft Skills
   - Certificações
   - Tecnologias recorrentes
   - Linguagens exigidas

---

## 📦 Instalação local

### 1. Pré-requisitos

- Docker
- Python 3.12 (apenas para testes locais fora do container)

### 2. Clone o projeto

```bash
git clone https://github.com/seu-usuario/glassdoor-agent-langchain.git
cd glassdoor-agent-langchain
```
### 3. Build e execução com Docker
```bash
docker build -t job-analyzer-api .
docker run -p 8080:8080 job-analyzer-api
```
### 4. Testes com Postman
```bash
POST /analisar
Content-Type: application/json
```

![Exemplo Postman](https://github.com/user-attachments/assets/c444f0af-1f12-42cb-8194-8c6740271cf9)


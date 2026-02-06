# 📧 Multi-Agent System for Writing and Evaluating Emails

## Sistema Multi-Agente para Escrita e Avaliação de E-mails

🇧🇷 *Versão em Português*
🇺🇸 *English Version Below*

---

# 🇧🇷 Português

## 🎯 Objetivo

Este projeto implementa um **sistema multi-agente utilizando LangGraph** para geração de e-mails profissionais.
O fluxo simula um processo real de trabalho, no qual diferentes agentes especializados colaboram para:

1. **Refletir e planejar** o conteúdo
2. **Escrever** o e-mail
3. **Avaliar e revisar** o resultado
4. Iterar até atingir qualidade adequada

A interface permite escolher o **tom do e-mail**:

* Formal
* Amigável
* Técnico

---

## 🧠 Arquitetura

**Agentes**

1. **Reflexão** – análise do contexto e planejamento
2. **Escrita** – geração do texto
3. **Avaliação** – revisão e decisão de reescrita

**Fluxo LangGraph**

```
Reflexão → Escrita → Avaliação ↺ (se necessário)
```

---

## 🧩 Como cada agente foi configurado (Prompts)

### 1. Agente de Reflexão

* Identifica objetivo e público
* Define nível de formalidade
* Lista pontos obrigatórios
* Considera o tom selecionado

### 2. Agente de Escrita

* Converte o plano em texto coeso
* Respeita regras do tom:

  * Formal → linguagem corporativa
  * Amigável → comunicação empática
  * Técnico → precisão e objetividade

### 3. Agente de Avaliação

* Revisa clareza e aderência
* Decide aprovação
* Solicita reescrita quando necessário

Formato obrigatório:

```
APROVADO: sim ou nao
JUSTIFICATIVA:
VERSAO_SUGERIDA:
```

---

## 🧪 Exemplo Real de Uso

**Entrada**

> “Escrever email para cliente explicando atraso na entrega por mudança de escopo e propondo nova data.”

**Tom:** Formal

**Saída (resumida)**

> Prezado(a),
> Identificamos ajustes no escopo necessários para garantir a qualidade técnica.
> Propomos como nova data 25/06 e seguimos à disposição para alinhamentos.
> Atenciosamente.

**Avaliação**

* Tom adequado
* Justificativa clara
* Proposta objetiva

---

## 🚀 Instruções de Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/mpolive/aula3-multi-agents.git
cd aula3-multi-agents
```

### 2. Criar e ativar ambiente virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar chave

Criar arquivo **.env**

```
OPENAI_API_KEY=sua_chave_aqui
```

### 5. Executar

```bash
streamlit run app.py
```

👉 [http://localhost:8501](http://localhost:8501)

---

## 📁 Estrutura

```
aula3-multi-agents/
├── app.py
├── email_graph.py
├── requirements.txt
├── .env
└── README.md
```

---

## 📊 Resultados

* Melhor estrutura textual
* Controle de estilo
* Processo iterativo
* Qualidade superior ao prompt único

---

# 🇺🇸 English Version

## 🎯 Objective

This project implements a **LangGraph multi-agent system** for professional email generation, simulating a real teamwork process:

1. Reflect and plan
2. Write
3. Evaluate
4. Iterate until approved

Available tones:

* Formal
* Friendly
* Technical

---

## 🧠 Architecture

Agents:

1. Reflection
2. Writing
3. Evaluation

Flow:

```
Reflection → Writing → Evaluation ↺
```

---

## 🧩 Agent Prompt Design

* **Reflection:** analyzes intent and audience
* **Writing:** generates according to tone
* **Evaluation:** quality gate with structured output

---

## 🧪 Real Example

**Input**

> “Write an email to a client explaining delay due to scope change and propose new deadline.”

**Tone:** Formal

**Output**

> Dear,
> Adjustments in scope were required to ensure quality.
> We propose June 25th as new deadline.
> Sincerely.

---

## 🚀 How to Run

```bash
python -m venv venv
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Outcomes

* Better argumentative structure
* Explicit tone control
* Transparent iterations

---

## 👥 Authors

Academic project on Multi-Agent LLM systems.

## 📄 License

Educational use.
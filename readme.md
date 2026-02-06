# 📧 Multi-Agent System for Writing and Evaluating Emails

## Sistema Multi-Agente para Escrita e Avaliação de E-mails

🇧🇷 *Versão em Português*
🇺🇸 *English Version Below*

---

## 🇧🇷 Português

### 🎯 Objetivo

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

### 🧠 Arquitetura

**Agentes**

1. **Reflexão** – análise do contexto e planejamento
2. **Escrita** – geração do texto
3. **Avaliação** – revisão e decisão de reescrita

**Fluxo LangGraph**

```
Reflexão → Escrita → Avaliação ↺ (se necessário)
```

---

### 🧪 Exemplo Real de Uso

**Entrada do Usuário**

> “Escrever email para cliente explicando atraso na entrega por mudança de escopo e propondo nova data.”

**Tom:** Formal

#### 📌 Saída Final Revisada

**Assunto:** Atualização sobre o cronograma do projeto

Prezado(a),

Gostaria de atualizá-lo(a) sobre o andamento do projeto. Durante a execução identificamos ajustes no escopo previamente definido, necessários para garantir a qualidade técnica da entrega.

Em razão dessas adequações, propomos como nova data o dia 25/06. Permanecemos à disposição para alinhar prioridades e minimizar impactos no planejamento.

Atenciosamente,
Equipe do Projeto

#### 📌 Avaliação do Agente

* Tom adequado ao contexto corporativo
* Clareza na justificativa
* Inclusão de proposta objetiva de solução
* Linguagem profissional e respeitosa

---

### 🛠 Tecnologias

* Python
* LangChain
* LangGraph
* Streamlit
* OpenAI API

---

### 🚀 Execução

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

### 📊 Resultados

* Melhor estrutura argumentativa
* Controle explícito de estilo
* Processo iterativo transparente
* Qualidade superior ao prompt único

---

---

## 🇺🇸 English Version

### 🎯 Objective

This project implements a **multi-agent system using LangGraph** for generating professional emails.
The workflow simulates a real working process in which specialized agents collaborate to:

1. **Reflect and plan** the content
2. **Write** the email
3. **Evaluate and review** the result
4. Iterate until adequate quality is achieved

The interface allows the user to choose the **tone of the email**:

* Formal
* Friendly
* Technical

---

### 🧠 Architecture

**Agents**

1. **Reflection Agent** – context analysis and planning
2. **Writing Agent** – text generation
3. **Evaluation Agent** – review and decision about rewriting

**LangGraph Flow**

```
Reflection → Writing → Evaluation ↺ (if needed)
```

---

### 🧪 Real Example

**User Input**

> “Write an email to a client explaining a delay due to scope change and proposing a new deadline.”

**Tone:** Formal

#### 📌 Final Output

**Subject:** Update on Project Schedule

Dear,

I would like to update you on the progress of the project. During development, adjustments to the originally defined scope were identified as necessary to ensure the technical quality of the delivery.

Due to these changes, we propose June 25th as the new deadline. We remain available to align priorities and reduce any impact on the overall planning.

Sincerely,
Project Team

#### 📌 Agent Evaluation

* Appropriate corporate tone
* Clear justification
* Objective proposal
* Professional language

---

### 🛠 Technologies

* Python
* LangChain
* LangGraph
* Streamlit
* OpenAI API

---

### 🚀 How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

### 📊 Outcomes

* Better argumentative structure
* Explicit tone control
* Transparent iterative process
* Higher quality than single-prompt approach

---

## 👥 Authors

Academic project developed for the study of Multi-Agent Systems with Large Language Models.

## 📄 License

Educational use.
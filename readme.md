# 📧 Multi-Agent Email Writer

## Sistema Multi-Agente para Escrita e Avaliação de E-mails

Este projeto demonstra a implementação de um **sistema multi-agente para escrita e avaliação de e-mails** utilizando a **OpenAI API**.  
A solução simula um fluxo de trabalho real, onde diferentes agentes de IA assumem papéis especializados, processando o contexto sequencialmente para gerar e-mails corporativos de alta qualidade.

O pipeline é composto por três agentes:

1. **Agente de Reflexão** – Analisa o contexto e cria um plano estruturado
2. **Agente de Escrita** – Redige o e-mail com base no plano de reflexão
3. **Agente de Avaliação** – Avalia, critica e fornece recomendações de melhoria

---

# 🇧🇷 Português

- Demonstrar o uso de **arquitetura multi-agente** com OpenAI API
- Melhorar qualidade, clareza e tom de e-mails corporativos
- Separar claramente as etapas de **reflexão, escrita e avaliação**
- Servir como base educacional para estudos de LLMs em pipelines multi-agente

---

## 🧠 Arquitetura

**Agentes**

1. **Reflexão** – análise do contexto e planejamento
2. **Escrita** – geração do texto
3. **Avaliação** – revisão e decisão de reescrita

**Fluxo LangGraph**

```text
Contexto do Usuário
        ↓
Agente de Reflexão (Planejamento)
        ↓ output → input
Agente de Escrita (Redação)
        ↓ output → input
Agente de Avaliação (Crítica e Recomendações)
        ↓
E-mail com Feedback Final
```

Cada agente é uma função independente que utiliza a OpenAI API (GPT-4 mini) para processar o contexto e gerar uma resposta estruturada.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **OpenAI API (GPT-4 mini)**
- **python-dotenv** (para gerenciamento de variáveis de ambiente)

---

## 📦 Instalação

### Pré-requisitos
- Python 3.10 ou superior
- Uma chave API válida do OpenAI (https://platform.openai.com/api-keys)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/multi-agent-email-writer.git
cd multi-agent-email-writer
```

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure sua chave da OpenAI criando um arquivo `.env` na raiz do projeto:

```bash
# .env
OPENAI_API_KEY="sua-chave-aqui"
OPENAI_ORG_ID="sua-org-id-opcional"
OPENAI_PROJECT_ID="seu-project-id-opcional"
```

Ou defina via variável de ambiente:

```bash
# Linux / Mac
export OPENAI_API_KEY="sua-chave"

# Windows (PowerShell)
$env:OPENAI_API_KEY="sua-chave"

# Windows (CMD)
setx OPENAI_API_KEY "sua-chave"
```

---

## 🧩 Como cada agente foi configurado (Prompts)

Execute o script principal do projeto:

> “Escrever email para cliente explicando atraso na entrega por mudança de escopo e propondo nova data.”

### Fluxo de Execução

1. **Agente de Reflexão** recebe o contexto do cliente e gera um plano estruturado
2. **Agente de Escrita** lê o plano e redige o e-mail corporativo
3. **Agente de Avaliação** analisa o e-mail gerado e fornece feedback

### Exemplo de Saída no Terminal

```
[Saída do Agente de Reflexão - Plano Estruturado]
...

[Saída do Agente de Escrita - E-mail Redigido]
...

[Saída do Agente de Avaliação - Feedback e Recomendações]
...
```

### Personalizando o Contexto

Para modificar o contexto do e-mail, edite o arquivo:
- [multi_agent_email/writting_agent/main.py](multi_agent_email/writting_agent/main.py)

Procure pela variável `customer_email` e altere o texto conforme necessário.

**Saída (resumida)**

## 🧪 Exemplo de Entrada e Saída

### Entrada (Contexto)
```
Crie um email para um cliente corporativo apresentando nossa solução
de visão computacional para inspeção industrial. O estilo deve ser
formal e técnico, com tom confiante e persuasivo. Inclua um CTA para
agendar uma demonstração.
```

### Fluxo de Processamento

**1. Reflexão (Planejamento):**
```
- Estrutura do e-mail definida
- Pontos principais: apresentação, diferenciais, CTA
- Tom: confiante e profissional
```

**2. Escrita (Redação):**
```
Prezado Sr. Silva,

Gostaria de apresentar nossa solução avançada de visão computacional...
[e-mail completo com CTA]
```

**3. Avaliação (Feedback):**
```
✓ Clareza: 9/10
✓ Profissionalismo: 9/10
✓ CTA presente e clara
Recomendações: Adicionar estatísticas de ROI
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

- ✅ Planejamento explícito antes da escrita (menos erros)
- ✅ Melhor adequação de tom e linguagem
- ✅ Revisão crítica automática e feedback estruturado
- ✅ Código modular e extensível
- ✅ Pipeline reutilizável para diferentes contextos
- ✅ Separação clara de responsabilidades

---

# 🇺🇸 English Version

- Loop automático de melhoria (avaliador → escritor)
- Pontuação de qualidade de e-mail com métricas
- Memória por cliente ou contexto persistente
- Interface web para facilitar uso
- Integração com bancos de dados CRM
- Uso de ferramentas (políticas internas, documentos, etc.)
- Suporte para múltiplos idiomas

---

## 🧠 Architecture

- OpenAI API Documentation: https://platform.openai.com/docs
- OpenAI Models: https://platform.openai.com/docs/models
- Python dotenv: https://github.com/theskumar/python-dotenv

---

## 🧩 Agent Prompt Design

Projeto desenvolvido para fins educacionais, demonstrando conceitos de **IA Generativa**, **arquiteturas multi-agente** e uso direto da **OpenAI API** para processamento sequencial de tarefas especializadas.

---

## 📋 Estrutura do Projeto

```
multi-agent-email/
├── main.py                          # Ponto de entrada principal
├── requirements.txt                 # Dependências do projeto
├── readme.md                        # Este arquivo
└── multi_agent_email/
    ├── main.py                      # Orquestrador dos agentes
    ├── openai_agent.py              # Cliente OpenAI compartilhado
    ├── reflection_agent/
    │   └── main.py                  # Agente de Reflexão
    ├── writting_agent/
    │   └── main.py                  # Agente de Escrita
    └── appraisal_agent/
        └── main.py                  # Agente de Avaliação
```

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
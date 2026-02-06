# 📧 Multi-Agent Email Writer com LangChain

## 📌 Visão Geral

Este projeto demonstra a implementação de um **sistema multi-agente para escrita e avaliação de e-mails** utilizando **LangChain**.  
A solução simula um fluxo de trabalho real, onde diferentes agentes de IA assumem papéis especializados, em vez de um único modelo gerar a resposta final.

O pipeline é composto por três agentes:

1. **Agente de Reflexão** – Analisa o problema e cria um plano estruturado
2. **Agente de Escrita** – Redige o e-mail com base no plano
3. **Agente de Avaliação** – Avalia, revisa e melhora o e-mail

---

## 🎯 Objetivo do Projeto

- Demonstrar o uso de **arquitetura multi-agente** com LangChain
- Melhorar qualidade, clareza e tom de e-mails corporativos
- Separar claramente as etapas de **planejamento, execução e revisão**
- Servir como base educacional para estudos de LLMs em pipelines

---

## 🧠 Arquitetura do Sistema

```text
Entrada do Usuário
        ↓
Agente de Reflexão (Planejamento)
        ↓
Agente de Escrita (Redação)
        ↓
Agente de Avaliação (Crítica e Revisão)
        ↓
E-mail Final Revisado
```

Cada agente é implementado como uma `LLMChain` independente.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **LangChain**
- **OpenAI API (Chat Models)**

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/multi-agent-email-langchain.git
cd multi-agent-email-langchain
```

2. Crie um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install langchain openai
```

4. Configure sua chave da OpenAI:

```bash
export OPENAI_API_KEY="sua-chave"   # Linux / Mac
setx OPENAI_API_KEY "sua-chave"     # Windows
```

---

## ▶️ Como Executar

Execute o script principal:

```bash
python main.py
```

Você pode alterar a entrada do usuário diretamente no código para testar diferentes tipos de e-mails.

---

## 🧪 Exemplo de Entrada

```text
Escreva um e-mail para um cliente informando atraso na entrega de um projeto.
```

## 📤 Exemplo de Saída

```text
Prezada(o) [Nome],

Espero que esteja bem.

Identificamos a necessidade de realizar ajustes técnicos adicionais no projeto,
o que impactará o prazo inicialmente previsto.

A nova data estimada de entrega é [nova data].
Estamos atuando de forma prioritária para garantir a qualidade acordada.

Agradecemos pela compreensão e seguimos à disposição.

Atenciosamente,
[Seu nome]
```

---

## 🔄 Benefícios da Abordagem Multi-Agente

- Planejamento explícito antes da escrita
- Melhor adequação de tom e linguagem
- Revisão crítica automática
- Código modular e extensível
- Pipeline reutilizável

---

## 🚀 Possíveis Evoluções

- Loop automático de melhoria (avaliador → escritor)
- Pontuação de qualidade do e-mail
- Memória por cliente ou contexto
- Integração com CrewAI
- Uso de ferramentas (políticas internas, CRM, etc.)

---

## 📚 Referências

- LangChain Documentation: https://python.langchain.com
- OpenAI API Documentation

---

## 👩‍💻 Autor

Projeto desenvolvido para fins educacionais, demonstrando conceitos de **IA Generativa**, **LangChain** e **arquiteturas multi-agente**.


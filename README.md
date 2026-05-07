# 💡 Edu — Educador Financeiro com IA Generativa

Edu é um assistente virtual de educação financeira desenvolvido para oferecer suporte personalizado em finanças pessoais por meio de IA generativa.

A aplicação utiliza contexto do usuário (perfil de investidor, histórico de transações, atendimentos anteriores e produtos financeiros disponíveis) para responder dúvidas financeiras de forma didática, contextualizada e segura.

O foco do projeto é unir experiência do usuário, análise de dados e IA em uma interface conversacional simples e acessível.

---

# O que é o Edu

O Edu atua como um educador financeiro digital.

Seu objetivo não é recomendar investimentos específicos, mas ajudar usuários a compreender conceitos como:

- reserva de emergência
- orçamento pessoal
- renda fixa
- diversificação
- planejamento financeiro
- perfil de investidor

As respostas são geradas considerando dados reais simulados do cliente, tornando a experiência mais personalizada.

Exemplo:

- perfil do investidor
- patrimônio atual
- reserva de emergência
- transações recentes
- histórico de atendimentos

---

# Arquitetura da Solução

A aplicação segue uma arquitetura simples orientada a contexto.

```text
Usuário
   ↓
Interface Web (Streamlit)
   ↓
Construção de contexto financeiro
   ↓
Prompt Engineering
   ↓
Google Gemini API
   ↓
Resposta contextualizada
```

## Componentes

### Frontend
- Streamlit

Responsável por:
- interface conversacional
- input do usuário
- renderização das respostas
- histórico de mensagens

### Processamento de dados
- Python
- Pandas
- JSON

Responsável por:
- leitura de datasets
- carregamento de perfil
- leitura de transações
- leitura de histórico de atendimento
- leitura de produtos financeiros

### Modelo de IA
- Google Gemini API

Responsável por:
- interpretação da pergunta
- geração de resposta contextualizada
- manutenção de comportamento via system prompt

---

# Estrutura do Projeto

```bash
dio-lab-bia-do-futuro/
│
├── data/
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
│
├── src/
│   └── app.py
│
└── README.md
```

---

# Como Executar

## 1. Clonar repositório

```bash
git clone https://github.com/caioverasalencar/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro
```

## 2. Instalar dependências

```bash
pip install streamlit pandas google-generativeai
```

## 3. Configurar API Key

Criar chave gratuita no Google AI Studio:

https://aistudio.google.com/app/apikey

Adicionar no arquivo `app.py`:

```python
API_KEY = "SUA_API_KEY"
```

## 4. Executar aplicação

```bash
streamlit run ./src/app.py
```

---

# Exemplo de Uso

### Pergunta do usuário

```text
Quanto gastei com alimentação recentemente?
```

### Resposta esperada

```text
Com base nas suas transações recentes, você realizou gastos relacionados à alimentação.
Esse acompanhamento ajuda no controle do orçamento e identificação de excessos.
Você costuma separar um limite mensal para alimentação?
```

---

### Pergunta conceitual

```text
O que é reserva de emergência?
```

### Resposta esperada

```text
Reserva de emergência é um valor guardado para lidar com imprevistos,
como despesas médicas ou perda de renda.
Ela costuma equivaler a alguns meses do custo de vida.
Você já possui uma reserva estruturada?
```

---

# Métricas de Avaliação

A solução foi avaliada considerando:

## Precisão contextual
Capacidade de usar corretamente:
- perfil do cliente
- patrimônio
- transações
- histórico

## Segurança de resposta
Restrições implementadas:
- não recomendar investimentos específicos
- restringir respostas ao domínio financeiro

## Eficiência de tokens
Otimizações realizadas:
- redução de contexto enviado
- limitação de histórico
- seleção parcial de produtos e transações

## UX conversacional
Critérios:
- respostas curtas
- linguagem simples
- interface limpa
- interação em formato chat

---

# Diferenciais

## Contextualização personalizada
As respostas utilizam dados do cliente em vez de respostas genéricas.

## Segurança financeira
Prompt restringe aconselhamento financeiro direto.

## Interface acessível
Uso de Streamlit para experiência web rápida e intuitiva.

## IA Generativa integrada
Uso de Google Gemini API como motor conversacional.

## Otimização para free tier
Ajustes para:
- reduzir consumo de tokens
- minimizar custo
- melhorar estabilidade

---

# Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Google Gemini API

---

# Autor

Projeto desenvolvido por **Caio Veras Alencar** como solução para desafio da DIO.

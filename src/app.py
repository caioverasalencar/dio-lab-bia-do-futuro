import json
import streamlit as st
import pandas as pd
import google.generativeai as genai

# ========== CONFIGURAÇÃO ==========
API_KEY = "CHAVE-AQUI"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ========== CARREGAR DADOS ==========
perfil = json.load(
    open(
        "C:/Users/caiov/Downloads/dio-lab-bia-do-futuro-main/data/perfil_investidor.json",
        encoding="utf-8"
    )
)

transacoes = pd.read_csv(
    "C:/Users/caiov/Downloads/dio-lab-bia-do-futuro-main/data/transacoes.csv"
)

historico = pd.read_csv(
    "C:/Users/caiov/Downloads/dio-lab-bia-do-futuro-main/data/historico_atendimento.csv"
)

produtos = json.load(
    open(
        "C:/Users/caiov/Downloads/dio-lab-bia-do-futuro-main/data/produtos_financeiros.json",
        encoding="utf-8"
    )
)

# ========== CONTEXTO OTIMIZADO ==========
@st.cache_data
def montar_contexto():
    return f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos
PERFIL: {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']}
RESERVA: R$ {perfil['reserva_emergencia_atual']}

ÚLTIMAS TRANSAÇÕES:
{transacoes.head(2).to_string(index=False)}

ÚLTIMOS ATENDIMENTOS:
{historico.head(2).to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos[:2], ensure_ascii=False)}
"""

contexto = montar_contexto()

# ========== PROMPT ==========
SYSTEM_PROMPT = """
Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples usando dados do cliente.

REGRAS:
- Nunca recomendar investimentos específicos;
- Responder apenas sobre finanças pessoais;
- Linguagem simples e direta;
- Usar exemplos personalizados;
- - Seja breve e claro;
- Sempre perguntar se o cliente entendeu.
"""

# ========== MEMÓRIA DE CHAT ==========
if "historico_chat" not in st.session_state:
    st.session_state.historico_chat = []

# ========== FUNÇÃO PRINCIPAL ==========
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA:
{msg}
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 400
            }
        )
        return response.text

    except Exception as e:
        return f"Erro temporário: {e}"

# ========== INTERFACE ==========
st.title("💡 Edu, Seu Educador Financeiro")

# mostrar histórico
for mensagem in st.session_state.historico_chat:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# input
if pergunta_usuario := st.chat_input("Digite sua dúvida financeira..."):
    st.session_state.historico_chat.append(
        {"role": "user", "content": pergunta_usuario}
    )
    st.chat_message("user").write(pergunta_usuario)

    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta_usuario)

    st.session_state.historico_chat.append(
        {"role": "assistant", "content": resposta}
    )
    st.chat_message("assistant").write(resposta)
#%%
#import google.generativeai as genai
#
#genai.configure(api_key="CHAVE AQUI")
#
#model = genai.GenerativeModel("models/gemini-2.5-flash")
#
#response = model.generate_content("diga oi")
#
#print(response.text)   # DEU CERTO

# %%

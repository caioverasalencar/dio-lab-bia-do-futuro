# Passo a Passo de Execução

## Setup da API Google Gemini

```bash
# 1. Instalar dependências
pip install streamlit pandas google-generativeai

# 2. Criar chave de API gratuita
# https://aistudio.google.com/app/apikey

# 3. Configurar a chave no arquivo
# app.py

API_KEY = "SUA_API_KEY_AQUI"

# 4. Testar se funciona
python app.py
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas google-generativeai

# 2. Rodar o app
streamlit run ./src/app.py
```

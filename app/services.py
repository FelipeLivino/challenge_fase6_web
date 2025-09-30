import streamlit as st
import requests
import pandas as pd
from app.config import API_URLS

def fetch_data(api_name):
    """Busca dados de uma API e retorna um DataFrame."""
    try:
        response = requests.get(API_URLS[api_name])
        response.raise_for_status()  # Lança exceção para erros HTTP
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados da API de {api_name}: {e}")
        return pd.DataFrame()

import streamlit as st

from app.services import fetch_data
from app.ui.equipamentos_tab import render_equipamentos_tab
from app.ui.sensores_tab import render_sensores_tab
from app.ui.leituras_tab import render_leituras_tab

def main():
    """Função principal da aplicação Streamlit."""
    # --- Configuração da Página ---
    st.set_page_config(
        page_title="Monitoramento de Sensores",
        page_icon="🤖",
        layout="wide",
    )

    # --- Título Principal ---
    st.title("Dashboard de Monitoramento de Sensores Industriais")
    st.markdown("Acompanhe em tempo real os dados dos seus equipamentos e sensores.")

    # --- Carregamento dos Dados ---
    df_equipamentos = fetch_data("equipamentos")
    df_sensores = fetch_data("sensores")
    df_leituras = fetch_data("leituras")

    # --- Abas da Aplicação ---
    tab_equip, tab_sensor, tab_leitura = st.tabs(["Equipamentos", "Sensores", "Leituras e Análises"])

    with tab_equip:
        render_equipamentos_tab(df_equipamentos)

    with tab_sensor:
        render_sensores_tab(df_sensores)

    with tab_leitura:
        render_leituras_tab(df_leituras, df_equipamentos, df_sensores)
    
    # --- Rodapé ---
    st.markdown("---")
    st.markdown("Desenvolvido para o Challenge da Fase 6 - FIAP.")

if __name__ == "__main__":
    main()

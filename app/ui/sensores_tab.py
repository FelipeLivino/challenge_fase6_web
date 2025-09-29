import streamlit as st

def render_sensores_tab(df_sensores):
    """Renderiza a aba de sensores."""
    st.header("Sensores Disponíveis")
    if not df_sensores.empty:
        st.dataframe(df_sensores, use_container_width=True)
    else:
        st.warning("Nenhum sensor encontrado ou falha ao carregar os dados.")

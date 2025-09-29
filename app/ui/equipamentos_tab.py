import streamlit as st

def render_equipamentos_tab(df_equipamentos):
    """Renderiza a aba de equipamentos."""
    st.header("Equipamentos Cadastrados")
    if not df_equipamentos.empty:
        st.dataframe(df_equipamentos, use_container_width=True)
    else:
        st.warning("Nenhum equipamento encontrado ou falha ao carregar os dados.")

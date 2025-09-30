import streamlit as st
import requests
import pandas as pd
from app.config import API_URLS

def render_equipamentos_tab(df_equipamentos):
    """Renderiza a aba de equipamentos."""
    if st.session_state.get("show_equipamento_dialog", False):
        equipamento_dialog(st.session_state.get("equipamento_to_edit"))
    else:
        render_equipamentos_list(df_equipamentos)

def render_equipamentos_list(df_equipamentos):
    """Renderiza a lista de equipamentos."""
    st.header("Equipamentos Cadastrados")

    if st.button("Adicionar Equipamento"):
        st.session_state.equipamento_to_edit = None
        st.session_state.show_equipamento_dialog = True
        st.rerun()

    if not df_equipamentos.empty:
        col_map = {
            "id": "ID",
            "marca": "Marca",
            "modelo": "Modelo",
            "status": "Status",
        }
        df_display = df_equipamentos[list(col_map.keys())].rename(columns=col_map)
        st.dataframe(df_display, use_container_width=True)

        st.subheader("Editar Equipamento")
        col1, col2 = st.columns([3, 1])
        with col1:
            equip_to_edit_id = st.selectbox(
                "Selecione um equipamento para editar",
                options=df_equipamentos["id"],
                format_func=lambda x: f"ID: {x} - {df_equipamentos.loc[df_equipamentos['id'] == x, 'marca'].iloc[0]} {df_equipamentos.loc[df_equipamentos['id'] == x, 'modelo'].iloc[0]}",
                index=None,
                placeholder="Selecione o equipamento",
                key="equip_select"
            )
        with col2:
            st.write("&nbsp;") # Placeholder for alignment
            if st.button("Editar", disabled=not equip_to_edit_id, key="edit_equipamento"):
                equipamento = df_equipamentos[df_equipamentos["id"] == equip_to_edit_id].iloc[0].to_dict()
                st.session_state.equipamento_to_edit = equipamento
                st.session_state.show_equipamento_dialog = True
                st.rerun()
    else:
        st.warning("Nenhum equipamento encontrado ou falha ao carregar os dados.")

def equipamento_dialog(equipamento=None):
    """Exibe um formulário para cadastrar ou editar um equipamento."""
    is_edit = equipamento is not None
    title = "Editar Equipamento" if is_edit else "Cadastrar Novo Equipamento"
    st.subheader(title)

    with st.form(key="equipamento_form"):
        marca = st.text_input("Marca", value=equipamento["marca"] if is_edit else "")
        modelo = st.text_input("Modelo", value=equipamento["modelo"] if is_edit else "")
        status_options = ["DESLIGADO", "NORMAL", "ATENCAO", "FALHA"]
        current_status_index = status_options.index(equipamento["status"]) if is_edit and equipamento["status"] in status_options else 0
        status = st.selectbox("Status", options=status_options, index=current_status_index)

        submitted = st.form_submit_button("Salvar")
        if submitted:
            save_equipamento(equipamento, marca, modelo, status)

    if st.button("Cancelar", key="cancel_equipamento"):
        st.session_state.show_equipamento_dialog = False
        st.rerun()

def save_equipamento(equipamento, marca, modelo, status):
    """Salva o equipamento (cria um novo ou atualiza um existente)."""
    with st.spinner("Salvando dados..."):
        is_edit = equipamento is not None
        url = API_URLS["equipamentos"]
        data = {"marca": marca, "modelo": modelo, "status": status}

        try:
            if is_edit:
                response = requests.put(f"{url}{equipamento['id']}/", json=data)
            else:
                response = requests.post(url, json=data)

            if response.status_code in [200, 201]:
                st.success(f"Equipamento {'atualizado' if is_edit else 'cadastrado'} com sucesso!")
                st.session_state.show_equipamento_dialog = False
                st.rerun()
            else:
                st.error("Ocorreu um erro ao salvar o equipamento.")
                st.error(f"Status Code: {response.status_code}")
                st.error(f"Resposta da API: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão: {e}")

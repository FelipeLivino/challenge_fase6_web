import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from app.config import API_URLS

def render_sensores_tab(df_sensores):
    """Renderiza a aba de sensores."""
    if st.session_state.get("show_sensor_dialog", False):
        sensor_dialog(st.session_state.get("sensor_to_edit"))
    else:
        render_sensores_list(df_sensores)

def render_sensores_list(df_sensores):
    """Renderiza a lista de sensores."""
    st.header("Sensores Disponíveis")

    if st.button("Adicionar Sensor"):
        st.session_state.sensor_to_edit = None
        st.session_state.show_sensor_dialog = True
        st.rerun()

    if not df_sensores.empty:
        # Assumindo que a API retorna estas colunas. Ajuste se necessário.
        col_map = {
            "id": "ID",
            "nome": "Nome",
            "status": "Status",
            "data_ativacao": "Data de Ativação",
        }
        # Garante que todas as colunas esperadas existam, preenchendo com None se não existirem
        for col in col_map.keys():
            if col not in df_sensores.columns:
                df_sensores[col] = None

        df_display = df_sensores[list(col_map.keys())].rename(columns=col_map)
        st.dataframe(df_display, use_container_width=True)

        st.subheader("Editar Sensor")
        col1, col2 = st.columns([3, 1])
        with col1:
            sensor_to_edit_id = st.selectbox(
                "Selecione um sensor para editar",
                options=df_sensores["id"],
                format_func=lambda x: f"ID: {x} - {df_sensores.loc[df_sensores['id'] == x, 'nome'].iloc[0]}",
                index=None,
                placeholder="Selecione o sensor",
                key="sensor_select"
            )
        with col2:
            st.write("&nbsp;") # Placeholder for alignment
            if st.button("Editar", disabled=not sensor_to_edit_id, key="edit_sensor"):
                sensor = df_sensores[df_sensores["id"] == sensor_to_edit_id].iloc[0].to_dict()
                st.session_state.sensor_to_edit = sensor
                st.session_state.show_sensor_dialog = True
                st.rerun()
    else:
        st.warning("Nenhum sensor encontrado ou falha ao carregar os dados.")

def sensor_dialog(sensor=None):
    """Exibe um formulário para cadastrar ou editar um sensor."""
    is_edit = sensor is not None
    title = "Editar Sensor" if is_edit else "Cadastrar Novo Sensor"
    st.subheader(title)

    with st.form(key="sensor_form"):
        nome = st.text_input("Nome", value=sensor["nome"] if is_edit else "")
        
        status_options = ["ATIVO", "INATIVO"]
        current_status_index = status_options.index(sensor["status"]) if is_edit and sensor["status"] in status_options else 0
        status = st.selectbox("Status", options=status_options, index=current_status_index)
        
        default_date = pd.to_datetime(sensor["data_ativacao"]).date() if is_edit and sensor.get("data_ativacao") else datetime.now().date()
        data_ativacao = st.date_input("Data de Ativação", value=default_date)

        submitted = st.form_submit_button("Salvar")
        if submitted:
            save_sensor(sensor, nome, status, data_ativacao)

    if st.button("Cancelar", key="cancel_sensor"):
        st.session_state.show_sensor_dialog = False
        st.rerun()

def save_sensor(sensor, nome, status, data_ativacao):
    """Salva o sensor (cria um novo ou atualiza um existente)."""
    with st.spinner("Salvando dados..."):
        is_edit = sensor is not None
        url = API_URLS["sensores"]
        data = {
            "nome": nome,
            "status": status,
            "data_ativacao": data_ativacao.isoformat()
        }

        try:
            if is_edit:
                response = requests.put(f"{url}{sensor['id']}/", json=data)
            else:
                response = requests.post(url, json=data)

            if response.status_code in [200, 201]:
                st.success(f"Sensor {'atualizado' if is_edit else 'cadastrado'} com sucesso!")
                st.session_state.show_sensor_dialog = False
                st.rerun()
            else:
                st.error("Ocorreu um erro ao salvar o sensor.")
                st.error(f"Status Code: {response.status_code}")
                st.error(f"Resposta da API: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão: {e}")

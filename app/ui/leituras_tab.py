import streamlit as st
import pandas as pd
from app.config import TEMPERATURA_ALERTA

def render_leituras_tab(df_leituras, df_equipamentos, df_sensores):
    """Renderiza a aba de leituras e análises."""
    st.header("Leituras dos Sensores")

    if df_leituras.empty or df_equipamentos.empty or df_sensores.empty:
        st.warning("Não foi possível carregar os dados de leituras, equipamentos ou sensores para análise.")
        return

    # --- Filtros ---
    col1, col2 = st.columns(2)
    with col1:
        # Criar um nome amigável para o equipamento
        df_equipamentos["nome_display"] = df_equipamentos["marca"] + " - " + df_equipamentos["modelo"]
        equip_selecionado = st.selectbox(
            "Selecione o Equipamento",
            options=df_equipamentos["nome_display"],
            index=None,
            placeholder="Filtrar por equipamento..."
        )

    with col2:
        sensor_selecionado = st.selectbox(
            "Selecione o Sensor",
            options=df_sensores["nome"],
            index=None,
            placeholder="Filtrar por sensor..."
        )

    # --- Lógica de Filtragem ---
    leituras_filtradas = df_leituras.copy()
    id_equip = None
    id_sensor = None

    if equip_selecionado:
        id_equip = df_equipamentos[df_equipamentos["nome_display"] == equip_selecionado]["id"].iloc[0]
        leituras_filtradas = leituras_filtradas[leituras_filtradas["t_equipamento_id"] == id_equip]

    if sensor_selecionado:
        id_sensor = df_sensores[df_sensores["nome"] == sensor_selecionado]["id"].iloc[0]
        leituras_filtradas = leituras_filtradas[leituras_filtradas["t_sensor_id"] == id_sensor]

    st.dataframe(leituras_filtradas, use_container_width=True)

    # --- KPIs e Alertas ---
    if not leituras_filtradas.empty:
        with st.container(height=300):
            st.subheader("Alertas de Leituras Filtradas")
            
            # Alertas
            leituras_alerta = leituras_filtradas[leituras_filtradas["temperatura"] > TEMPERATURA_ALERTA]
            if not leituras_alerta.empty:
                st.error(f"🚨 ALERTA: {len(leituras_alerta)} leitura(s) de temperatura acima de {TEMPERATURA_ALERTA}°C detectada(s)!")
                for _, leitura in leituras_alerta.iterrows():
                    equip_info = df_equipamentos[df_equipamentos["id"] == leitura["t_equipamento_id"]]["nome_display"].iloc[0]
                    st.warning(
                        f"**Equipamento:** {equip_info} | "
                        f"**Temperatura Registrada:** {leitura['temperatura']:.2f}°C | "
                        f"**Data:** {pd.to_datetime(leitura['data_coleta']).strftime('%d/%m/%Y %H:%M')}"
                    )
            else:
                st.success(f"✅ Nenhuma leitura de temperatura acima de {TEMPERATURA_ALERTA}°C. Todos os sistemas normais.")

        # KPIs
        st.subheader("KPIs das Leituras Filtradas")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        avg_temp = leituras_filtradas["temperatura"].mean()
        avg_umid = leituras_filtradas["umidade"].mean()
        avg_vibr = leituras_filtradas["vibracao"].mean()
        
        kpi1.metric(
            label="Temperatura Média (°C)",
            value=f"{avg_temp:.2f}"
        )
        kpi2.metric(
            label="Umidade Média (%)",
            value=f"{avg_umid:.2f}"
        )
        kpi3.metric(
            label="Vibração Média (g)",
            value=f"{avg_vibr:.3f}"
        )
        kpi4.metric(
            label="Nº de Alertas de Temp.",
            value=len(leituras_alerta)
        )

        # Gráfico de Linha
        st.subheader("Histórico de Leituras")
        leituras_filtradas["data_coleta"] = pd.to_datetime(leituras_filtradas["data_coleta"])
        st.line_chart(leituras_filtradas.set_index("data_coleta")[["temperatura", "umidade", "vibracao"]])
    
    elif equip_selecionado or sensor_selecionado:
        st.info("Nenhuma leitura encontrada para os filtros selecionados.")

# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Previsão de Falhas em Equipamentos Industriais com Sensores e IA

## Nome do grupo
Rumo ao NEXT

## 👨‍🎓 Integrantes: 

- Felipe Livino dos Santos (RM 563187)
- Daniel Veiga Rodrigues de Faria (RM 561410)
- Tomas Haru Sakugawa Becker (RM 564147)
- Daniel Tavares de Lima Freitas (RM 562625)
- Gabriel Konno Carrozza (RM 564468)

## 👩‍🏫 Professores:

### Tutor(a)

- Leonardo Ruiz Orabona

### Coordenador(a)

- ANDRÉ GODOI CHIOVATO


## 📜 Descrição

O projeto tem como objetivo desenvolver uma solução inteligente para antecipar falhas em equipamentos industriais por meio de sensores conectados e algoritmos de machine learning. A aplicação será responsável por monitorar continuamente os dados gerados por máquinas, processá-los em tempo real e utilizar modelos preditivos para indicar riscos de falha. Além disso, a plataforma contará com um dashboard interativo para visualização dos dados, índices de falha e status dos equipamentos.

A aplicação será implantada na plataforma Heroku. O frontend será construído com Streamlit, que também servirá como interface para visualização dos dashboards e indicadores. Toda a lógica será implementada em Python, desde os simuladores até os modelos de previsão.

## 📁 Estrutura de pastas

```
C:.
├───.envEXAMPLE
├───.gitignore
├───.python-version
├───main.py
├───Procfile
├───README.md
├───requirements.txt
├───.git
├───.venv
├───app
│   ├───__init__.py
│   ├───config.py
│   ├───services.py
│   ├───__pycache__
│   └───ui
│       ├───__init__.py
│       ├───equipamentos_tab.py
│       ├───leituras_tab.py
│       ├───sensores_tab.py
│       └───__pycache__
└───assets
    ├───arquitetura.png
    └───logo-fiap.png
```

# Dashboard de Monitoramento de Sensores Industriais

Este é o frontend da solução de monitoramento de sensores, desenvolvido para visualizar, gerenciar e analisar os dados coletados em tempo real. A interface foi construída utilizando **Streamlit** e se comunica com uma API backend para persistir e consultar as informações.

O dashboard permite a gestão completa dos ativos (equipamentos e sensores) e fornece uma visão analítica sobre as leituras, incluindo um sistema de alertas e KPIs para tomada de decisão.

![Visão Geral do Dashboard](assets/01-dashboard-geral.png)
> **Instrução para imagem:** Tire um screenshot da tela "Leituras e Análises" mostrando a tabela, os KPIs e os alertas.

---

## Funcionalidades da Interface

A interface gráfica é dividida em três seções principais, conforme demonstrado na apresentação.

### 1. Gestão de Equipamentos

Esta seção permite o ciclo de vida completo do cadastro de equipamentos industriais.

* **Cadastro de Novos Equipamentos:** É possível adicionar um novo equipamento ao sistema informando sua **Marca**, **Modelo** e **Status** inicial (ex: Normal, Atenção, Falha).
    ![Cadastro de Equipamento](assets/02-cadastro-equipamento.png)
    > **Instrução para imagem:** Capture a tela com o formulário "Cadastrar Novo Equipamento" preenchido.

* **Edição de Equipamentos:** A plataforma permite selecionar um equipamento já existente e alterar suas informações, como a marca ou o modelo, garantindo que os dados estejam sempre atualizados.
    ![Edição de Equipamento](assets/03-edicao-equipamento.png)
    > **Instrução para imagem:** Capture a tela mostrando o formulário "Editar Equipamento" com um item selecionado.

### 2. Gestão de Sensores

Similar à gestão de equipamentos, esta área é dedicada ao gerenciamento dos sensores que coletam os dados.

* **Cadastro e Ativação de Sensores:** Novos sensores podem ser cadastrados com um nome e uma data de ativação.
    ![Cadastro de Sensor](assets/04-cadastro-sensor.png)
    > **Instrução para imagem:** Capture o formulário "Cadastrar Novo Sensor".

* **Edição e Status:** É possível editar os dados de um sensor e alterar seu status (por exemplo, de "ATIVO" para "INATIVO"), facilitando a manutenção.
    ![Edição de Sensor](assets/05-edicao-sensor.png)
    > **Instrução para imagem:** Capture a tela de edição de um sensor, mostrando a mudança de status.

### 3. Leituras e Análises

Esta é a tela principal do dashboard, onde os dados são visualizados e analisados.

* **Tabela de Leituras:** Exibe os dados brutos recebidos dos sensores em tempo real, ordenados do mais recente para o mais antigo. As colunas incluem temperatura, umidade, vibração e o status (`NORMAL` ou `PERIGO`) definido pelo modelo de Machine Learning no backend.

* **Sistema de Alertas:** A seção **"Alertas de Leituras Filtradas"** é acionada automaticamente quando uma leitura é recebida com status de `PERIGO` ou `ALERTA`. Ela exibe um resumo do evento, incluindo o equipamento, os dados da leitura e a data/hora exata do ocorrido.
    ![Alertas e KPIs](assets/06-alertas-kpis.png)
    > **Instrução para imagem:** Dê um zoom na área que mostra os "Alertas" e os cards de "KPIs".

* **KPIs (Key Performance Indicators):** Cards de fácil visualização apresentam métricas essenciais, como **Temperatura Média**, **Umidade Média**, **Vibração Média** e o **Número Total de Alertas** gerados.

* **Histórico Gráfico:** Um gráfico de linhas plota o histórico das leituras de temperatura, umidade e vibração ao longo do tempo, permitindo a identificação de tendências e anomalias.
    ![Gráfico Histórico](assets/07-grafico-historico.png)
    > **Instrução para imagem:** Capture a parte da tela que mostra o gráfico "Histórico de Leituras".

* **Filtros Dinâmicos:** A interface é interativa. O usuário pode filtrar todos os dados da tela (tabela, KPIs e gráfico) selecionando um **Equipamento** ou um **Sensor** específico. Caso não existam leituras para o filtro selecionado, uma mensagem informativa é exibida.
    ![Filtros em Ação](assets/08-filtro-equipamento.png)
    > **Instrução para imagem:** Capture a tela com um filtro de equipamento ou sensor aplicado, mostrando os dados mudando.

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

_Pré-requisitos:_

- Python 3.8+ instalado
- Heroku CLI (opcional para deploy)

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

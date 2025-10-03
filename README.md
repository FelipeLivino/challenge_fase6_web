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

<image src="assets/dashboardVisaoGeral.png" alt="Visao geral do dashboard" width="100%" height="100%">

---

## Funcionalidades da Interface

A interface gráfica é dividida em três seções principais, conforme demonstrado na apresentação.
▶️ [Assista ao vídeo no YouTube](https://youtu.be/RgsAcX__7xw)

### 1. Gestão de Equipamentos

Esta seção permite o ciclo de vida completo do cadastro de equipamentos industriais.

* **Cadastro de Novos Equipamentos:** Ao clicar em **Adicionar equipamento** é possível adicionar um novo equipamento ao sistema informando sua **Marca**, **Modelo** e **Status** inicial (ex: Normal, Atenção, Falha).
<image src="assets/addEquipamento.png" alt="Cadastro de equipamento" width="100%" height="100%">

* **Edição de Equipamentos:** A plataforma permite selecionar um equipamento já existente e alterar suas informações, como a marca ou o modelo, garantindo que os dados estejam sempre atualizados.

### 2. Gestão de Sensores

Similar à gestão de equipamentos, esta área é dedicada ao gerenciamento dos sensores que coletam os dados.

* **Cadastro e Ativação de Sensores:** Novos sensores podem ser cadastrados com um nome e uma data de ativação.
<image src="assets/adicionarSensor.png" alt="Cadastro de sensor" width="100%" height="100%">

* **Edição e Status:** É possível editar os dados de um sensor e alterar seu status (por exemplo, de "ATIVO" para "INATIVO"), facilitando a manutenção.

### 3. Leituras e Análises

Esta é a tela principal do dashboard, onde os dados são visualizados e analisados.

* **Tabela de Leituras:** Exibe os dados brutos recebidos dos sensores em tempo real, ordenados do mais recente para o mais antigo. As colunas incluem temperatura, umidade, vibração e o status (`NORMAL` ou `PERIGO`) definido pelo modelo de Machine Learning no backend.

* **Sistema de Alertas:** A seção **"Alertas de Leituras Filtradas"** é acionada automaticamente quando uma leitura é recebida com status de `PERIGO` ou `ALERTA`. Ela exibe um resumo do evento, incluindo o equipamento, os dados da leitura e a data/hora exata do ocorrido.
<image src="assets/Leituras.png" alt="Tabela de leituras" width="100%" height="100%">


* **KPIs (Key Performance Indicators):** Cards de fácil visualização apresentam métricas essenciais, como **Temperatura Média**, **Umidade Média**, **Vibração Média** e o **Número Total de Alertas** gerados.

* **Histórico Gráfico:** Um gráfico de linhas plota o histórico das leituras de temperatura, umidade e vibração ao longo do tempo, permitindo a identificação de tendências e anomalias.
<image src="assets/KPIs .png" alt="Grafico de visualização" width="100%" height="100%">


* **Filtros Dinâmicos:** A interface é interativa. O usuário pode filtrar todos os dados da tela (tabela, KPIs e gráfico) selecionando um **Equipamento** ou um **Sensor** específico. Caso não existam leituras para o filtro selecionado, uma mensagem informativa é exibida.

## Arquitetura do Circuito Feito no Wokwi.com

<image src="assets/wokwi.png" alt="Circuito no Wokwi" width="100%" height="100%">

### **Análise do Código do Circuito (`.ino`)**

O código em C++ para o ESP32 foi atualizado e reestruturado para otimizar a coleta e o envio de dados dos sensores de monitoramento industrial. A seguir, os principais blocos de funcionamento:

#### **Configuração Inicial (`setup`)**

Nesta etapa, o ambiente do microcontrolador é preparado para a operação.

- **Inicialização de Comunicação e Sensores:**
  - Inicializa a comunicação serial para fins de debug e monitoramento.
  - Inicia os sensores de temperatura/umidade (DHT) e vibração (acelerômetro).
- **Conexão Wi-Fi:**
  - Estabelece a conexão com a rede Wi-Fi utilizando as credenciais fornecidas.
- **Calibração dos Sensores:**
  - Executa um processo de calibração inicial para garantir a precisão das leituras. O número de amostras para a calibração pode ser ajustado diretamente no código.

#### **Loop Principal (`loop`)**

O coração do programa, onde a coleta e o envio de dados ocorrem de forma contínua e eficiente.

- **Leitura Otimizada dos Sensores:**
  - Em vez de usar `delay()`, que bloqueia o processador, o loop utiliza uma **medição de tempo baseada em `millis()`**. Essa abordagem de boas práticas permite que o ESP32 continue responsivo enquanto aguarda o intervalo para a próxima coleta de dados.
  - Realiza a leitura dos valores de temperatura, umidade e vibração.
- **Envio Direto dos Dados:**
  - Após cada ciclo de leitura, os dados são imediatamente preparados e enviados para a API, garantindo que as informações cheguem ao backend em tempo real.

#### **Envio de Dados (Função de Envio HTTP)**

Esta função é responsável por formatar e transmitir as informações para o servidor.

- **Formatação JSON:**
  - Os dados coletados (temperatura, umidade, vibração) e os identificadores (`equipamento_id`, `sensor_id`) são formatados em um objeto JSON.
  > **Importante:** O campo `status` foi intencionalmente removido do payload. A responsabilidade de analisar os dados e determinar o estado do equipamento (`NORMAL`, `PERIGO`, etc.) foi delegada à API, que utiliza um modelo de Machine Learning.
- **Requisição HTTP POST:**
  - Utilizando a biblioteca `HTTPClient`, a função envia os dados formatados para o endpoint do web service (`/leitura-sensor`).
- **Feedback da Análise Remota:**
  - O código de resposta da API, que agora inclui o `status` determinado pelo modelo de ML, é impresso no monitor serial. Isso permite verificar em tempo real não apenas o sucesso do envio, mas também o resultado da análise inteligente feita no backend.

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

_Pré-requisitos:_

- Python 3.8+ instalado
- Heroku CLI (opcional para deploy)

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

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

# Código do Sensor ESP32 (Simulação Wokwi)

Este diretório contém o código-fonte para o microcontrolador ESP32, projetado para ser executado no ambiente de simulação online **Wokwi**.

O objetivo deste código é simular um sensor industrial que coleta dados de temperatura, umidade e vibração, e os envia para uma API de monitoramento para análise e armazenamento.

---

## Principais Características e Melhorias

Esta versão do código foi atualizada com foco em melhores práticas e maior desacoplamento de responsabilidades, conforme descrito abaixo:

### 1. Delegação da Lógica de Status para a API

Anteriormente, o próprio sensor poderia tentar determinar o status do equipamento. Nesta versão, essa responsabilidade foi removida do microcontrolador.

* **O campo `status` não é mais enviado no payload:** O ESP32 agora se concentra exclusivamente em coletar e enviar os **dados brutos** dos sensores.
* **Inteligência no Backend:** A lógica para determinar se a condição é `NORMAL`, `PERIGO` ou `ALERTA` é gerenciada inteiramente pela API, que utiliza um modelo de Machine Learning para analisar os dados recebidos. Isso torna o código do sensor mais simples, leve e focado.

### 2. Remoção de `delay()` (Boas Práticas)

Para otimizar o desempenho e a responsividade do microcontrolador, a função `delay()` foi substituída.

* **Medição de Tempo Não-Bloqueante:** O código agora utiliza uma abordagem baseada em medição de tempo (usando `millis()`), que permite que o ESP32 execute outras tarefas enquanto aguarda o próximo ciclo de leitura, em vez de "congelar" o processador.

---

## Como Executar e Testar a Simulação

Siga os passos abaixo para interagir com o projeto no Wokwi.

### 1. Iniciar a Simulação
   - Abra o projeto no Wokwi e clique no botão de "Play" (▶️) para iniciar a execução do código.

### 2. Observar a Calibração
   - No início, o sensor executa um rápido processo de calibração. No código atual, ele está configurado para coletar **2 amostras**, mas este valor pode ser facilmente aumentado para uma calibração mais precisa.

### 3. Monitorar o Envio de Dados (Status Normal)
   - Após a calibração, o ESP32 começará a enviar leituras para a API em intervalos regulares.
   - Observe o **Serial Monitor** na parte inferior da tela. Você verá a resposta da API, que deve indicar um status **`"NORMAL"`** sob condições padrão.

    ```json
    // Exemplo de resposta da API no Serial Monitor
    {
      "id": 302,
      "status": "NORMAL",
      "equipamento_id": 1,
      ...
    }
    ```

### 4. Simular um Alerta (Gerar "PERIGO")
   - A grande vantagem do Wokwi é a interatividade. Para testar o sistema de alertas:
   - **Altere o valor de um sensor:** Clique e arraste o controle do **sensor de vibração** (acelerômetro) para simular uma vibração excessiva no equipamento.
   - **Observe a Resposta:** Imediatamente, a próxima leitura enviada à API será analisada pelo modelo de Machine Learning, e a resposta retornada no Serial Monitor mudará para **`"PERIGO"`**.

    ```json
    // Exemplo de resposta da API após simular alta vibração
    {
      "id": 303,
      "status": "PERIGO",
      "equipamento_id": 1,
      ...
    }
    ```

Este teste confirma que todo o fluxo (coleta, envio, análise de ML e resposta) está funcionando corretamente. Os dados enviados, incluindo os alertas, serão refletidos em tempo real no [Dashboard de Monitoramento](#link-para-o-readme-do-dashboard).

---

## Estrutura do Payload Enviado à API

O ESP32 monta e envia um JSON com a seguinte estrutura para o endpoint do web service:

```json
{
  "temperatura": 24.0,
  "umidade": 60.0,
  "vibracao": 1.4706,
  "data_coleta": "2025-10-02T15:30:00",
  "t_equipamento_id": 1,
  "t_sensor_id": 2
}
```
## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

_Pré-requisitos:_

- Python 3.8+ instalado
- Heroku CLI (opcional para deploy)

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

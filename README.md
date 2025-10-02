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

## Arquitetura

<image src="assets/arquitetura.png" alt="Arquitetura do projeto" width="100%" height="100%">

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

## 🛠️ Tecnologias Utilizadas

🔧 Linguagem de Programação:
-	Python: Para o backend e manipulação de dados.
-	Streamlit: Para a criação do dashboard interativo.
🌐 Frontend:
-	Streamlit: Framework para construção da interface do usuário.
🧠 Inteligência Artificial:
-	Pandas e NumPy: Para manipulação e tratamento de dados.
-	Scikit-learn: Para a construção de modelos de machine learning.
☁️ Servidor de Aplicação:
-	Heroku: Plataforma como serviço (PaaS) para implantação e hospedagem da aplicação.

## 📆 Plano Inicial de Desenvolvimento

Etapas:
1.	Frontend – Setup do Streamlit.
2.	Sensores – Criação dos scripts simuladores em Python.
3.	API – Desenvolvimento da API que recebe e processa dados dos sensores.
4.	Banco de Dados – Estruturação do banco de dados.
5.	Modelagem de ML – Modelos de previsão de falha.
6.	Dashboard – Exibição dos dados e previsões no frontend.


## 📥 Estratégia de Coleta de Dados

Simulação de Sensores
-	Utilizaremos scripts Python que simulam sensores industriais.
-	Serão gerados dados como: temperatura, vibração, tempo de uso, ciclos de operação, etc.
-	Os dados serão processados pela API da aplicação.

## 📊 Justificativa

No setor industrial, falhas inesperadas em equipamentos podem gerar prejuízos significativos devido à paralisação de linhas de produção, manutenção corretiva emergencial e perda de produtividade. Apesar da presença de sensores nos equipamentos, muitas vezes os dados capturados não são utilizados de forma preditiva. Nosso projeto busca transformar esses dados em insights valiosos, utilizando aprendizado de máquina para prever falhas antes que elas ocorram, possibilitando ações preventivas e uma maior eficiência operacional.

O projeto visa entregar uma solução inteligente e escalável para análise preditiva de falhas, utilizando tecnologias modernas de backend e frontend. A fase inicial foca em levantar a arquitetura, integrar os componentes básicos e montar uma base para aplicação de machine learning.

## ✅ Funcionalidades previstas

- Dashboard com índices de falha
- Previsão de risco com base em sensores (ML)
- APIs para ingestão de dados
- Simuladores de sensores
- Cache do estado atual dos equipamentos

## Divisão de Responsabilidades (exemplo):

- Membro	Responsabilidade
- Gabriel	Frontend com Streamlit
- Daniel F.	API em Python + Integração com sensores
- Tomas	Simulador de sensores
- Felipe	Configuração do Heroku
- Daniel V.	Modelagem de ML

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

_Pré-requisitos:_

- Python 3.8+ instalado
- Heroku CLI (opcional para deploy)

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

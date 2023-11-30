## 🤖 rasa-project

Este projeto abriga os arquivos de configuração e o código-fonte responsável por compilar o modelo do chatbot para o projeto RASA.

### Estrutura de arquivos

| **`/`**                  |                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------|
| **`domain.yml`**         | Define o domínio do chatbot, incluindo intenções, entidades e respostas de ações.           |
| **`config.yml`**         | Especifica as configurações do modelo RASA, como o pipeline de processamento de linguagem natural. |
| **`endpoints.yml`**      | Contém informações sobre os endpoints, como o servidor do modelo e o servidor de ações.     |
| **`credentials.yml`**    | Armazena credenciais para serviços externos, como APIs ou canais de mensagens.              |

| **`data/`**              | Diretório que contém dados de treinamento e regras para o modelo.                           |
|--------------------------|---------------------------------------------------------------------------------------------|
| - **`nlu.yml`**          | Exemplos de treinamento para o processamento de linguagem natural (frases reais).           |
| - **`stories.yml`**      | Contém "histórias" de exemplo para treinar o modelo a seguir fluxos de conversação.         |
| - **`rules.yml`**        | Define regras de conversação para orientar o comportamento do chatbot.                      |

| **`actions/`**           | Diretório que contém o código fonte para ações personalizadas do chatbot.                   |
|--------------------------|---------------------------------------------------------------------------------------------|
| - **`actions.py`**       | Define as ações personalizadas que o chatbot pode realizar.                                 |

### Como desenvolver

Primeiro, abra o projeto em um editor de código fonte e edite os arquivos da maneira necessária. Certifique-se de que você tem o framework [Rasa Open Source](https://rasa.com/docs/rasa/installation/installing-rasa-open-source/) instalado e a versão correta do Python em sua máquina. Dentro do diretório do projeto, no Terminal, você pode executar o seguinte:

1. **Treinar o modelo (`rasa train`):** Treine o modelo usando os dados de treinamento definidos em `data/`.

2. ** Conversar com o modelo (`rasa shell`):** Inicie uma sessão simples de conversa para testar o comportamento do chatbot.

3. ** Interagir com o modelo (`rasa interactive`):** Inicie uma sessão interativa de conversa para testar de debugar o comportamento do chatbot.

#### Customizando respostas

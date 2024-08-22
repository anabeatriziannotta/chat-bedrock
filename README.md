# Chat com Claude Haiku

Este projeto consiste em uma aplicação web que integra um frontend em HTML com um backend Flask para interagir com um modelo AWS Bedrock. Este README fornece instruções sobre como configurar e implantar tanto o frontend quanto o backend.

## Visão Geral

- **Frontend**: Uma página HTML interativa que permite aos usuários inserir prompts e visualizar respostas.
- **Backend**: Um servidor Flask que processa os prompts e interage com o AWS Bedrock.

## Estrutura do Projeto

```
chat-bedrock/
├── backend/
│   ├── app.py            
│   └── requirements.txt    
└── frontend/
    └── index.html           
```

## Configuração e Execução

### 1. Configuração e Execução do Backend

O backend é implementado em Flask e serve a API para interagir com o modelo AWS Bedrock.

#### Requisitos

- **Python 3.x**: Certifique-se de ter Python 3.x instalado.
- **Pacotes Python**:
  - Flask
  - flask-cors
  - boto3

#### Instalação das Dependências

Crie e instale as dependências:

O arquivo `requirements.txt` deve conter:

```
Flask
flask-cors
boto3
```

#### Configuração

- **Credenciais AWS**: Configure suas credenciais da AWS para permitir que o `boto3` acesse o serviço Bedrock. Isso pode ser feito através do arquivo `~/.aws/credentials` ou configurando variáveis de ambiente.

- **Arquivo `app.py`**: Certifique-se de que a configuração do cliente `boto3` (região e ID do modelo) está correta.

#### Executando o Backend

Execute o servidor Flask:

```bash
python app.py
```

O backend estará disponível em `http://localhost:5000`.

### 2. Configuração e Execução do Frontend

O frontend é uma página HTML que se comunica com o backend.

#### Servidor Web Estático

Você pode usar um servidor web estático para hospedar o frontend:

1. **Navegue até o diretório do frontend**:

   ```bash
   cd frontend
   ```

2. **Inicie um servidor HTTP simples**:

   ```bash
   python -m http.server 8000
   ```

3. **Acesse o HTML**:

   Abra um navegador e vá para `http://localhost:8000`.

#### Configuração do JavaScript

No arquivo `index.html`, certifique-se de que o URL da API está configurado corretamente para apontar para o backend. O URL padrão é `http://localhost:5000/api/invoke`.

### Acesso e Testes

1. **Acesse o Frontend**:

   Abra um navegador e vá para `http://localhost:8080` para ver a página HTML.

2. **Verifique a Comunicação**:

   Teste a funcionalidade enviando prompts e garantindo que o frontend recebe e exibe as respostas do backend.

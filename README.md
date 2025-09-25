# Payment System API

Sistema para criação e processamento de pagamentos.

## 🛠️ Tecnologias Utilizadas

- **Flask 2.3.0** - Framework web Python
- **Flask-SQLAlchemy 3.1.1** - ORM para gerenciamento do banco de dados
- **Flask-SocketIO 5.3.6** - Comunicação em tempo real via WebSocket
- **QRCode 7.4.2** - Geração de códigos QR para pagamentos
- **Pillow 10.4.0** - Processamento de imagens
- **SQLite** - Banco de dados local
- **Pytest** - Framework para testes unitários

## 🏗️ Arquitetura e Padrões

### Estrutura do Projeto
```
├── app.py                 # Aplicação principal Flask
├── db_models/            # Modelos de dados (ORM)
│   └── payment.py
├── docs/
├── payments/             # Lógica de processamento de pagamentos
│   └── pix.py
├── repository/           # Camada de acesso a dados
│   └── database.py
├── templates/            # Templates HTML
├── static/              # Arquivos estáticos (CSS, imagens)
└── tests/               # Testes unitários
```

### Padrões Implementados
- **Repository Pattern** - Separação da lógica de acesso a dados
- **MVC (Model-View-Controller)** - Organização da aplicação
- **Factory Pattern** - Inicialização da aplicação Flask

## ⚙️ Setup e Configuração

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/DimitriSchulzAmado/payment-system-api.git
cd payment-system
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. (Opcional) Integre a documentação Swagger:
```bash
# Veja instruções detalhadas em SWAGGER_INTEGRATION.md
# Para visualização rápida, acesse https://editor.swagger.io/ e carregue swagger.yaml
```

4. Execute a aplicação:
```bash
python app.py
```

5. Acesse a aplicação em `http://localhost:5000`

### Configuração do Banco de Dados

O banco SQLite é criado automaticamente na primeira execução no diretório `instance/database.db`.


## 🚀 Funcionalidades

- **Criação de pagamentos PIX** via API REST
- **Geração automática de QR Code** para pagamentos
- **Confirmação de pagamentos** em tempo real
- **Interface web** para visualização de pagamentos
- **WebSocket** para notificações em tempo real

## 📡 Documentação da API

- **Swagger UI**: `http://localhost:5000/api/docs`
- **Especificação JSON**: `http://localhost:5000/api/swagger.json`

### Endpoints Principais

- `POST /payments/pix` - Criar novo pagamento PIX
- `GET /payments/pix/qr_code/<file_name>` - Obter imagem do QR Code
- `GET /payments/pix/confirmation` - Confirmar pagamento
- `GET /payments/pix/<payment_id>` - Visualizar página de pagamento

### WebSocket Events
- `connect` - Cliente conecta ao servidor
- `disconnect` - Cliente desconecta do servidor
- `payment-confirmed-{payment_id}` - Evento emitido quando pagamento é confirmado

## 🧪 Testes

Execute os testes com:
```bash
pytest tests/test_pix.py -v
```
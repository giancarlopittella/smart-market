# 🛒 Smart Market

Sistema desktop de autoatendimento inspirado nos caixas de supermercados, desenvolvido em Python utilizando PyQt6 e PostgreSQL.

---

## 🚀 Tecnologias

- Python 3
- PyQt6
- PostgreSQL
- Psycopg2
- Pygame

---

## ✅ Funcionalidades

- Inclusão de CPF na nota
- Cadastro de produtos
- Leitura de código de barras
- Carrinho de compras
- Registro de vendas
- Pagamento
- Cupom Fiscal
- Armazenamento das vendas no PostgreSQL
- Reinício automático para uma nova compra

---

## 📂 Estrutura

```text
Mercado/
│
├── assets/
├── banco/
├── cadastro_produto.py
├── checkout.py
├── cupom.py
├── database.py
├── main.py
├── pagamento.py
├── tela_inicio.py
├── requirements.txt
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/giancarlopittella/smart-market.git
```

Acesse a pasta do projeto:

```bash
cd smart-market
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a conexão com o PostgreSQL no arquivo `database.py`.

Execute a aplicação:

```bash
python main.py
```

---

## 🎯 Objetivo

Projeto desenvolvido para fins de estudo e prática de:

- Interfaces Desktop com PyQt6
- Programação Orientada a Objetos
- Integração com PostgreSQL
- CRUD
- Fluxo completo de um sistema de autoatendimento

---

## 👨‍💻 Autor

**Giancarlo Pittella**
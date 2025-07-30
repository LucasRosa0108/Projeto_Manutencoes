# 🛠️ Sistema de Manutenção - Projeto Escolar

Este é um aplicativo de manutenção empresarial desenvolvido como trabalho escolar. O sistema simula a gestão de manutenções **preditiva, preventiva e corretiva** em uma empresa fictícia, com interface moderna usando **Flet** e banco de dados **SQLite**.

---

## 📌 Funcionalidades

- 📋 Página de Máquinas: Visualiza todas as máquinas, tipo de manutenção e status.
- 🔧 Página de Manutenções:
  - ✅ Preventiva: Explicação + tabela + adicionar/remover máquinas.
  - ❌ Corretiva: Explicação + tabela + adicionar/remover máquinas.
  - 📊 Preditiva: Explicação + status com cores (verde, amarelo, vermelho, roxo, azul, preto).
- 🏢 Sobre a empresa fictícia.
- 🚪 Botão para sair do programa.
- 📎 Navegação com botões de voltar e menu.
- 📌 Nomes dos integrantes do grupo fixados na interface.

---

## 💻 Tecnologias Usadas

- Python 3
- Flet
- SQLite (banco de dados offline)

---

## 🚀 Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o aplicativo

```bash
python main.py
```

---

## 📦 Como gerar o executável

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

O executável estará na pasta `dist/`.

---

## 📄 Licença

Este projeto é apenas para fins educacionais.

---

---

# 🛠️ Maintenance System - School Project

This is a business maintenance application developed as a school project. The system simulates the management of **predictive, preventive, and corrective maintenance** in a fictional company, with a modern interface using **Flet** and **SQLite** database.

---

## 📌 Features

- 📋 Machines Page: View all machines, maintenance type, and operational status.
- 🔧 Maintenance Page:
  - ✅ Preventive: Explanation + table + add/remove machines.
  - ❌ Corrective: Explanation + table + add/remove machines.
  - 📊 Predictive: Explanation + color status (green, yellow, red, purple, blue, black).
- 🏢 About the fictitious company.
- 🚪 Exit program button.
- 📎 Navigation with back and menu buttons.
- 📌 Group member names fixed on the interface.

---

## 💻 Technologies Used

- Python 3
- Flet
- SQLite (offline database)

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-user/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 📦 How to build the executable

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be inside the `dist/` folder.

---

## 📄 License

This project is for educational purposes only.

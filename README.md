# 🗄️ BackupAppPro — Backup Automático Inteligente

<p align="center">
Proteja seus arquivos com backups automáticos, compactados e simples de configurar 🚀
</p>

<p align="center">
<a href="https://github.com/miguelofc/BackupAppPro">
<img src="https://img.shields.io/github/repo-size/miguelofc/BackupAppPro?style=for-the-badge">
</a>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/python-3.14-blue?style=for-the-badge">
</a>
<a href="LICENSE">
<img src="https://img.shields.io/github/license/miguelofc/BackupAppPro?style=for-the-badge">
</a>
</p>

---

📌 *Click here for English version*:  
➡️ [`README-EN.md`](README-EN.md)

---

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Automação de Backup](#-automação-de-backup)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 🚀 Sobre o Projeto

O **BackupAppPro** é um sistema de backup automático em **Python**, com:

✔ Execução manual ou automática  
✔ Interface gráfica (GUI) amigável  
✔ Compactação em `.zip`  
✔ Logs detalhados  
✔ Backup incremental eficiente  

Simples e seguro para qualquer usuário!

---

## 🔧 Funcionalidades

- ✅ Backup automático e incremental
- ✅ Compactação ZIP
- ✅ Seleção simples de pastas pela GUI
- ✅ Log de execução (`backup.log`)
- ✅ Script CLI para execução rápida
- ✅ Automação via cron/Task Scheduler

---

## 💻 Instalação

```bash
git clone https://github.com/miguelofc/BackupAppPro.git
cd BackupAppPro

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt


⸻

🖥️ Como Usar

▶️ Modo Gráfico (GUI)

python3 backup_gui_pro.py

✅ Seleção das pastas
✅ Botão para iniciar o backup
✅ Logs na interface

⸻

🧑‍💻 Modo Terminal

python3 backup_auto.py


⸻

⏱️ Automação de Backup

Cron — a cada 2 minutos (Linux/macOS)

*/2 * * * * /usr/bin/python3 /caminho/BackupAppPro/backup_auto.py

📌 Substitua o caminho conforme seu sistema

⸻

📂 Estrutura do Projeto

BackupAppPro/
├── backup_auto.py
├── backup_gui_pro.py
├── run_backup.sh
├── backup.log
├── requirements.txt
└── README.md


⸻

👤 Autor

Miguel Ângelo Moraes de Almeida
📧 miguelofc29@gmail.com
📍 Pernambuco - Brasil

⸻

🛡️ Licença

Distribuído sob MIT License — consulte o arquivo LICENSE.

⸻

“Automatizar é dar mais tempo ao que realmente importa.”
— BackupAppPro 🚀

---

# 🌎 `README-EN.md` — Inglês 🇺🇸

> ✅ Fica ao lado do README principal, com link cruzado

```md
# 🗄️ BackupAppPro — Smart Automatic Backup System

<p align="center">
Keep your files safe with automated and compressed backups, easy to set up 🚀
</p>

<p align="center">
<a href="https://github.com/miguelofc/BackupAppPro">
<img src="https://img.shields.io/github/repo-size/miguelofc/BackupAppPro?style=for-the-badge">
</a>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/python-3.14-blue?style=for-the-badge">
</a>
<a href="LICENSE">
<img src="https://img.shields.io/github/license/miguelofc/BackupAppPro?style=for-the-badge">
</a>
</p>

---

📌 *Versão em Português*:  
➡️ [`README.md`](README.md)

---

## 📑 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Backup Automation](#-backup-automation)
- [Project Structure](#-project-structure)
- [Author](#-author)
- [License](#-license)

---

## 🚀 About

**BackupAppPro** is an automated backup tool built with **Python**, featuring:

✔ Manual or automated execution  
✔ Graphical User Interface  
✔ ZIP compression  
✔ Detailed logs  
✔ Smart incremental backup system

Fast and secure for anyone!

---

## 🔧 Features

- ✅ Automatic and incremental backup
- ✅ ZIP compression
- ✅ GUI folder selection
- ✅ Execution logs (`backup.log`)
- ✅ CLI for batch usage
- ✅ Cron/Task Scheduler compatible

---

## 💻 Installation

```bash
git clone https://github.com/miguelofc/BackupAppPro.git
cd BackupAppPro

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt


⸻

🖥️ How to Use

▶️ GUI Mode

python3 backup_gui_pro.py

🧑‍💻 Command Line Mode

python3 backup_auto.py


⸻

⏱️ Backup Automation

Cron — every 2 minutes (Linux/macOS)

*/2 * * * * /usr/bin/python3 /path/BackupAppPro/backup_auto.py


⸻

📂 Project Structure

BackupAppPro/
├── backup_auto.py
├── backup_gui_pro.py
├── run_backup.sh
├── backup.log
├── requirements.txt
└── README.md


⸻

👤 Author

Miguel Ângelo Moraes de Almeida
📧 miguelofc29@gmail.com
📍 Pernambuco - Brazil

⸻

🛡️ License

Released under the MIT License — see LICENSE.

⸻

“Automation is freedom to focus on what truly matters.”
— BackupAppPro 🚀

---

## ✅ O que fazer agora?

Basta colar esses arquivos no seu repositório e rodar:

```bash
git add README.md README-EN.md
git commit -m "Refatoração visual do README + versão em inglês"
git push origin main


⸻
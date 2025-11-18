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

- Execução manual ou automática  
- Interface gráfica (GUI) amigável  
- Compactação em `.zip`  
- Logs detalhados  
- Backup incremental eficiente  

Simples, seguro e confiável!

---

## 🔧 Funcionalidades

<div align="center">

| Funcionalidade | Descrição |
|----------------|-----------|
| Backup automático | Executa backups sem intervenção do usuário |
| Backup incremental | Salva apenas alterações para economizar espaço |
| GUI amigável | Seleção de pastas e monitoramento em tempo real |
| Log detalhado | Histórico completo de cada execução |
| CLI | Backup rápido via terminal |
| Automação | Compatível com Cron ou Task Scheduler |

</div>

---

## 💻 Instalação

<pre>
1️⃣ Clonar o repositório:

git clone https://github.com/miguelofc/BackupAppPro.git
cd BackupAppPro

2️⃣ Instalar dependências:

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
</pre>

---

## 🖥️ Como Usar

### ▶️ Modo Gráfico (GUI)

```bash
python3 backup_gui_pro.py
```

- Selecione pastas de origem e destino  
- Clique em iniciar backup  
- Visualize os logs em tempo real  

### 🧑‍💻 Modo Terminal (CLI)

```bash
python3 backup_auto.py
```

- Executa backup rápido sem GUI  

---

## ⏱️ Automação de Backup

### Cron — a cada 2 minutos (Linux/macOS)

```bash
*/2 * * * * /usr/bin/python3 /caminho/BackupAppPro/backup_auto.py
```

📌 Substitua o caminho conforme seu sistema

---

## 📂 Estrutura do Projeto

```
BackupAppPro/
├── backup_auto.py       # Script principal do backup
├── backup_gui_pro.py    # Interface gráfica (GUI)
├── run_backup.sh        # Loop de execução automática
├── backup.log           # Log do backup
├── requirements.txt     # Dependências Python
└── README.md            # Documentação
```

---

## 👤 Autor

**Miguel Ângelo Moraes de Almeida**  
📧 miguelofc29@gmail.com  
📍 Pernambuco - Brasil  

---

---

> “Automatizar é dar mais tempo ao que realmente importa.”  
> — BackupAppPro 🚀

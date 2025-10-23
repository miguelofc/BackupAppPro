Perfeito! 😎 Vou gerar um README.md completo, profissional e “all-in-one”, com todos os badges possíveis, instruções passo a passo, links clicáveis e formatação pronta para GitHub. Você poderá copiar tudo de uma vez e colocar no seu repositório.

⸻


# 🗄️ BackupAppPro

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/seuusuario/BackupAppPro/backup.yml?branch=main&style=for-the-badge)
![GitHub Repo Size](https://img.shields.io/github/repo-size/seuusuario/BackupAppPro?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.14-blue?style=for-the-badge)
![License](https://img.shields.io/github/license/seuusuario/BackupAppPro?style=for-the-badge)
![Build Status](https://img.shields.io/jenkins/build?jobUrl=http://localhost:8080/job/BackupAppPro-Pipeline&style=for-the-badge)

---

## 🚀 Visão Geral

**BackupAppPro** é um sistema de backup automático em **Python 3.14**, com **GUI (Tkinter)** opcional, **integração com Google Drive via Rclone**, logs detalhados e automação via **GitHub + Jenkins**.  

O objetivo é fornecer **segurança, confiabilidade e simplicidade** para usuários que precisam proteger arquivos importantes com backups incrementais e compactados.

---

## 🧩 Funcionalidades

- ✅ Backup incremental automático  
- ✅ Compactação em `.zip`  
- ✅ Envio para Google Drive via `rclone`  
- ✅ GUI intuitiva para seleção de pastas e monitoramento  
- ✅ Execução manual ou automática (cron/task scheduler)  
- ✅ Logs detalhados (`backup.log` e `run_backup.log`)  
- ✅ Integração com GitHub e Jenkins para CI/CD  
- ✅ Notificação via Telegram (opcional)  

---

## 🗂️ Estrutura do Projeto

BackupAppPro/
├── backup_auto.py          # Script principal de backup
├── backup_gui_pro.py       # GUI (Tkinter)
├── run_backup.sh           # Loop de execução automática
├── backup.log              # Log do backup
├── run_backup.log          # Log do loop shell
├── Jenkinsfile             # Pipeline Jenkins
├── requirements.txt        # Dependências Python (opcional)
└── README.md               # Documentação

---

## 💻 Requisitos

- macOS 12+ ou Linux (Python 3.10+)  
- Python 3.14 (recomendado)  
- Rclone (`brew install rclone` ou equivalente)  
- Git  
- (Opcional) Jenkins LTS  
- (Opcional) Token do Telegram para notificações  

---

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/BackupAppPro.git
cd BackupAppPro

2. Instalar dependências

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

3. Configurar Rclone (Google Drive)

rclone config

	•	Crie uma configuração chamada gdrive e autentique com sua conta Google.

⸻

🖥️ Usando a GUI

python3 backup_gui_pro.py

Funcionalidades:
	•	Seleção de pasta de origem
	•	Seleção de pasta de destino
	•	Início do backup manual
	•	Visualização de logs em tempo real

⸻

🖥️ Usando o CLI / Automação

Executar manualmente:

python3 backup_auto.py

Executar em loop a cada 2 minutos:

bash run_backup.sh


⸻

🌐 Integração GitHub
	•	Crie um repositório no GitHub chamado BackupAppPro
	•	Suba seu projeto:

git init
git add .
git commit -m "Versão inicial"
git branch -M main
git remote add origin https://github.com/seuusuario/BackupAppPro.git
git push -u origin main


⸻

🤖 Integração Jenkins

1. Instalar Jenkins

brew install jenkins-lts
brew services start jenkins-lts

Acesse: http://localhost:8080

⸻

2. Configurar Job Pipeline
	•	Novo Item → Pipeline → Nome: BackupAppPro-Pipeline
	•	Pipeline → Script from SCM → Git → URL do repositório → Branch: main → Jenkinsfile

⸻

3. Jenkinsfile

pipeline {
    agent any

    environment {
        PYTHON = '/Library/Frameworks/Python.framework/Versions/3.14/bin/python3'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/seuusuario/BackupAppPro.git'
            }
        }
        stage('Instalar dependências') {
            steps {
                sh '''
                ${PYTHON} -m pip install --upgrade pip || true
                ${PYTHON} -m pip install -r requirements.txt || true
                '''
            }
        }
        stage('Rodar Backup') {
            steps {
                sh '${PYTHON} backup_auto.py'
            }
        }
        stage('Arquivar Logs') {
            steps {
                archiveArtifacts artifacts: '*.log', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            script {
                def TELEGRAM_TOKEN = credentials('telegram-token')
                def CHAT_ID = credentials('telegram-chatid')
                sh '''
                LAST6=$(tail -n 6 backup.log | sed "s/'/\"/g")
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \
                     -d chat_id=${CHAT_ID} \
                     -d text="✅ BackupAppPro concluído com sucesso! Últimas 6 linhas:\n$LAST6" \
                     -d parse_mode=Markdown
                '''
            }
        }
        failure {
            script {
                def TELEGRAM_TOKEN = credentials('telegram-token')
                def CHAT_ID = credentials('telegram-chatid')
                sh '''
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \
                     -d chat_id=${CHAT_ID} \
                     -d text="❌ BackupAppPro falhou. Verifique o Jenkins." \
                     -d parse_mode=Markdown
                '''
            }
        }
    }
}


⸻

⏱️ Agendamento (Cron / Jenkins)

Exemplo cron para rodar todo dia às 02:00:

0 2 * * * /usr/bin/python3 /caminho/para/BackupAppPro/backup_auto.py

Jenkins (Build Periodic)

H/2 * * * *  # Executa a cada 2 minutos


⸻

🗂️ Logs
	•	backup.log → registro detalhado do backup
	•	run_backup.log → log do loop shell
	•	Jenkins Console → log completo de execução

⸻

🧠 Dicas Avançadas
	•	Use pyinstaller --onefile --windowed backup_gui_pro.py para gerar .app no macOS
	•	Faça commits frequentes no GitHub
	•	Configure alertas adicionais (Slack, e-mail) no Jenkins

⸻

🧑‍💻 Autor

Miguel Ângelo Moraes de Almeida
📍 Pernambuco, Brasil
💻 GitHub | 📧 miguelofc29@gmail.com 

⸻

🛡️ Licença

MIT License — veja LICENSE

⸻

“Automatizar é libertar tempo para o que realmente importa.”
— BackupAppPro

---

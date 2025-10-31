🗄️ BackupAppPro


⸻

🚀 Visão Geral

BackupAppPro é um sistema de backup automático em Python 3.14, com GUI (Tkinter) opcional, Google Drive via Rclone, logs detalhados e automação com GitHub e Jenkins.

✔ Backup seguro e automatizado
✔ Pensado para usuários e empresas

⸻

🧩 Funcionalidades
	•	✅ Backup incremental automático
	•	✅ Compactação em .zip
	•	✅ Upload para Google Drive com rclone
	•	✅ Interface gráfica para facilitar o uso
	•	✅ Execução automática via cron/Task Scheduler
	•	✅ Logs completos (backup.log + run_backup.log)
	•	✅ Integração com CI/CD (GitHub Actions + Jenkins)
	•	✅ Notificações via Telegram (opcional)

⸻

🗂️ Estrutura do Projeto

BackupAppPro/
├── backup_auto.py          # Script principal de backup
├── backup_gui_pro.py       # GUI em Tkinter
├── run_backup.sh           # Execução em loop
├── backup.log              # Log do backup
├── run_backup.log          # Log do script de loop
├── Jenkinsfile             # Pipeline Jenkins
├── requirements.txt        # Dependências Python
└── README.md               # Documentação


⸻

💻 Requisitos
	•	macOS 12+ ou Linux
	•	Python 3.10+ (recomendado 3.14)
	•	Rclone

 brew install rclone


	•	Git
	•	(Opcional) Jenkins LTS
	•	(Opcional) Token e Chat ID do Telegram

⸻

⚙️ Instalação

1️⃣ Clonar o repositório

git clone https://github.com/seuusuario/BackupAppPro.git
cd BackupAppPro

2️⃣ Instalar dependências

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

3️⃣ Configurar Google Drive via Rclone

rclone config

Crie um remote chamado gdrive e autentique sua conta Google.

⸻

🖥️ Uso com Interface Gráfica

python3 backup_gui_pro.py

✔ Seleção de pastas
✔ Backup manual
✔ Logs em tempo real

⸻

🖥️ Uso por Linha de Comando / Automação

Execução manual:

python3 backup_auto.py

Loop automático a cada 2 minutos:

bash run_backup.sh


⸻

🌐 Integração com GitHub

Criar versionamento e subir para GitHub:

git init
git add .
git commit -m "Versão inicial"
git branch -M main
git remote add origin https://github.com/seuusuario/BackupAppPro.git
git push -u origin main


⸻

🤖 Integração com Jenkins

Instalar Jenkins (macOS)

brew install jenkins-lts
brew services start jenkins-lts

Acesse: http://localhost:8080

⸻

Pipeline no Jenkins
	•	Criar novo job → Pipeline
	•	Selecionar “Script from SCM” → Git
	•	Informar repositório + branch main
	•	Usar o Jenkinsfile abaixo 👇

pipeline {
    agent any

    environment {
        PYTHON = 'python3'
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
                ${PYTHON} -m pip install --upgrade pip
                ${PYTHON} -m pip install -r requirements.txt
                '''
            }
        }
        stage('Executar Backup') {
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
}


⸻

⏱️ Agendamentos

Cron — Executar todo dia às 02:00

0 2 * * * /usr/bin/python3 /caminho/BackupAppPro/backup_auto.py

Jenkins — Cada 2 minutos

H/2 * * * *


⸻

🗂️ Logs
	•	backup.log → Relatório do backup
	•	run_backup.log → Execução da automação shell
	•	Jenkins Console → CI/CD detalhado

⸻

🧠 Dicas Avançadas
	•	Transformar em app macOS:

 pyinstaller --onefile --windowed backup_gui_pro.py


	•	Adicionar notificações (Telegram, Slack, Email)
	•	Upload para S3, FTP ou servidores remotos via Rclone

⸻

👤 Autor

Miguel Ângelo Moraes de Almeida
📌 Pernambuco - Brasil
📧 miguelofc29@gmail.com

⸻

“Automatizar é libertar tempo para o que realmente importa.”
— BackupAppPro

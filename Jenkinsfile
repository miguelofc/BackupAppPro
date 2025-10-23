pipeline {
    agent any

    environment {
        PYTHON = '/Library/Frameworks/Python.framework/Versions/3.14/bin/python3'
        RCLONE = '/opt/homebrew/bin/rclone' // <-- caminho absoluto do rclone (ajuste se necessário)
    }

    stages {
        stage('Clonar do GitHub') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/miguelofc/BackupAppPro.git', 
                    credentialsId: 'github-token'
            }
        }

        stage('Instalar dependências (opcional)') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    echo "Instalando dependências..."
                    ${PYTHON} -m pip install --upgrade pip || true
                    ${PYTHON} -m pip install -r requirements.txt || true
                else
                    echo "Nenhum requirements.txt encontrado, pulando instalação de dependências."
                fi
                '''
            }
        }

        stage('Executar Backup') {
            steps {
                sh """
                echo "=== Rodando backup_auto.py ==="
                ${PYTHON} backup_auto.py
                echo "=== backup_auto.py finalizado ==="
                """
            }
        }

        stage('Commit logs') {
            steps {
                sh '''
                git config user.email "jenkins@localhost" || true
                git config user.name "Jenkins CI" || true
                git add backup.log || true
                git commit -m "Atualiza backup.log - ${BUILD_ID}" || true
                git push origin main || true
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Backup concluído com sucesso!'
        }
        failure {
            echo '❌ Falha no pipeline. Verifique os logs!'
        }
    }
}

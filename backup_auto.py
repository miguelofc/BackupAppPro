import os
import sys
import subprocess
from datetime import datetime
import logging

# ------------------------------------------------
# Se o usuário escolher uma pasta, ela vem via argumento
# ------------------------------------------------
if len(sys.argv) > 1:
    origem = sys.argv[1]
else:
    origem = "/Users/miguel/Documents/projetos"  # Caminho padrão (caso não passe nada)

destino_base = "/Users/miguel/Backups"

# ------------------------------------------------
# Configuração de logs
# ------------------------------------------------
log_dir = "/Users/miguel/BackupAppPro"
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "backup.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ------------------------------------------------
# Nome do backup com data e hora
# ------------------------------------------------
data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
destino = os.path.join(destino_base, f"backup_{data_atual}")

try:
    # Cria pasta destino
    os.makedirs(destino, exist_ok=True)

    # Backup incremental
    cmd = ["rsync", "-a", "--delete", f"{origem}/", f"{destino}/"]
    subprocess.run(cmd, check=True)
    print(f"✅ Backup incremental criado: {destino}")
    logging.info(f"Backup incremental criado: {destino}")

    # Compacta o backup
    zip_file = f"{destino}.zip"
    subprocess.run(["zip", "-r", zip_file, destino], check=True)
    print(f"📦 Backup compactado em: {zip_file}")
    logging.info(f"Backup compactado: {zip_file}")

    # Envia para o Google Drive via Rclone
    print("☁️ Enviando backup para o Google Drive...")
    subprocess.run(["rclone", "copy", zip_file, "gdrive:BackupAppPro/"], check=True)
    print("✅ Upload concluído com sucesso!")
    logging.info(f"Upload concluído: {zip_file}")

    # Notificação no macOS
    os.system(f'''osascript -e 'display notification "Backup concluído e enviado à nuvem com sucesso!" with title "BackupAppPro"' ''')

except subprocess.CalledProcessError as e:
    print("⚠️ Erro durante o processo de backup:", e)
    logging.error(f"Erro durante o processo: {e}")

except Exception as e:
    print("❌ Erro inesperado:", e)
    logging.error(f"Erro inesperado: {e}")

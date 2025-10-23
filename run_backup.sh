#!/bin/bash
# -------------------------------------------
# Script de execução automática do BackupAppPro
# Faz o backup a cada 2 minutos e registra logs
# -------------------------------------------

# Caminho do script Python
SCRIPT="/Users/miguel/BackupAppPro/backup_auto.py"
LOG="/Users/miguel/BackupAppPro/run_backup.log"

echo "🚀 Iniciando execução automática do BackupAppPro..."
echo "-----------------------------------------------" >> "$LOG"

# Loop infinito (roda continuamente)
while true; do
    echo "⏰ $(date '+%Y-%m-%d %H:%M:%S') - Executando backup..." | tee -a "$LOG"
    
    # Executa o backup com Python 3
    /usr/bin/python3 "$SCRIPT" >> "$LOG" 2>&1
    
    echo "✅ Backup finalizado às $(date '+%H:%M:%S')" | tee -a "$LOG"
    echo "-----------------------------------------------" >> "$LOG"
    
    # Espera 2 minutos (120 segundos)
    sleep 120
done

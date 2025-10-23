import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import time
import os

# -----------------------------
# Caminhos padrões
# -----------------------------
SCRIPT_BACKUP = "/Users/miguel/BackupAppPro/backup_auto.py"
LOG_FILE = "/Users/miguel/BackupAppPro/backup.log"
origem_padrao = "/Users/miguel/Documents/projetos"

# Variável para armazenar a pasta escolhida
origem = origem_padrao

# -----------------------------
# Função para escolher pasta
# -----------------------------
def escolher_pasta():
    global origem
    pasta = filedialog.askdirectory(initialdir=origem, title="Selecione a pasta para backup")
    if pasta:
        origem = pasta
        pasta_label.config(text=f"Pasta selecionada: {origem}")

# -----------------------------
# Função para rodar backup
# -----------------------------
def iniciar_backup():
    def rodar():
        status_label.config(text="⏳ Backup em andamento...")
        barra_progresso.start(10)  # inicia barra animada
        try:
            subprocess.run(["python3", SCRIPT_BACKUP, origem], check=True)
            status_label.config(text="✅ Backup concluído!")
        except subprocess.CalledProcessError as e:
            status_label.config(text=f"❌ Erro no backup: {e}")
        finally:
            barra_progresso.stop()
    
    threading.Thread(target=rodar, daemon=True).start()

# -----------------------------
# Função para atualizar logs
# -----------------------------
def atualizar_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            log_text.delete(1.0, tk.END)
            log_text.insert(tk.END, f.read())
            log_text.see(tk.END)
    root.after(2000, atualizar_logs)

# -----------------------------
# Função de agendamento
# -----------------------------
def agendar_backup():
    try:
        intervalo = int(intervalo_entry.get())
        if intervalo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Atenção", "Digite um intervalo válido em minutos!")
        return

    def backup_periodico():
        while True:
            subprocess.run(["python3", SCRIPT_BACKUP, origem])
            status_label.config(text=f"✅ Backup automático concluído em {time.strftime('%H:%M:%S')}")
            time.sleep(intervalo * 60)
    
    threading.Thread(target=backup_periodico, daemon=True).start()
    messagebox.showinfo("Agendamento", f"Backup agendado a cada {intervalo} minutos.")

# -----------------------------
# Interface gráfica
# -----------------------------
root = tk.Tk()
root.title("BackupAppPro PRO")
root.geometry("700x600")
root.resizable(False, False)

# Botão de escolher pasta
tk.Button(root, text="Escolher Pasta", command=escolher_pasta, font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=10)
pasta_label = tk.Label(root, text=f"Pasta selecionada: {origem}", font=("Arial", 10))
pasta_label.pack(pady=5)

# Botão de backup manual
tk.Button(root, text="Fazer Backup Agora", command=iniciar_backup, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Agendamento
frame_agendamento = tk.Frame(root)
frame_agendamento.pack(pady=10)
tk.Label(frame_agendamento, text="Agendar backup (minutos):", font=("Arial", 10)).pack(side="left")
intervalo_entry = tk.Entry(frame_agendamento, width=8, font=("Arial", 10))
intervalo_entry.pack(side="left", padx=5)
tk.Button(frame_agendamento, text="Agendar Backup Automático", command=agendar_backup, font=("Arial", 10), bg="#2196F3", fg="white").pack(side="left")

# Status
status_label = tk.Label(root, text="", font=("Arial", 11))
status_label.pack(pady=5)

# Barra de progresso
barra_progresso = ttk.Progressbar(root, orient="horizontal", length=500, mode="indeterminate")
barra_progresso.pack(pady=10)

# Logs
tk.Label(root, text="Logs do backup:", font=("Arial", 10)).pack()
log_text = tk.Text(root, width=80, height=20, font=("Arial", 9))
log_text.pack(pady=5)

# Atualiza logs automaticamente
atualizar_logs()

# Inicia interface
root.mainloop()

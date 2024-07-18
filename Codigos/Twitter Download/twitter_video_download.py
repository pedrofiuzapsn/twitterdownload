import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp as youtube_dl

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def download_video():
    tweet_url = url_entry.get()
    save_directory = directory_entry.get()
    
    if not tweet_url:
        messagebox.showerror("Erro", "Por favor, insira o URL do tweet")
        return
    
    if not save_directory:
        messagebox.showerror("Erro", "Por favor, selecione o diretório para salvar o vídeo")
        return
    
    try:
        ydl_opts = {
            'outtmpl': f'{save_directory}/%(title)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([tweet_url])
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeos do Twitter")

# Campo para o URL do tweet
tk.Label(root, text="URL do Tweet:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Campo para o diretório de download
tk.Label(root, text="Diretório de Download:").grid(row=1, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Procurar", command=browse_directory)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Botão de download
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=2, columnspan=3, pady=20)

root.mainloop()

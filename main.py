import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import cv2

from cisterciense_drawer import desenhar_cisterciense
from cisterciense_reader import processar_quadrantes

def mostrar_imagem_pil(path, label):
    imagem = Image.open(path)
    imagem = imagem.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem)
    label.config(image=imagem_tk)
    label.image = imagem_tk

def gerar_e_mostrar():
    try:
        numero = int(entrada.get())
        img = desenhar_cisterciense(numero)
        caminho = f"output/{numero}_cisterciense.png"
        cv2.imwrite(caminho, img)
        mostrar_imagem_pil(caminho, label_saida)
        label_saida_texto.config(text=f"Cisterciense de: {numero}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro entre 1 e 9999")

def carregar_imagem():
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem cisterciense",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if caminho:
        mostrar_imagem_pil(caminho, label_entrada)
        numero_detectado = processar_quadrantes(caminho)
        label_entrada_texto.config(
            text=f"Imagem carregada:\n{os.path.basename(caminho)}\nNúmero detectado: {numero_detectado}"
        )

# Interface
janela = tk.Tk()
janela.title("Conversor Cisterciense")
janela.geometry("600x400")

# Entrada arábica
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)

botao_gerar = tk.Button(janela, text="Gerar Cisterciense", command=gerar_e_mostrar)
botao_gerar.pack()

# Label da imagem gerada
label_saida_texto = tk.Label(janela, text="Imagem Gerada", font=("Arial", 10))
label_saida_texto.pack()
label_saida = tk.Label(janela)
label_saida.pack()

# Separador
tk.Label(janela, text="—" * 60).pack(pady=5)

# Carregar imagem
botao_carregar = tk.Button(janela, text="Carregar imagem para ler", command=carregar_imagem)
botao_carregar.pack()

label_entrada_texto = tk.Label(janela, text="Imagem Carregada", font=("Arial", 10))
label_entrada_texto.pack()
label_entrada = tk.Label(janela)
label_entrada.pack()

janela.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import cv2

from cisterciense_drawer import desenhar_cisterciense
from cisterciense_reader import processar_quadrantes

if not os.path.exists("output"):
    os.makedirs("output")

def mostrar_imagem_pil(path, label):
    imagem = Image.open(path)
    imagem = imagem.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_img = tk.Label(image=imagem_tk)
    label_img.image = imagem_tk  # Manter referência para evitar garbage collection
    label_img.pack()

    label_valor = tk.Label(text=label, font=("Arial", 10))
    label_valor.pack()

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
        # Limpar imagens e textos anteriores
        for widget in frame_imagens.winfo_children():
            widget.destroy()
        label_entrada_texto.config(text="")
        label_entrada.config(image="")

        valores_detectados = processar_quadrantes(caminho)

        # Criar imagens para cada valor detectado
        imagens = {}
        for quadrante, valor in valores_detectados.items():
            if valor > 0:  # Apenas gerar se o valor for maior que 0
                img = desenhar_cisterciense(valor, (0, 0, 255))
                imagens[quadrante] = (img, valor)

        # Exibir as imagens menores (unidades, dezenas, centenas, milhares) lado a lado
        texto_resultado = f"Imagem carregada:\n{os.path.basename(caminho)}\n"
        total_valor = 0
        for quadrante, (img, valor) in imagens.items():
            # Converter a imagem OpenCV para PIL para exibição
            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            img_pil = img_pil.resize((100, 100))  # Redimensionar para exibição
            img_tk = ImageTk.PhotoImage(img_pil)

            # Criar um frame para cada imagem e seu texto
            frame_individual = tk.Frame(frame_imagens)
            frame_individual.pack(side=tk.LEFT, padx=5)

            # Criar um label para a imagem
            label_img = tk.Label(frame_individual, image=img_tk)
            label_img.image = img_tk  # Manter referência para evitar garbage collection
            label_img.pack()

            # Criar um label para o valor correspondente
            label_valor = tk.Label(frame_individual, text=f"{quadrante.capitalize()}: {valor}", font=("Arial", 10))
            label_valor.pack()

            # texto_resultado += f"{quadrante.capitalize()}: {valor}\n"
            total_valor += valor

        # Atualizar o texto com os valores detectados e o valor total
        label_entrada_texto.config(text=texto_resultado)
        mostrar_imagem_pil(caminho, f"Valor Total: {total_valor}\n")


# Interface
janela = tk.Tk()
janela.title("Conversor Cisterciense")
janela.geometry("800x600")

# Adicionar o frame_imagens globalmente para reutilização


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

frame_imagens = tk.Frame(janela)
frame_imagens.pack(pady=10)

janela.mainloop()

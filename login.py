# Jogo da Velha versão 0.2
# Grupo: Camilo Sidou, Elton Jonathas da Silva, Reine Santos

from tkinter import *
from PIL import ImageTk, Image

# Janela principal (root):
root = Tk()
root.title('Jogo da Velha - Versão 0.2')
root.configure(background="#8986D8")
root.geometry("600x300")

# Frame esquerdo para a imagem
fr_esquerdo = Frame(root, bg="white")
fr_esquerdo.grid(row=0, column=0)

# Frame direito para os demais widgets
fr_direito = Frame(root, bg="#8986D8")
fr_direito.grid(row=0, column=1)

# Imagem esquerda
img = ImageTk.PhotoImage(Image.open("old_day.png").resize((300, 300)))
panel = Label(fr_esquerdo, image=img, bg="white")
panel.pack()

# Label Nome de usuário
lb_username = Label(fr_direito, text="Nome de usuário", font=("Helvetica", 18), fg="black", bg="#8986D8")
lb_username.grid(row=0, column=0, padx=50, pady=10)

# Caixa de texto para o nome de usuário
tb_username = Text(fr_direito, width=10, height=1, font=("Helvetica", 18))
tb_username.grid(row=1, column= 0, padx=50, pady=10)

# Botão iniciar
btt_iniciar = Button(fr_direito, text="Iniciar")
btt_iniciar.grid(row=2, column=0, padx=50, pady=10)

root.mainloop()
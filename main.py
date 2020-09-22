from tkinter import *
from tkinter import messagebox

# Janela principal (root):
root = Tk()
root.title('Jogo da Velha - Versão 0.1')

# Variáveis globais:
vencedor = ''
fim = False

# Turno
turno_x = True
count = 0
turno = Label(root, text='Turno: X', font=("Helvetica", 14), height=3, width=8)

# Funções dos botões:
def b_clickd(b):
    global turno_x, count
    
    if b['text'] == ' ' and turno_x is True:
        b['text'] = 'X'
        turno_x = False
        count += 1
        turno['text'] = 'Turno: O'
    elif b['text'] == ' ' and turno_x is False:
        b['text'] = 'O'
        turno_x = True
        count += 1
        turno['text'] = 'Turno: X'
    else:
        messagebox.showerror("Erro!", "Espaço já preenchido.\nEscolha outra posição!")
    check_end()

# Funções da lógica do jogo:
def end_game(winner):
    global fim
    fim = True
    vencedor = winner
    messagebox.showinfo("Fim de jogo", vencedor + ' venceu!')
    desabilitar_botoes()

def check_end():
    global vencedor, fim
    global b1, b2, b3
    global b4, b5, b6
    global b7, b8, b9

    # check linhas:
    if b1['text'] == b2['text'] and b2['text'] == b3['text'] and b1['text'] != ' ':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        end_game(b1['text'])
    elif b4['text'] == b5['text'] and b5['text'] == b6['text'] and b4['text'] != ' ':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        end_game(b4['text'])
    elif b7['text'] == b8['text'] and b8['text'] == b9['text'] and b7['text'] != ' ':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        end_game(b7['text'])
    # check colunas:
    elif b1['text'] == b4['text'] and b4['text'] == b7['text'] and b1['text'] != ' ':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        end_game(b1['text'])
    elif b2['text'] == b5['text'] and b5['text'] == b8['text'] and b2['text'] != ' ':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        end_game(b2['text'])
    elif b3['text'] == b6['text'] and b6['text'] == b9['text'] and b3['text'] != ' ':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        end_game(b3['text'])
    # check tranversais:
    elif b1['text'] == b5['text'] and b5['text'] == b9['text'] and b1['text'] != ' ':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        end_game(b1['text'])
    elif b7['text'] == b5['text'] and b5['text'] == b3['text'] and b7['text'] != ' ':
        b7.config(bg='red')
        b5.config(bg='red')
        b3.config(bg='red')
        end_game(b7['text'])
    else:
        if count >= 9:
            end_game('Ninguém')

# Funções de funcionalidade do jogo:
def desabilitar_botoes():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def reiniciar_jogo():
    global count, turno_x
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, turno

    count = 0
    turno_x = True

    # Definir os botões:
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg='#fff', command=lambda: b_clickd(b9)) 

    # Grid dos botões:
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    turno['text'] = 'Turno: X'
    turno.grid(row=3)

# Menu do jogo:
menu = Menu(root)
root.config(menu=menu)

# Opções do menu:
opcoes_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Opções', menu=opcoes_menu)

opcoes_menu.add_command(label='Reiniciar jogo', command=reiniciar_jogo)

# Executa a janela:
reiniciar_jogo()
root.mainloop()
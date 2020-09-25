# Jogo da Velha versão 0.1
# Grupo: Camilo Sidou, Elton Jonathas da Silva, Reine Santos

'''
    Justificativas:

    1. Motivação para o uso da linguagem escolhida:
    R: Escolhemos a linguagem Python por ser uma linguagem que, em primeiro lugar, todos os integrantes dominavam. Além disso, por ser uma linguage OO, permite a modularização das instâncias dos jogos em Classes, o que será implementado futuramente. Por fim, possui todas as bibliotecas que precisaremos para implementar o projeto de forma nativa: Tkinter, para interface gráfica, Socket para a implementação da comunicação entre programas e computadores.

    2. Quais decisões de projeto estão alinhadas com futuras versões?
    R: Utilizaremos para as futuras versões uma arquitetura cliente-servidor, separando a lógica do jogo da sua interface. Utilizaremos sockets para implementar a comunicação com o protocolo TCP por sua confiabilidade, estabelecendo os demais protocolos para a validação das jogadas, monitoramento das partidas, etc. Também utilizaremos um banco de dados SQLite para guarda as informações necessárias e manter a integridade das informações das partidas e dos jogadores.

    3. Avalie a atual interface e indique de que forma ela pode evoluir para responder a escala maiores de interação.
    R: A atual interface foi pensada para o ser o mais simples possível e precisa melhorar, tanto esteticamente quanto funcionalmente. Nas futuras versões, colocaremos a opção do jogador inserir o seu nome, bem como um Menu que terá as opções de jogar uma partida local (2 pessoas, 1 computador), uma partida direta com um jogador específico (que seria identificado através de um nome ou ID) ou jogar uma partida aleatória com qualquer jogador que também tenha escolhido uma partida aleatória e esteja aguardando um oponente num lobby de espera.

'''

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
turno = Label(root, text='Turno: X', font=("Helvetica", 14), height=2, width=0)

# Funções dos botões:
def b_clickd(b):
    global turno_x, count
    
    if b['text'] == ' ' and turno_x is True:
        b['text'] = 'C'
        turno_x = False
        count += 1
        turno['text'] = 'Turno: O'
    elif b['text'] == ' ' and turno_x is False:
        b['text'] = 'O'
        turno_x = True
        count += 1
        turno['text'] = 'Turno: C'
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
    b1 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b1))
    b2 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b2))
    b3 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b3))
    b4 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b4))
    b5 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b5))
    b6 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b6))
    b7 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b7))
    b8 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b8))
    b9 = Button(root, text=" ", font=("Symbol", 30, 'bold'), height=3, width=6, cursor='hand2', fg='#eee', bg='#222', command=lambda: b_clickd(b9)) 

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

opcoes_menu.add_command(label='Reiniciar', command=reiniciar_jogo)

# Executa a janela:
reiniciar_jogo()
root.mainloop()
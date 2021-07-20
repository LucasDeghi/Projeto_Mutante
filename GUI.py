import tkinter as tk
from Ambiente_do_Setor import *


HEIGHT = 400
WIDTH = 500

def formatar_resposta():
    dado = d66()
    resultado = ('Ambiente:', lista_resultados[dado]['Ambiente'], '\nRuina:', lista_resultados[dado]['Ruina'],
    '\nAmeaca:', lista_resultados[dado]['Ameaça'], '\nArtefato:', lista_resultados[dado]['Artefatos'])

    return resultado

def clean():
    label['text'] = []

def setor():


    Desafio_setor().Tipo_Ruina()
    Desafio_setor().nivel_podridao()
    Desafio_setor().nivel_ameaça()

    label['text'] = formatar_resposta()


def rafagay():
    clean()
    setor()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

imagem_de_fundo = tk.PhotoImage(file='./Campo de Batalha.png')
imagem_de_fundo_label = tk.Label(root, image=imagem_de_fundo)
imagem_de_fundo_label.place(x=0, y=0, relwidth=1, relheight=1)


frame = tk.Frame(root, bg="#ffcc00", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#entry = tk.Entry(frame, font=40)
#entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Make", font=15, command=lambda: setor())
button.place(relx=0.6, relheight=1, relwidth=0.3)

button = tk.Button(frame, text="Del", font=20, command=lambda: clean())
button.place(relx= 0.1, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#ffcc00", bd=10)
lower_frame.place(relx=0.5, rely=.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40)
label.place(relwidth = 1, relheight=1)



root.mainloop()

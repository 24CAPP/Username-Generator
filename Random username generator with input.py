import tkinter as tk
import itertools
import random
import time

def genera_username():
    random.seed()

    parole_input = [parola.get() for parola in parole]
    parole_input = [parola for parola in parole_input if parola]

    numero_input = numero.get()

    usernames = []

    for parola in parole_input:
        for i in range(len(parola) + 1):
            username = parola[:i] + numero_input + parola[i:] + str(random.randint(1, 10000))
            usernames.append(username)

    usernames = list(set(usernames))[:5]

    casella_username.delete(1.0, tk.END)
    for username in usernames:
        casella_username.insert(tk.END, username + '\n')

finestra = tk.Tk()
finestra.title("Generatore di Username")

parole = [tk.StringVar() for _ in range(2)]
numero = tk.StringVar()

for i in range(2):
    label = tk.Label(finestra, text=f"Parola {i+1}:")
    label.pack()
    casella = tk.Entry(finestra, textvariable=parole[i])
    casella.pack()

numero_label = tk.Label(finestra, text="Numero:")
numero_label.pack()
casella_numero = tk.Entry(finestra, textvariable=numero)
casella_numero.pack()

casella_username = tk.Text(finestra, height=10, width=30)
casella_username.pack(pady=10)

bottone_genera = tk.Button(finestra, text="Genera Username", command=genera_username)
bottone_genera.pack()

finestra.mainloop()

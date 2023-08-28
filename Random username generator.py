import tkinter as tk
import random
import string  # Importiamo il modulo 'string' per generare lettere minuscole

# Genera Username
def genera_username():
    lunghezza = 10  # Lunghezza predefinita dell'username
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(lunghezza))
    
    # Username generato
    casella_username.delete(1.0, tk.END)
    casella_username.insert(tk.END, username)

# Finestra principale
finestra = tk.Tk()
finestra.title("Generatore di Username")

# Casella username
casella_username = tk.Text(finestra, height=1, width=30)
casella_username.pack(pady=10)

# Bottone
bottone_genera = tk.Button(finestra, text="Genera Username", command=genera_username)
bottone_genera.pack()

# Esecuzione della finestra
finestra.mainloop()

import tkinter as tk
import os


def dodaj_biljesku():
    tekst = unos_biljeske.get()
    if tekst.strip():
        with open("biljeske.txt", "a", encoding="utf-8") as datoteka:
            datoteka.write(tekst + "\n")
        unos_biljeske.delete(0, tk.END)
        status_label.config(text="Bilješka spremljena.", fg="green")
    else:
        status_label.config(text="Molimo unesite neki tekst.", fg="red")


def otvori_biljeske():
    if os.path.exists("biljeske.txt"):
        with open("biljeske.txt", "r", encoding="utf-8") as datoteka:
            sadrzaj = datoteka.read().strip()
            if sadrzaj:
                biljeske_label.config(text=sadrzaj)
            else:
                biljeske_label.config(text="Nema unesenih bilješki.")
    else:
        biljeske_label.config(text="Datoteka s bilješkama ne postoji.")


def napravi_gui():
    global unos_biljeske, biljeske_label, status_label

    prozor = tk.Tk()
    prozor.title("Moja Bilježnica")
    prozor.geometry("400x400")

    tk.Label(prozor, text="Unesite novu bilješku:").pack(pady=5)

    unos_biljeske = tk.Entry(prozor, width=50)
    unos_biljeske.pack(pady=5)

    tk.Button(prozor, text="Spremi bilješku", command=dodaj_biljesku).pack(pady=5)
    tk.Button(prozor, text="Prikaži sve bilješke", command=otvori_biljeske).pack(pady=5)

    status_label = tk.Label(prozor, text="", fg="green")
    status_label.pack(pady=5)

    biljeske_label = tk.Label(prozor, text="", anchor="w", justify="left", wraplength=350)
    biljeske_label.pack(pady=10)

    prozor.mainloop()


napravi_gui()

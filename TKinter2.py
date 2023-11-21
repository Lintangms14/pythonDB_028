import tkinter as tk
from tkinter import ttk
import sqlite3

def klikButton():
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        hasil = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        hasil = "Teknik"
    else:
        hasil = "Bahasa"

    output_label.config(text=f"Prodi Pilihan: {hasil}")

    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            prediksi_fakultas TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, nilai_biologi, nilai_fisika, nilai_inggris, hasil))

    conn.commit()
    conn.close()

uiApp = tk.Tk()
uiApp.configure(background='white')
uiApp.geometry("400x400")
uiApp.resizable(False, False)
uiApp.title("Prediksi Prodi")

inputFrame = ttk.Frame(uiApp)
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)

input_label = ttk.Label(inputFrame, text="prediksi Prodi Pilihan")
input_label.pack(padx=10, pady=5, fill="x", expand=True)

label_nama = ttk.Label(inputFrame, text="Nama Siswa")
label_biologi = ttk.Label(inputFrame, text="Nilai Biologi")
label_fisika = ttk.Label(inputFrame, text="Nilai Fisika")
label_inggris = ttk.Label(inputFrame, text="Nilai Inggris")

entry_nama = ttk.Entry(inputFrame)
entry_biologi = ttk.Entry(inputFrame)
entry_fisika = ttk.Entry(inputFrame)
entry_inggris = ttk.Entry(inputFrame)

label_nama.pack(padx=10, pady=5, fill="x", expand=True)
entry_nama.pack(padx=10, pady=5, fill="x", expand=True)
label_biologi.pack(padx=10, pady=5, fill="x", expand=True)
entry_biologi.pack(padx=10, pady=5, fill="x", expand=True)
label_fisika.pack(padx=10, pady=5, fill="x", expand=True)
entry_fisika.pack(padx=10, pady=5, fill="x", expand=True)
label_inggris.pack(padx=10, pady=5, fill="x", expand=True)
entry_inggris.pack(padx=10, pady=5, fill="x", expand=True)

button_submit = ttk.Button(inputFrame, text="Submit Nilai", command=klikButton)
button_submit.pack(padx=10, pady=5, fill="x", expand=True)

output_label = tk.Label(inputFrame, text="Prodi Pilihan: -", font=("Helvetica", 12))
output_label.config(wraplength=600)
output_label.pack(padx=10, pady=5, fill="x", expand=True)

uiApp.mainloop()
import zipfile
import ttkbootstrap as tb
from tkinter import filedialog, messagebox

def select_zip():
    archivo = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if archivo:
        ruta_zip.set(archivo)

def select_destiny():
    carpeta = filedialog.askdirectory()
    if carpeta:
        ruta_destino.set(carpeta)

def extract_zip():
    zip_path = ruta_zip.get()
    dest_path = ruta_destino.get()

    if not zip_path or not dest_path:
        messagebox.showerror("Error", "Select ZIP file and a destiny folder.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
        messagebox.showinfo("Success", "ZIP extracted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't extract the ZIP file:\n{e}")

app = tb.Window(themename="flatly")
app.title("Extractor ZIP")

ruta_zip = tb.StringVar()
ruta_destino = tb.StringVar()

tb.Entry(app, textvariable=ruta_zip, width=50).pack(pady=5)
tb.Button(app, text="Select ZIP", command=select_zip).pack(pady=5)

tb.Entry(app, textvariable=ruta_destino, width=50).pack(pady=5)
tb.Button(app, text="Select Destiny", command=select_destiny).pack(pady=5)

tb.Button(app, text="Extract", command=extract_zip).pack(pady=10)

app.mainloop()

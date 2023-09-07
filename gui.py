import qrcode
import os
import tkinter as tk
from tkinter import filedialog


def generate_qrcode():
    entrada = entry.get()
    filename = filename_entry.get()
    
    if entrada.lower() == "sair":
        root.quit()
    
    image = qrcode.make(entrada)
    image_path = os.path.join(qrcode_gen_path, filename + '.png')
    image.save(image_path)
    
    
    result_label.config(text=f"QR Code gerado e salvo em {image_path}")
    
    filename_entry.delete(0, tk.END)  # Limpar a entrada do nome do arquivo
    entry.delete(0, tk.END)


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
qrcode_gen_path = os.path.join(desktop_path, "qrcode")
if not os.path.exists(qrcode_gen_path):
    os.mkdir(qrcode_gen_path)

root = tk.Tk()
root.title("QR Code Generator")

header_label = tk.Label(root, text="QR Code Generator", font=("Helvetica", 16))
header_label.pack(pady=10)

entry_label = tk.Label(root, text="Link ou Palavra:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

filename_label = tk.Label(root, text="Nome do arquivo:")
filename_label.pack()

filename_entry = tk.Entry(root)
filename_entry.pack()

generate_button = tk.Button(root, text="Gerar QR Code", command=generate_qrcode)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

import PyPDF2
import tkinter as tk
from tkinter import messagebox
import time

def read_pdf():
    file_path = entry.get()
    
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            num_pages = pdf_reader.numPages
            content = ""
            for page in range(num_pages):
                content += pdf_reader.getPage(page).extractText()
            
            display_text(content)
            
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo PDF.")
    except PyPDF2.PdfReadError:
        messagebox.showerror("Error", "No se pudo leer el archivo PDF.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def display_text(content):
    text.delete('1.0', tk.END)
    display_characters(content, 0)
    

def display_characters(content, index):
    if index < len(content):
        text.insert(tk.END, content[index])
        if content[index] != ' ':
            text.update()  # Actualizar la ventana después de insertar cada letra
            time.sleep(0.1)  # Retraso de 0.1 segundos
        display_characters(content, index + 1)

# Crear la ventana principal
window = tk.Tk()
window.title("Visor de PDF")
#window.geometry("300x200")
window.attributes('-alpha', 0.7)

# Crear el contenedor Frame
top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP, padx=10, pady=10)

# Etiqueta para la ruta del archivo PDF
label = tk.Label(top_frame, text="Ruta del archivo PDF:")
label.pack(side=tk.LEFT)

# Entrada para el archivo PDF
entry = tk.Entry(top_frame)
entry.pack(side=tk.LEFT)

# Botón para leer el PDF
button = tk.Button(top_frame, text="Leer PDF", command=read_pdf)
button.pack(side=tk.RIGHT)

# Área de texto para mostrar el contenido del PDF
text = tk.Text(window)
text.pack()

# Ejecutar el bucle de eventos
window.mainloop()








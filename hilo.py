import threading
import time
import random
import tkinter as tk
from tkinter import scrolledtext

def cajero(cliente, text_widget):
    """
    Simula la atención en un cajero bancario.
    :param cliente: Nombre del cliente
    :param text_widget: Widget de texto para mostrar la salida en la interfaz gráfica
    """
    tiempo_atencion = random.randint(2, 6)  # Genera un tiempo de atención aleatorio entre 2 y 6 segundos
    mensaje_inicio = f"[INICIO] Atendiendo a {cliente}, tiempo estimado: {tiempo_atencion} segundos.\n"
    text_widget.insert(tk.END, mensaje_inicio)  # Inserta el mensaje en el widget de texto
    text_widget.see(tk.END)  # Desplaza automáticamente el scroll hacia el final
    time.sleep(tiempo_atencion)  # Simula el tiempo de atención
    mensaje_fin = f"[FIN] {cliente} ha sido atendido.\n"
    text_widget.insert(tk.END, mensaje_fin)  # Inserta el mensaje de finalización
    text_widget.see(tk.END)

def iniciar_atencion(text_widget):
    """
    Inicia múltiples hilos para atender a los clientes en paralelo.
    :param text_widget: Widget de texto para mostrar la salida
    """
    clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
    hilos = []
    
    for cliente in clientes:
        # Crea un hilo para cada cliente y lo inicia
        hilo = threading.Thread(target=cajero, args=(cliente, text_widget))
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos:
        hilo.join()  # Espera a que todos los hilos finalicen antes de continuar

def crear_interfaz():
    """
    Crea una interfaz gráfica con Tkinter para visualizar la simulación.
    """
    ventana = tk.Tk()
    ventana.title("Simulación de Cajero Bancario")
    ventana.geometry("500x300")  # Define el tamaño de la ventana
    
    # Crea un widget de texto con desplazamiento para mostrar la salida
    text_widget = scrolledtext.ScrolledText(ventana, width=60, height=15)
    text_widget.pack(pady=10)
    
    # Botón para iniciar la simulación con hilos
    boton_inicio = tk.Button(
        ventana, text="Iniciar Atención",
        command=lambda: threading.Thread(target=iniciar_atencion, args=(text_widget,)).start()
    )
    boton_inicio.pack()
    
    ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica

if __name__ == "__main__":
    crear_interfaz()  # Llama a la función para crear la interfaz gráfica

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import psutil
import time

# Función para convertir bytes en GB
def bytes_to_gb(num_bytes):
    return round(num_bytes / (1024 ** 3), 2)

# Función para crear una ventana emergente de error
def create_error_popup(message):
    dialog = Gtk.MessageDialog(
        parent=None,
        flags=0,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.CANCEL,
        text="Error"
    )
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()

while True:
    disk = psutil.disk_usage('/')
    free_space_gb = bytes_to_gb(disk.free) + 0.49
    print(f"Espacio libre en el disco principal: {free_space_gb} GB")
    if free_space_gb < 4:
        create_error_popup("¡Error! El espacio libre en el disco principal es inferior a 4 GB.")
    time.sleep(1)


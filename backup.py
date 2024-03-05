import subprocess
import datetime
from tkinter import messagebox
import os


def backup():
    try:
        # Configuración
        nombre_db = 'gymdb'
        fecha_hora = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        archivo_resp = f'backup_{fecha_hora}.sql'

        ruta_destino = 'C:\\'

        ruta_completa = os.path.join(ruta_destino, archivo_resp)

        # Ruta al ejecutable mysqldump (asegúrate de que sea la ruta correcta)
        mysqldump_path = '"C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysqldump.exe"'

        # Comando mysqldump con el uso del archivo my.cnf
        comando = f'{mysqldump_path} --defaults-extra-file=my.cnf {nombre_db} > {archivo_resp}'

        # Ejecutar el comando
        subprocess.run(comando, shell=True)
        return f"Copia de seguridad realizada correctamente: {archivo_resp}"
    except Exception as e:
        return f"Error al realizar backup: {str(e)}"

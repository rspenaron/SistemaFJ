"""
Modulo de manejo de logs
Este archivo gestiona el registro de eventos y errores del sistema
Escribe en un archivo de texto todas las operaciones importantes
"""

import os
from datetime import datetime

class GestorLogs:
    """
    Clase singleton para manejar el registro de eventos y errores
    Solo existe una instancia en todo el sistema
    """
    
    _instancia = None
    _ruta_log = "logs/sistema.log"
    
    def __new__(cls):
        """Patron Singleton: garantiza una sola instancia"""
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia
    
    def _inicializar(self):
        """Crea la carpeta de logs si no existe"""
        try:
            if not os.path.exists("logs"):
                os.makedirs("logs")
        except Exception as e:
            print(f"Error creando carpeta de logs: {e}")
    
    def _escribir(self, tipo, mensaje):
        """Escribe un mensaje en el archivo de log"""
        try:
            with open(self._ruta_log, "a", encoding="utf-8") as archivo:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"[{timestamp}] [{tipo}] {mensaje}\n")
        except Exception as e:
            # Si falla el log, al menos lo imprimimos en consola
            print(f"ERROR ESCRIBIENDO LOG: {e}")
            print(f"LOG ORIGINAL: [{tipo}] {mensaje}")
    
    def info(self, mensaje):
        """Registra un mensaje informativo"""
        self._escribir("INFO", mensaje)
    
    def error(self, mensaje):
        """Registra un error"""
        self._escribir("ERROR", mensaje)
    
    def warning(self, mensaje):
        """Registra una advertencia"""
        self._escribir("WARNING", mensaje)
    
    def debug(self, mensaje):
        """Registra un mensaje de depuracion"""
        self._escribir("DEBUG", mensaje)
    
    def leer_logs(self, lineas=50):
        """Lee las ultimas lineas del archivo de log"""
        try:
            if not os.path.exists(self._ruta_log):
                return ["No hay archivo de log aun"]
            
            with open(self._ruta_log, "r", encoding="utf-8") as archivo:
                todas = archivo.readlines()
                return todas[-lineas:]
        except Exception as e:
            return [f"Error leyendo logs: {e}"]
"""
Modulo de la clase Cliente
Este archivo define la estructura de un cliente con validaciones
Recibe nombre, email, telefono y fecha de registro opcional
Retorna un objeto cliente con datos validados
"""

import re
from datetime import datetime
from excepciones import ClienteInvalidoError, ValidacionError

class Cliente:
    """
    Clase que representa un cliente del sistema
    Atributos privados con encapsulacion y validaciones
    """
    
    def __init__(self, nombre, email, telefono, fecha_registro=None):
        """
        Constructor de la clase Cliente
        Recibe nombre, email, telefono y fecha de registro opcional
        """
        self._nombre = None
        self._email = None
        self._telefono = None
        self._fecha_registro = fecha_registro or datetime.now()
        self._activo = True
        
        # Usar los setters para validar
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    # Propiedades getters y setters
    
    @property
    def nombre(self):
        """Getter del nombre"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        """Setter del nombre con validacion"""
        if not valor or not valor.strip():
            raise ValidacionError("El nombre no puede estar vacio")
        if len(valor.strip()) < 3:
            raise ValidacionError("El nombre debe tener al menos 3 caracteres")
        self._nombre = valor.strip().title()
    
    @property
    def email(self):
        """Getter del email"""
        return self._email
    
    @email.setter
    def email(self, valor):
        """Setter del email con validacion de formato"""
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not valor or not re.match(patron_email, valor):
            raise ValidacionError(f"Email invalido: {valor}")
        self._email = valor.strip().lower()
    
    @property
    def telefono(self):
        """Getter del telefono"""
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        """Setter del telefono con validacion"""
        if not valor or not valor.strip():
            raise ValidacionError("El telefono no puede estar vacio")
        # Eliminar espacios y guiones para validar
        limpio = re.sub(r'[\s\-]', '', valor)
        if not limpio.isdigit() or len(limpio) < 7:
            raise ValidacionError(f"Telefono invalido: {valor}")
        self._telefono = valor.strip()
    
    @property
    def activo(self):
        """Getter del estado activo"""
        return self._activo
    
    @activo.setter
    def activo(self, valor):
        """Setter del estado activo"""
        self._activo = valor
    
    @property
    def fecha_registro(self):
        """Getter de fecha de registro solo lectura"""
        return self._fecha_registro
    
    # Metodos de la clase
    
    def desactivar(self):
        """Desactiva el cliente"""
        self._activo = False
        return f"Cliente {self._nombre} desactivado"
    
    def activar(self):
        """Activa el cliente"""
        self._activo = True
        return f"Cliente {self._nombre} activado"
    
    def __str__(self):
        """Representacion en texto del cliente"""
        estado = "Activo" if self._activo else "Inactivo"
        return f"Cliente: {self._nombre} | Email: {self._email} | Tel: {self._telefono} | Estado: {estado}"
    
    def __repr__(self):
        """Representacion para depuracion"""
        return f"Cliente('{self._nombre}', '{self._email}', '{self._telefono}')"
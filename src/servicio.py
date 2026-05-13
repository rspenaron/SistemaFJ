"""
Modulo de la clase abstracta Servicio
Este archivo define la estructura base para todos los servicios
Las clases hijas deben implementar los metodos abstractos
Recibe nombre, precio base y capacidad maxima
"""

from abc import ABC, abstractmethod
from datetime import datetime
from excepciones import ServicioNoDisponibleError, ValidacionError

class Servicio(ABC):
    """
    Clase abstracta que define el contrato para todos los servicios
    No se puede instanciar directamente, solo heredar de ella
    """
    
    # Contador de IDs compartido entre todas las instancias
    _contador_ids = 1
    
    def __init__(self, nombre, precio_base, capacidad_maxima=10):
        """
        Constructor del servicio
        Recibe nombre, precio base y capacidad maxima opcional
        """
        self._id = Servicio._contador_ids
        Servicio._contador_ids += 1
        
        # Validaciones iniciales
        if not nombre or not nombre.strip():
            raise ValidacionError("El nombre del servicio no puede estar vacio")
        if precio_base <= 0:
            raise ValidacionError("El precio base debe ser mayor a 0")
        if capacidad_maxima <= 0:
            raise ValidacionError("La capacidad debe ser mayor a 0")
        
        self._nombre = nombre.strip()
        self._precio_base = precio_base
        self._capacidad_maxima = capacidad_maxima
        self._disponible = True
    
    # Propiedades
    
    @property
    def id(self):
        """ID del servicio solo lectura"""
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio_base(self):
        return self._precio_base
    
    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima
    
    @property
    def disponible(self):
        return self._disponible
    
    def cambiar_disponibilidad(self, disponible):
        """Cambia la disponibilidad del servicio"""
        self._disponible = disponible
    
    # Metodos abstractos que las clases hijas deben implementar
    
    @abstractmethod
    def calcular_costo(self, horas=1, **kwargs):
        """
        Calcula el costo del servicio
        Cada subclase implementa su propia logica de calculo
        Recibe horas y parametros adicionales especificos
        Retorna el costo total
        """
        pass
    
    @abstractmethod
    def descripcion(self):
        """
        Retorna una descripcion detallada del servicio
        Cada subclase tiene su propio formato de descripcion
        """
        pass
    
    @abstractmethod
    def validar_parametros(self, **kwargs):
        """
        Valida los parametros especificos del servicio
        Retorna True si son validos o lanza una excepcion
        """
        pass
    
    # Metodos concretos
    
    def __str__(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._nombre} | ${self._precio_base}/h | Cap: {self._capacidad_maxima} | {estado}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._nombre}', {self._precio_base}, {self._capacidad_maxima})"
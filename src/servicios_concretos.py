"""
Modulo de servicios concretos
Este archivo define los tipos especificos de servicios que ofrece la empresa
Cada servicio hereda de la clase Servicio y personaliza su comportamiento
"""

from servicio import Servicio
from excepciones import ValidacionError, ServicioNoDisponibleError

class ServicioSala(Servicio):
    """
    Servicio de reserva de salas
    Caracteristicas: capacidad de personas, equipamiento como proyector y aire
    """
    
    def __init__(self, nombre, precio_base, capacidad_maxima,
                 tiene_proyector=False, tiene_aire_acondicionado=True):
        """
        Constructor para salas
        Recibe nombre, precio, capacidad, y opciones de equipamiento
        """
        super().__init__(nombre, precio_base, capacidad_maxima)
        self._tiene_proyector = tiene_proyector
        self._tiene_aire_acondicionado = tiene_aire_acondicionado
    
    def calcular_costo(self, horas=1, **kwargs):
        """
        Calcula costo de sala
        Base: precio_base * horas
        Proyector: +10 por hora
        Aire acondicionado: +5 por hora
        Descuento del 10 por ciento si son mas de 5 horas
        """
        if horas <= 0:
            raise ValidacionError("Las horas deben ser mayores a 0")
        
        costo = self._precio_base * horas
        
        if self._tiene_proyector:
            costo += 10 * horas
        
        if self._tiene_aire_acondicionado:
            costo += 5 * horas
        
        # Aplicar descuento por horas
        if horas > 5:
            descuento = costo * 0.10
            costo -= descuento
        
        return round(costo, 2)
    
    def calcular_costo_con_impuesto(self, horas=1, tasa_impuesto=0.19, **kwargs):
        """Calcula costo con impuesto - version sobrecargada del metodo"""
        costo_base = self.calcular_costo(horas, **kwargs)
        return round(costo_base * (1 + tasa_impuesto), 2)
    
    def descripcion(self):
        """Descripcion especifica para salas"""
        extras = []
        if self._tiene_proyector:
            extras.append("Proyector")
        if self._tiene_aire_acondicionado:
            extras.append("Aire Acondicionado")
        
        texto_extras = ", ".join(extras) if extras else "Sin extras"
        
        return f"SALA: {self._nombre} | Capacidad: {self._capacidad_maxima} personas | Extras: {texto_extras} | Precio base: ${self._precio_base}/h"
    
    def validar_parametros(self, **kwargs):
        """Valida parametros para reserva de sala"""
        if "cantidad_personas" in kwargs:
            personas = kwargs["cantidad_personas"]
            if personas > self._capacidad_maxima:
                raise ValidacionError(f"La sala solo tiene capacidad para {self._capacidad_maxima} personas")
        return True


class ServicioEquipo(Servicio):
    """
    Servicio de alquiler de equipos
    Caracteristicas: tipo de equipo, seguro opcional
    """
    
    def __init__(self, nombre, precio_base, capacidad_maxima,
                 tipo_equipo, incluye_seguro=False):
        super().__init__(nombre, precio_base, capacidad_maxima)
        self._tipo_equipo = tipo_equipo
        self._incluye_seguro = incluye_seguro
    
    def calcular_costo(self, horas=1, **kwargs):
        """
        Calcula costo de equipo
        Base: precio_base * horas
        Seguro: +15 por ciento si esta incluido
        """
        if horas <= 0:
            raise ValidacionError("Las horas deben ser mayores a 0")
        
        costo = self._precio_base * horas
        
        if self._incluye_seguro:
            costo = costo * 1.15
        
        return round(costo, 2)
    
    def calcular_costo_con_descuento(self, horas=1, descuento=0, **kwargs):
        """Calcula costo con descuento - version sobrecargada del metodo"""
        costo_base = self.calcular_costo(horas, **kwargs)
        return round(costo_base * (1 - descuento / 100), 2)
    
    def descripcion(self):
        """Descripcion especifica para equipos"""
        seguro = "Incluye seguro" if self._incluye_seguro else "Sin seguro"
        return f"EQUIPO: {self._nombre} | Tipo: {self._tipo_equipo} | {seguro} | Precio base: ${self._precio_base}/h"
    
    def validar_parametros(self, **kwargs):
        """Valida parametros para reserva de equipo"""
        return True


class ServicioAsesoria(Servicio):
    """
    Servicio de asesorias especializadas
    Caracteristicas: especialidad, nivel de experiencia del consultor
    """
    
    def __init__(self, nombre, precio_base, capacidad_maxima,
                 especialidad="General", nivel_experiencia="Junior"):
        super().__init__(nombre, precio_base, capacidad_maxima)
        self._especialidad = especialidad
        self._nivel_experiencia = nivel_experiencia
    
    def calcular_costo(self, horas=1, **kwargs):
        """
        Calcula costo de asesoria
        Base: precio_base * horas
        Senior: +50 por ciento
        Especialista: +80 por ciento
        """
        if horas <= 0:
            raise ValidacionError("Las horas deben ser mayores a 0")
        
        costo = self._precio_base * horas
        
        # Ajuste por nivel de experiencia
        if self._nivel_experiencia == "Senior":
            costo = costo * 1.50
        elif self._nivel_experiencia == "Especialista":
            costo = costo * 1.80
        
        return round(costo, 2)
    
    def calcular_costo_con_descuento_y_impuesto(self, horas=1, descuento=0, tasa_impuesto=0.19, **kwargs):
        """Calcula costo con descuento e impuesto - version sobrecargada"""
        costo_base = self.calcular_costo(horas, **kwargs)
        costo_descuento = costo_base * (1 - descuento / 100)
        return round(costo_descuento * (1 + tasa_impuesto), 2)
    
    def descripcion(self):
        """Descripcion especifica para asesorias"""
        return f"ASESORIA: {self._nombre} | Especialidad: {self._especialidad} | Nivel: {self._nivel_experiencia} | Precio base: ${self._precio_base}/h"
    
    def validar_parametros(self, **kwargs):
        """Valida parametros para reserva de asesoria"""
        if "nivel_requerido" in kwargs:
            nivel_requerido = kwargs["nivel_requerido"]
            niveles_permitidos = ["Junior", "Senior", "Especialista"]
            if nivel_requerido not in niveles_permitidos:
                raise ValidacionError(f"Nivel invalido. Permitidos: {niveles_permitidos}")
        return True
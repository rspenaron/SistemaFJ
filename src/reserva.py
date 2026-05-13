"""
Modulo de la clase Reserva
Este archivo gestiona las reservas que hacen los clientes
Integra un cliente, un servicio, duracion y estado de la reserva
"""

from datetime import datetime, timedelta
from excepciones import ReservaInvalidaError, CapacidadExcedidaError, ServicioNoDisponibleError
from cliente import Cliente
from servicio import Servicio

class Reserva:
    """
    Clase que representa una reserva
    Relaciona un cliente con un servicio por una cantidad de horas
    """
    
    # Estados posibles de una reserva
    ESTADO_PENDIENTE = "Pendiente"
    ESTADO_CONFIRMADA = "Confirmada"
    ESTADO_CANCELADA = "Cancelada"
    ESTADO_COMPLETADA = "Completada"
    
    _contador_ids = 1
    
    def __init__(self, cliente, servicio, horas=1,
                 fecha_hora=None, parametros_extra=None):
        """
        Constructor de la reserva
        Recibe cliente, servicio, horas, fecha opcional y parametros extra
        """
        self._id = Reserva._contador_ids
        Reserva._contador_ids += 1
        
        self._cliente = cliente
        self._servicio = servicio
        self._horas = horas
        self._fecha_hora = fecha_hora or datetime.now()
        self._parametros_extra = parametros_extra or {}
        self._estado = Reserva.ESTADO_PENDIENTE
        self._fecha_creacion = datetime.now()
        
        # Validar todo antes de crear la reserva
        self._validar_reserva()
    
    def _validar_reserva(self):
        """
        Validaciones completas de la reserva
        Lanza excepciones si algo esta mal
        """
        # 1. Validar que el cliente este activo
        if not self._cliente.activo:
            raise ReservaInvalidaError(f"El cliente {self._cliente.nombre} esta inactivo")
        
        # 2. Validar que el servicio este disponible
        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self._servicio.nombre} no esta disponible")
        
        # 3. Validar horas
        if self._horas <= 0:
            raise ReservaInvalidaError("La duracion debe ser mayor a 0 horas")
        
        if self._horas > 24:
            raise ReservaInvalidaError("La duracion maxima es 24 horas")
        
        # 4. Validar parametros especificos del servicio
        try:
            self._servicio.validar_parametros(**self._parametros_extra)
        except Exception as e:
            raise ReservaInvalidaError(f"Error en parametros: {str(e)}")
        
        # 5. Validar capacidad si aplica
        if "cantidad_personas" in self._parametros_extra:
            personas = self._parametros_extra["cantidad_personas"]
            if personas > self._servicio.capacidad_maxima:
                raise CapacidadExcedidaError(
                    f"Capacidad excedida. Maximo: {self._servicio.capacidad_maxima} personas"
                )
    
    # Propiedades
    
    @property
    def id(self):
        return self._id
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def servicio(self):
        return self._servicio
    
    @property
    def horas(self):
        return self._horas
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def fecha_hora(self):
        return self._fecha_hora
    
    # Metodos para gestionar estados
    
    def confirmar(self):
        """Confirma la reserva cambiando su estado"""
        if self._estado != Reserva.ESTADO_PENDIENTE:
            raise ReservaInvalidaError(f"No se puede confirmar una reserva en estado {self._estado}")
        
        self._estado = Reserva.ESTADO_CONFIRMADA
        return True
    
    def cancelar(self):
        """Cancela la reserva"""
        if self._estado == Reserva.ESTADO_COMPLETADA:
            raise ReservaInvalidaError("No se puede cancelar una reserva ya completada")
        
        if self._estado == Reserva.ESTADO_CANCELADA:
            return False
        
        self._estado = Reserva.ESTADO_CANCELADA
        return True
    
    def completar(self):
        """Marca la reserva como completada"""
        if self._estado != Reserva.ESTADO_CONFIRMADA:
            raise ReservaInvalidaError("Solo se pueden completar reservas confirmadas")
        
        self._estado = Reserva.ESTADO_COMPLETADA
        return True
    
    def calcular_costo_total(self, **kwargs):
        """
        Calcula el costo total usando polimorfismo
        Llama al metodo calcular_costo del servicio
        """
        return self._servicio.calcular_costo(self._horas, **self._parametros_extra, **kwargs)
    
    def obtener_resumen(self):
        """Retorna un resumen de la reserva"""
        return f"""
        ==================================================
        RESERVA #{self._id}
        ==================================================
        Cliente: {self._cliente.nombre}
        Servicio: {self._servicio.nombre}
        Estado: {self._estado}
        Duracion: {self._horas} horas
        Fecha/Hora: {self._fecha_hora.strftime('%d/%m/%Y %H:%M')}
        Costo Total: ${self.calcular_costo_total():.2f}
        ==================================================
        """
    
    def __str__(self):
        return f"Reserva #{self._id}: {self._cliente.nombre} - {self._servicio.nombre} ({self._estado})"
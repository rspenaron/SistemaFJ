"""
Modulo de excepciones personalizadas para el sistema Software FJ
Este archivo define todas las excepciones que puede lanzar el sistema
Las excepciones ayudan a manejar errores de forma controlada
"""

class ErrorSoftwareFJ(Exception):
    """Excepcion base para toda la aplicacion"""
    pass

class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se lanza cuando los datos del cliente no son validos"""
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se lanza cuando el servicio solicitado no esta disponible"""
    pass

class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se lanza cuando la reserva no se puede realizar"""
    pass

class CapacidadExcedidaError(ReservaInvalidaError):
    """Se lanza cuando la capacidad del servicio es insuficiente"""
    pass

class ValidacionError(ErrorSoftwareFJ):
    """Se lanza cuando hay errores de validacion de datos"""
    pass
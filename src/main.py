"""
SISTEMA INTEGRAL DE GESTION DE CLIENTES, SERVICIOS Y RESERVAS
Software FJ

Este es el archivo principal del programa
Ejecuta una demostracion completa con operaciones validas e invalidas
Demuestra todos los conceptos de programacion orientada a objetos
"""

import sys
import os

# Agregar la carpeta src al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cliente import Cliente
from servicios_concretos import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from logs import GestorLogs
from excepciones import *

class SistemaSoftwareFJ:
    """
    Clase principal que orquesta todo el sistema
    Contiene metodos para gestionar clientes, servicios y reservas
    """
    
    def __init__(self):
        """Inicializa el sistema con listas vacias y el gestor de logs"""
        self.logger = GestorLogs()
        self.clientes = []
        self.servicios = []
        self.reservas = []
        
        self.logger.info("=" * 60)
        self.logger.info("SISTEMA SOFTWARE FJ INICIADO")
        self.logger.info("=" * 60)
        
        print("\n" + "=" * 60)
        print("SISTEMA INTEGRAL SOFTWARE FJ")
        print("=" * 60)
        print("Gestiona clientes, servicios y reservas")
        print("=" * 60 + "\n")
    
    # Gestion de Clientes
    
    def registrar_cliente(self, nombre, email, telefono):
        """
        Registra un nuevo cliente con manejo de excepciones
        Retorna el cliente creado o None si hay error
        """
        try:
            print(f"\n-> Intentando registrar cliente: {nombre}")
            cliente = Cliente(nombre, email, telefono)
            self.clientes.append(cliente)
            self.logger.info(f"Cliente registrado exitosamente: {cliente.nombre} - ID: {id(cliente)}")
            print(f"Cliente registrado exitosamente: {cliente}")
            return cliente
        
        except ValidacionError as e:
            self.logger.error(f"Error validando cliente: {e}")
            print(f"Error de validacion: {e}")
            return None
        
        except Exception as e:
            self.logger.error(f"Error inesperado registrando cliente: {e}")
            print(f"Error inesperado: {e}")
            return None
    
    # Gestion de Servicios
    
    def crear_servicio_sala(self, nombre, precio, capacidad, proyector=False, aire=True):
        """Crea un servicio de sala"""
        try:
            servicio = ServicioSala(nombre, precio, capacidad, proyector, aire)
            self.servicios.append(servicio)
            self.logger.info(f"Servicio creado: {servicio.descripcion()}")
            print(f"Servicio de sala creado: {servicio.nombre}")
            return servicio
        except Exception as e:
            self.logger.error(f"Error creando servicio sala: {e}")
            print(f"Error: {e}")
            return None
    
    def crear_servicio_equipo(self, nombre, precio, capacidad, tipo_equipo, seguro=False):
        """Crea un servicio de equipo"""
        try:
            servicio = ServicioEquipo(nombre, precio, capacidad, tipo_equipo, seguro)
            self.servicios.append(servicio)
            self.logger.info(f"Servicio creado: {servicio.descripcion()}")
            print(f"Servicio de equipo creado: {servicio.nombre}")
            return servicio
        except Exception as e:
            self.logger.error(f"Error creando servicio equipo: {e}")
            print(f"Error: {e}")
            return None
    
    def crear_servicio_asesoria(self, nombre, precio, capacidad, especialidad, nivel):
        """Crea un servicio de asesoria"""
        try:
            servicio = ServicioAsesoria(nombre, precio, capacidad, especialidad, nivel)
            self.servicios.append(servicio)
            self.logger.info(f"Servicio creado: {servicio.descripcion()}")
            print(f"Servicio de asesoria creado: {servicio.nombre}")
            return servicio
        except Exception as e:
            self.logger.error(f"Error creando servicio asesoria: {e}")
            print(f"Error: {e}")
            return None
    
    # Gestion de Reservas
    
    def crear_reserva(self, cliente_id, servicio_id, horas, **parametros):
        """Crea una nueva reserva"""
        try:
            # Buscar cliente
            cliente = self.clientes[cliente_id] if 0 <= cliente_id < len(self.clientes) else None
            if not cliente:
                raise ReservaInvalidaError("Cliente no encontrado")
            
            # Buscar servicio
            servicio = self.servicios[servicio_id] if 0 <= servicio_id < len(self.servicios) else None
            if not servicio:
                raise ReservaInvalidaError("Servicio no encontrado")
            
            print(f"\n-> Creando reserva para {cliente.nombre} - {servicio.nombre} ({horas} horas)")
            
            # Crear reserva
            reserva = Reserva(cliente, servicio, horas, parametros_extra=parametros)
            self.reservas.append(reserva)
            
            self.logger.info(f"Reserva creada: {reserva}")
            print(f"Reserva #{reserva.id} creada exitosamente")
            return reserva
        
        except (ReservaInvalidaError, ServicioNoDisponibleError, CapacidadExcedidaError) as e:
            self.logger.error(f"Error en reserva: {e}")
            print(f"Error en reserva: {e}")
            return None
        
        except Exception as e:
            self.logger.error(f"Error inesperado creando reserva: {e}")
            print(f"Error inesperado: {e}")
            return None
    
    def confirmar_reserva(self, reserva_id):
        """Confirma una reserva existente"""
        try:
            if reserva_id >= len(self.reservas):
                raise ReservaInvalidaError("Reserva no encontrada")
            
            reserva = self.reservas[reserva_id]
            reserva.confirmar()
            self.logger.info(f"Reserva #{reserva.id} confirmada")
            print(f"Reserva #{reserva.id} confirmada")
            return True
        
        except Exception as e:
            self.logger.error(f"Error confirmando reserva: {e}")
            print(f"Error: {e}")
            return False
    
    def completar_reserva(self, reserva_id):
        """Completa una reserva"""
        try:
            if reserva_id >= len(self.reservas):
                raise ReservaInvalidaError("Reserva no encontrada")
            
            reserva = self.reservas[reserva_id]
            reserva.completar()
            self.logger.info(f"Reserva #{reserva.id} completada")
            print(f"Reserva #{reserva.id} completada")
            return True
        
        except Exception as e:
            self.logger.error(f"Error completando reserva: {e}")
            print(f"Error: {e}")
            return False
    
    def cancelar_reserva(self, reserva_id):
        """Cancela una reserva"""
        try:
            if reserva_id >= len(self.reservas):
                raise ReservaInvalidaError("Reserva no encontrada")
            
            reserva = self.reservas[reserva_id]
            reserva.cancelar()
            self.logger.info(f"Reserva #{reserva.id} cancelada")
            print(f"Reserva #{reserva.id} cancelada")
            return True
        
        except Exception as e:
            self.logger.error(f"Error cancelando reserva: {e}")
            print(f"Error: {e}")
            return False
    
    # Consultas
    
    def mostrar_clientes(self):
        """Muestra todos los clientes registrados"""
        print("\n" + "=" * 60)
        print("CLIENTES REGISTRADOS")
        print("=" * 60)
        if not self.clientes:
            print("No hay clientes registrados")
        else:
            for i, cliente in enumerate(self.clientes):
                print(f"[{i}] {cliente}")
    
    def mostrar_servicios(self):
        """Muestra todos los servicios disponibles"""
        print("\n" + "=" * 60)
        print("SERVICIOS DISPONIBLES")
        print("=" * 60)
        if not self.servicios:
            print("No hay servicios registrados")
        else:
            for i, servicio in enumerate(self.servicios):
                print(f"\n[{i}] {servicio}")
                print(f"    {servicio.descripcion()}")
    
    def mostrar_reservas(self):
        """Muestra todas las reservas"""
        print("\n" + "=" * 60)
        print("RESERVAS")
        print("=" * 60)
        if not self.reservas:
            print("No hay reservas")
        else:
            for i, reserva in enumerate(self.reservas):
                print(f"\n[{i}] {reserva}")
                print(reserva.obtener_resumen())
    
    def mostrar_logs(self):
        """Muestra los ultimos logs"""
        print("\n" + "=" * 60)
        print("ULTIMOS LOGS DEL SISTEMA")
        print("=" * 60)
        logs = self.logger.leer_logs(20)
        for log in logs:
            print(log.strip())


# Demostracion del Sistema

def demostracion_sistema():
    """
    Demostracion completa del sistema
    Incluye operaciones validas e invalidas para probar manejo de excepciones
    Se realizan al menos 10 operaciones como solicita el profesor
    """
    
    print("\n" + "INICIANDO DEMOSTRACION DEL SISTEMA".center(60))
    print("Se simularan varias operaciones incluyendo errores controlados\n")
    
    sistema = SistemaSoftwareFJ()
    
    # 1. REGISTRO DE CLIENTES
    print("\n" + "-" * 60)
    print("1. REGISTRO DE CLIENTES")
    print("-" * 60)
    
    cliente1 = sistema.registrar_cliente("Juan Perez", "juan@email.com", "3001234567")
    cliente2 = sistema.registrar_cliente("Maria Gomez", "maria.gomez@empresa.co", "3109876543")
    cliente_invalido1 = sistema.registrar_cliente("Pedro", "email-invalido", "3205555555")
    cliente_invalido2 = sistema.registrar_cliente("A", "a@b.com", "3111111111")
    cliente3 = sistema.registrar_cliente("Carlos Rodriguez", "carlos.rodriguez@tecnologia.com", "3015557777")
    cliente4 = sistema.registrar_cliente("Ana Martinez", "ana.martinez@consultora.co", "3156668888")
    
    # 2. CREACION DE SERVICIOS
    print("\n" + "-" * 60)
    print("2. CREACION DE SERVICIOS")
    print("-" * 60)
    
    sala1 = sistema.crear_servicio_sala("Sala Ejecutiva", 50.0, 10, proyector=True, aire=True)
    sala2 = sistema.crear_servicio_sala("Sala de Conferencias", 80.0, 30, proyector=True, aire=True)
    equipo1 = sistema.crear_servicio_equipo("Laptop Gamer", 25.0, 5, "Portatil", seguro=True)
    equipo2 = sistema.crear_servicio_equipo("Proyector 4K", 15.0, 8, "Proyector", seguro=False)
    asesoria1 = sistema.crear_servicio_asesoria("Asesoria Python", 60.0, 1, "Programacion", "Senior")
    asesoria2 = sistema.crear_servicio_asesoria("Consultoria TI", 120.0, 1, "Infraestructura", "Especialista")
    servicio_invalido = sistema.crear_servicio_sala("Sala Invalida", 0, 5)
    
    # 3. DEMOSTRACION DE POLIMORFISMO
    print("\n" + "-" * 60)
    print("3. DEMOSTRACION DE POLIMORFISMO")
    print("-" * 60)
    
    print("\nCalculos de costos (mismo metodo, diferentes resultados):")
    
    if sala1:
        print(f"\n   Sala '{sala1.nombre}' (3 horas):")
        print(f"      Costo base: ${sala1.calcular_costo(3):.2f}")
        print(f"      Con impuesto 19%: ${sala1.calcular_costo_con_impuesto(3):.2f}")
    
    if equipo1:
        print(f"\n   Equipo '{equipo1.nombre}' (5 horas):")
        print(f"      Costo base: ${equipo1.calcular_costo(5):.2f}")
        print(f"      Con descuento 10%: ${equipo1.calcular_costo_con_descuento(5, 10):.2f}")
    
    if asesoria1:
        print(f"\n   Asesoria '{asesoria1.nombre}' (2 horas):")
        print(f"      Costo base: ${asesoria1.calcular_costo(2):.2f}")
        print(f"      Con descuento 15% e impuesto: ${asesoria1.calcular_costo_con_descuento_y_impuesto(2, 15):.2f}")
    
    # 4. CREACION DE RESERVAS VALIDAS
    print("\n" + "-" * 60)
    print("4. CREACION DE RESERVAS VALIDAS")
    print("-" * 60)
    
    if cliente1 and sala1:
        reserva1 = sistema.crear_reserva(0, 0, 3, cantidad_personas=5)
        if reserva1:
            sistema.confirmar_reserva(0)
    
    if cliente2 and equipo1:
        reserva2 = sistema.crear_reserva(1, 2, 5)
        if reserva2:
            sistema.confirmar_reserva(1)
    
    if cliente3 and asesoria1:
        reserva3 = sistema.crear_reserva(2, 4, 2)
        if reserva3:
            sistema.confirmar_reserva(2)
    
    # 5. RESERVAS CON ERRORES (MANEJO DE EXCEPCIONES)
    print("\n" + "-" * 60)
    print("5. RESERVAS CON ERRORES (Manejo de excepciones)")
    print("-" * 60)
    
    print("\nIntentando reserva con capacidad excedida...")
    if cliente1 and sala1:
        reserva_error1 = sistema.crear_reserva(0, 0, 2, cantidad_personas=20)
    
    print("\nIntentando reserva con 0 horas...")
    if cliente2 and equipo1:
        reserva_error2 = sistema.crear_reserva(1, 2, 0)
    
    print("\nIntentando reserva con mas del maximo de horas...")
    if cliente3 and asesoria1:
        reserva_error3 = sistema.crear_reserva(2, 4, 25)
    
    print("\nIntentando reserva con cliente inactivo...")
    if cliente4:
        cliente4.desactivar()
        reserva_error4 = sistema.crear_reserva(3, 0, 2)
        cliente4.activar()
    
    # 6. GESTION DE RESERVAS
    print("\n" + "-" * 60)
    print("6. GESTION DE RESERVAS")
    print("-" * 60)
    
    print("\nCompletando reserva...")
    sistema.completar_reserva(0)
    
    print("\nCancelando reserva...")
    sistema.cancelar_reserva(1)
    
    print("\nIntentando confirmar reserva cancelada...")
    sistema.confirmar_reserva(1)
    
    print("\nIntentando cancelar reserva completada...")
    sistema.cancelar_reserva(0)
    
    # 7. RESERVA ADICIONAL VALIDA
    print("\n" + "-" * 60)
    print("7. RESERVA ADICIONAL")
    print("-" * 60)
    
    if cliente4 and asesoria2:
        reserva4 = sistema.crear_reserva(3, 5, 4)
        if reserva4:
            sistema.confirmar_reserva(3)
    
    # 8. MOSTRAR RESULTADOS
    print("\n" + "=" * 60)
    print("8. RESUMEN FINAL")
    print("=" * 60)
    
    sistema.mostrar_clientes()
    sistema.mostrar_servicios()
    sistema.mostrar_reservas()
    
    # 9. MOSTRAR LOGS
    print("\n" + "=" * 60)
    print("9. REGISTRO DE LOGS")
    print("=" * 60)
    print("\nRevisa el archivo en: logs/sistema.log\n")
    sistema.mostrar_logs()
    
    # Finalizar
    print("\n" + "=" * 60)
    print("DEMOSTRACION COMPLETADA")
    print("=" * 60)
    print("\nEl sistema manejo exitosamente:")
    print("Registro de clientes (validos e invalidos)")
    print("Creacion de servicios (validos e invalidos)")
    print("Polimorfismo en calculos de costos")
    print("Creacion de reservas exitosas")
    print("Manejo de excepciones (capacidad excedida, horas invalidas, etc)")
    print("Gestion de estados de reservas")
    print("Logging de eventos y errores")
    print("\nLos logs se guardaron en: logs/sistema.log")
    print("=" * 60 + "\n")


# Punto de entrada principal

if __name__ == "__main__":
    try:
        demostracion_sistema()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"\nError fatal no manejado: {e}")
        print("Por favor, revisa el archivo de logs")
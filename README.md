# Sistema Integral de Gestion - Software FJ

## Como Ejecutar el Programa

Paso 1: Descargar o copiar el proyecto

Paso 2: Ejecutar el main.py con visual studio code


## Descripcion del Proyecto

Este proyecto fue desarrollado para el curso de Programacion de la UNAD
Implementa un sistema orientado a objetos para gestionar clientes, servicios y reservas de una empresa llamada Software FJ

El sistema no utiliza base de datos, toda la informacion se maneja con listas en memoria
Incluye manejo avanzado de excepciones y registro de eventos en archivos de log

## Objetivos del Trabajo

Demostrar los principios de la programacion orientada a objetos:
- Abstraccion: clase abstracta Servicio que define el contrato basico
- Herencia: tres tipos de servicios que heredan de Servicio
- Polimorfismo: mismos metodos con comportamientos diferentes segun el tipo
- Encapsulacion: atributos privados con getters y setters que validan datos

Demostrar manejo avanzado de excepciones:
- Excepciones personalizadas para cada tipo de error
- Bloques try/except, try/except/else, try/except/finally
- Registro de todos los errores en archivos de log



## Estructura de Carpetas y Archivos
SoftwareFJ/

1 src/ # Carpeta con el codigo fuente
    1.1 init.py # Marca src como paquete Python
    1.2 cliente.py # Clase Cliente con validaciones
    1.3 servicio.py # Clase abstracta Servicio
    1.4 servicios_concretos.py # ServicioSala, ServicioEquipo, servicioAsesoria
    1.5 reserva.py # Clase Reserva con estados
    1.6 excepciones.py # Excepciones personalizadas
    1.7 logs.py # Gestor de archivos de log
    1.8 main.py # Archivo principal a ejecutar

2 logs/ # Carpeta donde se guardan los logs
    2.1sistema.log """Archivo de log (se crea automaticamente)"""

3 README.md # Este archivo de documentacion

## Explicacion de Cada Archivo

### excepciones.py
Define las excepciones personalizadas del sistema
Cada excepcion representa un tipo especifico de error
Jerarquia: ErrorSoftwareFJ es la base, las otras heredan de ella

### cliente.py
Define la clase Cliente con encapsulacion
Los atributos _nombre, _email, _telefono son privados
Los setters validan que los datos sean correctos antes de asignarlos
El email debe tener formato valido con @ y punto
El telefono debe tener al menos 7 digitos
El nombre no puede estar vacio ni ser muy corto

### servicio.py
Define la clase abstracta Servicio
Tiene metodos abstractos que las clases hijas deben implementar:
- calcular_costo: cada servicio calcula su costo de forma diferente
- descripcion: cada servicio tiene su propio formato de descripcion
- validar_parametros: cada servicio valida sus parametros especificos

### servicios_concretos.py
Define tres tipos de servicios que heredan de Servicio

ServicioSala:
- Para reservar salas de reunion o conferencias
- Costo adicional por proyector y aire acondicionado
- Descuento del 10% si se reserva por mas de 5 horas
- Valida que la cantidad de personas no exceda la capacidad

ServicioEquipo:
- Para alquilar equipos como laptops o proyectores
- Incluye seguro opcional que aumenta el costo 15%
- Metodo sobrecargado para calcular con descuento

ServicioAsesoria:
- Para asesorias especializadas en tecnologia
- Costo varia segun nivel (Junior, Senior, Especialista)
- Metodo sobrecargado para calcular con descuento e impuesto

### reserva.py
Define la clase Reserva que integra cliente y servicio
Estados posibles: Pendiente, Confirmada, Cancelada, Completada
El constructor valida todo antes de crear la reserva:
- Cliente debe estar activo
- Servicio debe estar disponible
- Horas deben ser entre 1 y 24
- Capacidad no debe excederse
- Parametros especificos validos para el servicio

### logs.py
Define el gestor de logs como singleton (solo una instancia)
Los logs se guardan en la carpeta logs/ con formato:
[fecha hora] [tipo] mensaje
Tipos: INFO, ERROR, WARNING, DEBUG
Si no se puede escribir el log, se muestra en consola

### main.py
Archivo principal que ejecuta la demostracion
Define la clase SistemaSoftwareFJ que orquesta todo
La funcion demostracion_sistema ejecuta mas de 10 operaciones:
- Registro de clientes validos e invalidos
- Creacion de servicios validos e invalidos
- Demostracion de polimorfismo con calculos de costos
- Creacion de reservas exitosas
- Creacion de reservas con errores (capacidad, horas, etc)
- Gestion de estados de reservas (confirmar, cancelar, completar)
- Muestra de logs al final
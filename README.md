# Sistema de Reserva - Pruebas Unitarias

Este repositorio contiene un sistema de reserva implementado en Python junto con pruebas unitarias para las diferentes clases del sistema.

## Introducción

El sistema de reserva es una aplicación que permite gestionar reservas de hoteles. Está compuesto por varias clases, como `Hotel`, `Cliente`, `Reserva`, `ManejadorHoteles` y `ManejadorClientes`. Cada clase desempeña un papel específico en el proceso de reserva y gestión de clientes y hoteles.

## Explicación de los fundamentos del desarrollo de pruebas unitarias:

Las pruebas unitarias son fundamentales en el desarrollo de software, ya que permiten verificar el comportamiento correcto de pequeñas unidades de código de forma aislada. Se escriben casos de prueba que evalúan el funcionamiento esperado de estas unidades, mejorando la calidad del software al identificar y corregir errores temprano en el ciclo de desarrollo.

## Pruebas Unitarias por Clase:

### Prueba unitaria para la clase Reserva:

Una prueba verifica si el método `__str__` de la clase `Reserva` devuelve la representación correcta de la reserva.

### Prueba unitaria para la clase Cliente:

Una prueba se encarga de validar el método `to_dict` de la clase `Cliente`, garantizando que la conversión del cliente a un diccionario sea precisa.

### Prueba unitaria para la clase ManejadorHoteles:

Una prueba valida si el método `crear_hotel` del `ManejadorHoteles` puede crear correctamente un nuevo hotel.

### Prueba unitaria para la clase Hotel:

Una prueba asegura que el método `agregar_reserva` de la clase `Hotel` añada correctamente las reservas.

### Prueba unitaria para la clase ManejadorClientes:

Una prueba confirma que el método `crear_cliente` del `ManejadorClientes` pueda crear un nuevo cliente correctamente.

## Análisis de Errores de Pylint – PEP 8:

Los errores de Pylint, como "line too long" y "too-few-public-methods", señalan incumplimientos de las convenciones de estilo definidas en PEP 8, lo que mejora la legibilidad y mantenibilidad del código.

## Análisis de Errores de Flake:

Los errores de Flake, como "line too long", indican que una línea de código excede la longitud máxima permitida según las convenciones de estilo, lo que puede afectar la claridad del código.

## Correcto Diseño de Casos de Prueba. Incluir casos negativos:

Es importante diseñar casos de prueba que cubran tanto los escenarios esperados como los inesperados. Incluir casos negativos garantiza que el código maneje adecuadamente situaciones inesperadas, mejorando la robustez y fiabilidad del software.

## Cobertura de líneas por clase:

Se debe apuntar a una cobertura de al menos el 85% por clase, asegurando que la mayoría de las líneas de código sean ejecutadas durante las pruebas unitarias para garantizar una mayor confiabilidad y calidad del software.

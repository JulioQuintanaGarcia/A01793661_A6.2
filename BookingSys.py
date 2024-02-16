# pylint: disable=C0103
# pylint: disable=too-few-public-methods
"""Sistema de Reserva"""
import json
from datetime import datetime


class Hotel:
    """Clase representando a Hotel"""
    def __init__(self, nombre, ubicacion, estrellas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.estrellas = estrellas
        self.reservas = []

    def agregar_reserva(self, reserva):
        """Funcion agregar reserva"""
        self.reservas.append(reserva)

    def cancelar_reserva(self, reserva_id):
        """Funcion cancelar reserva"""
        for reserva in self.reservas:
            if reserva['id'] == reserva_id:
                self.reservas.remove(reserva)
                return True
        return False

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} ({self.estrellas} estrellas)"

    def to_dict(self):
        """Funcion formato diccionario"""
        return {
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "estrellas": self.estrellas,
            "reservas": self.reservas
        }


class Cliente:
    """Clase representando a Cliente"""
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return (
            f"{self.nombre} {self.apellido} - {self.email} - "
            f"Teléfono: {self.telefono}"
        )

    def to_dict(self):
        """Funcion diccionario cliente"""
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono
        }


class Reserva:
    """Clase representando a Reserva"""
    def __init__(self, cliente, hotel, fecha_entrada, fecha_salida,
                 habitacion, costo):
        self.cliente = cliente
        self.hotel = hotel
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.habitacion = habitacion
        self.costo = costo
        self.id = datetime.now().strftime("%Y%m%d%H%M%S")

    def __str__(self):
        return (f"Reserva de {self.cliente.nombre} {self.cliente.apellido} "
                f"en {self.hotel.nombre} del {self.fecha_entrada}"
                f" al {self.fecha_salida} "
                f"- Habitación {self.habitacion}"
                f" (${self.costo})")

    def to_dict(self):
        """Funcion diccionario reserva"""
        return {
            "id": self.id,
            "cliente": self.cliente.to_dict(),
            "hotel": self.hotel.to_dict(),
            "fecha_entrada": self.fecha_entrada,
            "fecha_salida": self.fecha_salida,
            "habitacion": self.habitacion,
            "costo": self.costo
        }


class ManejadorHoteles:
    """Clase representando a Manejador de Hotel"""
    def __init__(self, archivo_hoteles):
        self.archivo_hoteles = archivo_hoteles

    def _cargar_hoteles_desde_archivo(self):
        hoteles = []
        try:
            with open(self.archivo_hoteles, 'r', encoding="utf-8") as file:
                for line in file:
                    hotel = json.loads(line)
                    if self._validar_hotel(hotel):
                        hoteles.append(hotel)
                    else:
                        print("Error: Hotel no válido en el archivo.")
        except FileNotFoundError:
            pass
        return hoteles

    def _guardar_hoteles_en_archivo(self, hoteles):
        with open(self.archivo_hoteles, 'w', encoding="utf-8") as file:
            for hotel in hoteles:
                json.dump(hotel, file)
                file.write('\n')

    def _validar_hotel(self, hotel):
        """Validar hotel"""
        return (
            all(key in hotel for key in ("nombre", "ubicacion", "estrellas")
                ) and
            isinstance(hotel["nombre"], str) and
            isinstance(hotel["ubicacion"], str) and
            isinstance(hotel["estrellas"], int)
        )

    def crear_hotel(self, nombre, ubicacion, estrellas):
        """Crear hotel"""
        hoteles = self._cargar_hoteles_desde_archivo()
        nuevo_hotel = Hotel(nombre, ubicacion, estrellas)
        hoteles.append(nuevo_hotel.to_dict())
        self._guardar_hoteles_en_archivo(hoteles)


class ManejadorClientes:
    """Clase representando a Manejador de cliente"""
    def __init__(self, archivo_clientes):
        self.archivo_clientes = archivo_clientes

    def _cargar_clientes_desde_archivo(self):
        clientes = []
        try:
            with open(self.archivo_clientes, 'r', encoding="utf-8") as file:
                for line in file:
                    cliente = json.loads(line)
                    if self._validar_cliente(cliente):
                        clientes.append(cliente)
                    else:
                        print("Error: Cliente no válido en el archivo.")
        except FileNotFoundError:
            pass
        return clientes

    def _guardar_clientes_en_archivo(self, clientes):
        with open(self.archivo_clientes, 'w', encoding="utf-8") as file:
            for cliente in clientes:
                json.dump(cliente, file)
                file.write('\n')

    def _validar_cliente(self, cliente):
        """Validar cliente"""
        return (
            all(
                key in cliente for key in ("nombre", "apellido",
                                           "email", "telefono")
                ) and
            isinstance(cliente["nombre"], str) and
            isinstance(cliente["apellido"], str) and
            isinstance(cliente["email"], str) and
            isinstance(cliente["telefono"], str)
        )

    def crear_cliente(self, clienteInfo):
        """Crear cliente"""
        clientes = self._cargar_clientes_desde_archivo()
        nuevo_cliente = Cliente(**clienteInfo)
        clientes.append(nuevo_cliente.to_dict())
        self._guardar_clientes_en_archivo(clientes)


if __name__ == "__main__":
    # Ejemplo de uso
    manejador_hoteles = ManejadorHoteles("hoteles.json")
    manejador_hoteles.crear_hotel("Hotel Ejemplo", "Ciudad Ejemplo", 4)

    manejador_clientes = ManejadorClientes("clientes.json")
    cliente_info = {
        "nombre": "Juan",
        "apellido": "Perez",
        "email": "juan@example.com",
        "telefono": "123456789"
    }
    manejador_clientes.crear_cliente(cliente_info)

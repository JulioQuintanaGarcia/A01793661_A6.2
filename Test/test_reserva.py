import unittest
from datetime import datetime
from sistema_reserva import Cliente, Hotel, Reserva


class TestReserva(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Juan", "Perez", "juan@example.com", "123456789")
        self.hotel = Hotel("Hotel Ejemplo", "Ciudad Ejemplo", 4)
        self.fecha_entrada = datetime(2024, 2, 14)
        self.fecha_salida = datetime(2024, 2, 16)
        self.habitacion = "Suite"
        self.costo = 200

    def test_creacion_reserva(self):
        reserva = Reserva(self.cliente, self.hotel, self.fecha_entrada, self.fecha_salida,
                          self.habitacion, self.costo)
        self.assertIsInstance(reserva, Reserva)
        self.assertEqual(reserva.cliente, self.cliente)
        self.assertEqual(reserva.hotel, self.hotel)
        self.assertEqual(reserva.fecha_entrada, self.fecha_entrada)
        self.assertEqual(reserva.fecha_salida, self.fecha_salida)
        self.assertEqual(reserva.habitacion, self.habitacion)
        self.assertEqual(reserva.costo, self.costo)

    def test_to_dict(self):
        reserva = Reserva(self.cliente, self.hotel, self.fecha_entrada, self.fecha_salida,
                          self.habitacion, self.costo)
        reserva_dict = reserva.to_dict()
        expected_dict = {
            "cliente": self.cliente.to_dict(),
            "hotel": self.hotel.to_dict(),
            "fecha_entrada": self.fecha_entrada,
            "fecha_salida": self.fecha_salida,
            "habitacion": self.habitacion,
            "costo": self.costo
        }
        self.assertEqual(reserva_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
import unittest
from sistema_reserva import Hotel


class TestHotel(unittest.TestCase):
    def test_creacion_hotel(self):
        hotel = Hotel("Hotel Ejemplo", "Ciudad Ejemplo", 4)
        self.assertIsInstance(hotel, Hotel)
        self.assertEqual(hotel.nombre, "Hotel Ejemplo")
        self.assertEqual(hotel.ubicacion, "Ciudad Ejemplo")
        self.assertEqual(hotel.estrellas, 4)

    def test_to_dict(self):
        hotel = Hotel("Hotel Ejemplo", "Ciudad Ejemplo", 4)
        hotel_dict = hotel.to_dict()
        expected_dict = {
            "nombre": "Hotel Ejemplo",
            "ubicacion": "Ciudad Ejemplo",
            "estrellas": 4,
            "reservas": []
        }
        self.assertEqual(hotel_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
import unittest
from sistema_reserva import ManejadorHoteles


class TestManejadorHoteles(unittest.TestCase):
    def setUp(self):
        self.manejador_hoteles = ManejadorHoteles("hoteles_test.json")

    def test_crear_hotel(self):
        self.manejador_hoteles.crear_hotel("Hotel Ejemplo", "Ciudad Ejemplo", 4)
        # Verificar que se haya creado el hotel en el archivo de prueba
        with open("hoteles_test.json", "r") as f:
            data = f.read()
            self.assertIn("Hotel Ejemplo", data)


if __name__ == '__main__':
    unittest.main()
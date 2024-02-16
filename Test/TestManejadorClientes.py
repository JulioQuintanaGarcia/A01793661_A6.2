import unittest
from pathlib import Path
from sistema_reserva import ManejadorClientes


class TestManejadorClientes(unittest.TestCase):
    def setUp(self):
        self.manejador_clientes = ManejadorClientes("clientes_test.json")

    def test_crear_cliente(self):
        cliente_info = {
            "nombre": "Juan",
            "apellido": "Perez",
            "email": "juan@example.com",
            "telefono": "123456789"
        }
        self.manejador_clientes.crear_cliente(cliente_info)
        # Verificar que se haya creado el cliente en el archivo de prueba
        with open("clientes_test.json", "r") as f:
            data = f.read()
            self.assertIn("Juan", data)


if __name__ == '__main__':
    unittest.main()
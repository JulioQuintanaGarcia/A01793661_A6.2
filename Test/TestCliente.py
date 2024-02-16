import unittest
from sistema_reserva import Cliente


class TestCliente(unittest.TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente("Juan", "Perez", "juan@example.com", "123456789")
        self.assertIsInstance(cliente, Cliente)
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.apellido, "Perez")
        self.assertEqual(cliente.email, "juan@example.com")
        self.assertEqual(cliente.telefono, "123456789")

    def test_to_dict(self):
        cliente = Cliente("Juan", "Perez", "juan@example.com", "123456789")
        cliente_dict = cliente.to_dict()
        expected_dict = {
            "nombre": "Juan",
            "apellido": "Perez",
            "email": "juan@example.com",
            "telefono": "123456789"
        }
        self.assertEqual(cliente_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
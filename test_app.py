from app import add

"""
Módulo de tests para la aplicación.
Pruebas unitarias de las funciones principales.
"""


def test_add():
    """
        Test para verificar la función calcular_suma.
        """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

from unittest import TestCase

from src import app


class testUnit(TestCase):

    def test_start(self):
        app.start(2)

    def test_complex(self):
        prime_number = app.complex(8)
        print(prime_number)

from unittest import TestCase

from src import app


class testUnit(TestCase):

    def test_start(self):
        app.start(2)

    def test_complex(self):
        prime_number = app.complex(8)
        print(prime_number)

    def test_read(self):
        payload = {
            "CommonParms": {
                "action": "read"
            }
        }
        app.start(payload)

    # payload for create should look like this
    def test_create(self):
        payload = {
            "CommonParms": {
                "action": "create"
            },
            "request": {
                # user or business json goes here
            }
        }

# for update would be very simular to create

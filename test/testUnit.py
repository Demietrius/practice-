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
            "commonParms": {
                "action": "read"
            }
        }
        app.start(payload)

    # payload for create should look like this
    def test_create(self):
        payload = {
            "commonParms": {
                "action": "create",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "businessId": 123,
                    "firstName": "Joe",
                    "lastName": "Jake",
                    "age": 22
                }
            }
        }
        app.handler(payload)

    def testUpdate(self):
        payload = {
            "commonParms": {
                "action": "update",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "businessId": 123,
                    "firstName": "Joe",
                    "lastName": "Jake",
                    "age": 22,
                    "userId": 23439,
                    "lastUpdated": "02/22/2022T12:00:01.003",
                    "lastUpdatedBy": 29393
                }
            }
        }

    # for update would be very simular to create

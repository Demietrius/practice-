from unittest import TestCase
import user_business_API

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
            "commonParams": {
                "action": "create",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "firstName": "Mecole",
                    "lastName": "Hardman",
                    "salary": 500000,
                    "sex": "M",
                    "worksFor": 1
                }
            }
        }
        user_business_API.create_handler(payload)

    def testUpdate(self):
        payload = {
            "commonParms": {
                "action": "update",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "firstName": "Mecole",
                    "lastName": "Hardman",
                    "salary": 1200000,
                    "sex": "M",
                    "worksFor": 1,
                    "userID": 6
                }
            }
        }
        user_business_API.update_handler(payload)
    # for update would be very simular to create

from unittest import TestCase
import user_business_API

class testUnit(TestCase):

    def test_read(self):
        payload = {
            "commonParams": {
                "action": "read",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "userID": "11"
                    }
            }
        }
        user_business_API.handler(payload)


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
        user_business_API.handler(payload)

    def testUpdate(self):
        payload = {
            "commonParams": {
                "action": "update",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "firstName": "Trey",
                    "lastName": "Smith",
                    "salary": 1500000,
                    "sex": "M",
                    "worksFor": 1,
                    "userID": 1
                }
            }
        }
        user_business_API.update_handler(payload)
    # for update would be very simular to create

    def test_delete(self):
        payload = {
            "commonParams": {
                "action": "delete",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "userID": "11"
                    }
            }
        }
        user_business_API.handler(payload)

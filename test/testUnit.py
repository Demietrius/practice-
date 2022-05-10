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
                    "userID": "3"
                }
            }
        }
        user_business_API.handler(payload)

    def test_create(self):
        payload = {
            "commonParams": {
                "action": "create",
                "domain": "userProfile"
            },
            "request": {
                "user": {
                    "firstName": "Nick",
                    "lastName": "Bolton",
                    "salary": 2500000,
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
        user_business_API.handler(payload)

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

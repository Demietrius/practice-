import user_business_API
from db_access import DatabaseAccessor



def test_read():
    payload = {
        "commonParams": {
            "action": "read"
        },
        "request": {
            "user": {
                "userID": "5"
            }
        }
    }
    user_business_API.handler(payload)
    print(DatabaseAccessor.read.read_results)

test_read()

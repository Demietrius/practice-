
def user_input():
    request = input("Command List:"
                    "\n **********"
                    "\n add_user"
                    "\n update_user"
                    "\n lookup_all_users"
                    "\n lookup_single_user"
                    "\n lookup_self"
                    "\n delete_user"
                    "\n **********"
                    "\nEnter command: ")

user_input()

def read():
    payload = {
        "commonParams":{

            "lookup_all_users": "read",
            "lookup_single_user": "read",
            "lookup_self": "read"
        }
    }


from db_access import DatabaseAccessor
import json

with open("../src/db_login.json", "r") as f:
    db_login = json.load(f)
    host = db_login["login"]["host"]
    user = db_login["login"]["user"]
    password = db_login["login"]["password"]
    database = db_login["login"]["database"]
    database = DatabaseAccessor(host, user, password, database)


def create_handler(request):
    if "user" not in request["request"]:
        return 2, "error: no data for user"
    database.create(request["request"]["user"])


def update_handler(request):
    if "user" not in request["request"]:
        return 2, "error: no data for user"
    database.update(request["request"]["user"])


def read_handler(request):
    if "user" not in request["request"]:
        return 2, "error: no data for user"
    database.read(request["request"]["user"]["userID"])


def delete_handler(request):
    if "user" not in request["request"]:
        return 2, "error: no data for user"
    database.delete(request["request"]["user"]["userID"])


def handler(request):
    if "commonParams" not in request:
        return 2, " error: missing common parameter (commonParams)"

    if "domain" in request["commonParams"] \
            and "action" in request["commonParams"] \
            and request["commonParams"]["domain"] == "userProfile":

        if request["commonParams"]["action"] == "create":
            create_handler(request)
        if request["commonParams"]["action"] == "update":
            update_handler(request)
        if request["commonParams"]["action"] == "read":
            read_handler(request)
        if request["commonParams"]["action"] == "delete":
            delete_handler(request)

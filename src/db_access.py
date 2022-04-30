class DBAccess:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


class Business:

    def __init__(self, business_id, business_name, business_type, number_of_employees):
        self.business_id = int(business_id),
        self.business_name = business_name,
        self.business_type = business_type,
        self.number_of_employees = int(number_of_employees)


class User:

    def __init__(self, first_name, last_name, salary, sex, user_id, works_for):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.sex = sex
        self.user_id = user_id
        self.works_for = works_for



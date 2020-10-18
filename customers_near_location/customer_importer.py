import json

class Customer():
    def __init__(self, latitude, user_id, name, longitude):
        self.latitude = float(latitude)
        self.user_id = user_id
        self.name = name
        self.longitude = float(longitude)

def import_customers(filename: str) -> list: 
    with open(filename) as customer_file:
        customer_string_list = list(customer_file)

    customer_list = [Customer(**json.loads(string)) for string in customer_string_list]

    return customer_list
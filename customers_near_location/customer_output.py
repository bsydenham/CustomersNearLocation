import json

class CustomerOutput:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

def output_customers(filename: str, customers: list):
    write_list = []
    for customer in customers:
        write_list.append(CustomerOutput(customer.user_id, customer.name))
    with open(filename, 'w') as f:
        for customer_output in write_list:
            f.write(json.dumps(customer_output.__dict__) + '\n')
    
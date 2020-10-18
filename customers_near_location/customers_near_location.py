import configparser
from . import config
from . import customer_importer
from . import customers_within_distance
from . import customer_output

def get_customers_near_location() -> None:
    configuration = config.get_config(configparser.ConfigParser())

    customers = customer_importer.import_customers(configuration['import_filename'])

    filtered_customers = customers_within_distance.get_customers_within_distance(customers, configuration['coordinates'], configuration['distance_limit_km'])

    customer_output.output_customers(configuration['output_filename'], filtered_customers)
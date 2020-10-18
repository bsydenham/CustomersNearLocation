# CustomersNearLocation
Python script to import list of JSON object customers then filtering out those which are outside of a configured range of a desired location, by using latitude and longitude coordinates.

To run:

1. [Install Python](https://www.python.org/downloads/) if not installed already, make sure it has been added to PATH in Windows
2. Configure `config.ini` file to desired settings (defaults already set)
3. Open command window at repository location, type `python -m customers_near_location` to run, or `python -m unittest` to run tests (integration test will also run)
4. View output file for results
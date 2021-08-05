from .models import Sample
from .foundation import database

# List of tables to create in database
tables = [Sample]

def create_tables():
    with database:
        database.create_tables([Sample])
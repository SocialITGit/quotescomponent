import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime



@anvil.server.callable
def createPackage(package):
  app_tables.packages.add_row(
    created=datetime.now(),
    name=package.name,
    description= package.description,
    price=package.price,
    items = package.items
  )

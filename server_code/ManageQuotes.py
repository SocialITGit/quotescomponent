import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime




@anvil.server.callable
def createItem(item):
  app_tables.items.add_row(
    created=datetime.now(),
    name=item.name,
    description= item.description,
    price=item.price
  )
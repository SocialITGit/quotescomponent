import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime




@anvil.server.callable
def create_item(item):
  app_tables.items.add_row(
    created=datetime.now(),
    name=item.name,
    description= item.description,
    price=item.price,
    image = item.image,
    user = 'davide.lissoni@socialit.it'
  )


@anvil.server.callable
def find_all_items():
  return app_tables.items.search()
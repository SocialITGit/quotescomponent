import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime



@anvil.server.callable
def find_davide():
   return app_tables.users.get(email='davide.lissoni@socialit.it')
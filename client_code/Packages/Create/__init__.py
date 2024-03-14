from ._anvil_designer import CreateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Create(CreateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    items =  [(item['name'], item) for item in anvil.server.call('findAllItems')] 
    self.drdItems = items;
    # Any code you write here will run before the form opens.

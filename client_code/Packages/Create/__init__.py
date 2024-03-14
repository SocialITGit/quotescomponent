from ._anvil_designer import CreateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Items.ViewCard import ViewCard

class Create(CreateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selecteItems =[];
    items =  [(item['name'], item) for item in anvil.server.call('findAllItems')] 
    self.drdItems.items = items;
    # Any code you write here will run before the form opens.
  def btnAddItem_click(self, **event_args):
    item = self.drdItems.selected_value
    self.selecteItems.append(item)
    self.repItems.items = self.selecteItems
    pass

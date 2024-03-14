from ._anvil_designer import CreateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Items.ViewCard import ViewCard
from .. import Model

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

  def btnCreate_click(self, **event_args):
      package = Model.Package(self.txtName.text, self.txtDescription.text, self.txtPrice.text, self.selecteItems)
      anvil.server.call('createPackage', package)
  pass

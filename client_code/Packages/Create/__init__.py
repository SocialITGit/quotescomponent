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
    self.selected_items =[];
    self.user =  anvil.server.call('find_davide') 
    items =  [(item['name'], item) for item in anvil.server.call('find_items_by_user', self.user)] 
    self.drop_down_items.items = items;
    # Any code you write here will run before the form opens.
  
  
  def button_add_item_click(self, **event_args):
    item = self.drop_down_items.selected_value
    self.selected_items.append(item)
    self.repeating_panel_items.items = self.selected_items
    pass

  def button_create_package_click(self, **event_args):
      package = Model.Package(self.text_box_name.text, self.text_area_description.text, self.text_box_price.text, self.selected_items, self.user)
      anvil.server.call('create_package', package)
  pass

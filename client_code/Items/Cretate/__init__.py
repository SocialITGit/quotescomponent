from ._anvil_designer import CretateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from form_checker import validation
from .. import Model

class Cretate(CretateTemplate):
  def __init__(self, **properties):
    # validazione form
    self.init_components(**properties)
    self.validator = validation.Validator()
    self.validator.require_text_field(self.text_box_name, self.label_name_error)
    self.validator.require_text_field(self.text_box_price, self.label_price_error)
    

  def button_create_click(self, **event_args):
    if self.validator.is_valid():
      item = Model.Item(self.text_box_name.text, self.text_area_description.text, self.text_box_price.text, self.image_primary.source)
      anvil.server.call('create_item', item)
      
    else:
      self.validator.show_all_errors()
    
  pass

  def button_upload_image_change(self, file, **event_args):
    self.image_primary.source = file
    pass

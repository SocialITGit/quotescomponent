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
    self.validator.require_text_field(self.txtName, self.lblNameError)
    self.validator.require_text_field(self.txtPrice, self.lblPriceError)
    

  def button_create_click(self, **event_args):
    if self.validator.is_valid():
      item = Model.Item(self.txtName.text, self.txtDescription.text, self.txtPrice.text, self.imgPrimary.source)
      anvil.server.call('createItem', item)
      
    else:
      self.validator.show_all_errors()
    
  pass

  def button_upload_image_change(self, file, **event_args):
    self.imgPrimary.source = file
    pass

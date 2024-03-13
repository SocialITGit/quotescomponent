from ._anvil_designer import CretateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from form_checker import validation

class Cretate(CretateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.validator = validation.Validator()
    self.validator.require_text_field(self.txtName, self.lblNameError)
    self.validator.require_text_field(self.txtPrice, self.lblPriceError)
    
    # Any code you write here will run before the form opens.

  def btnCreate_click(self, **event_args):
    if self.validator.is_valid():
      alert("Thanks for signing up")
    else:
      self.validator.show_all_errors()
    
  pass

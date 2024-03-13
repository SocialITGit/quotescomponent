import anvil.server

@anvil.server.portable_class
class Item:
    def __init__(self, name, description, price, image):
      self.name = name
      self.description = description
      self.price = price
      self.image = image


    def set_created(self, created):
      self.created = created
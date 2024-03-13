import anvil.server

@anvil.server.portable_class
class Item:
    def __init__(self, name, description, price):
      self.name = name
      self.description = description
      self.price = price


    def set_created(self, created):
      self.created = created
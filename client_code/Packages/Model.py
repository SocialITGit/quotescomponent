import anvil.server

@anvil.server.portable_class
class Package:
    def __init__(self, name, description, price, items):
      self.name = name
      self.description = description
      self.price = price
      self.items = items


    def set_created(self, created):
      self.created = created
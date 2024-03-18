import anvil.server

@anvil.server.portable_class
class Package:
    def __init__(self, name, description, price, items, user):
      self.name = name
      self.description = description
      self.price = price
      self.items = items
      self.user = user


    def set_created(self, created):
      self.created = created
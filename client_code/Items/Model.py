import anvil.server

@anvil.server.portable_class
class Item:
    def __init__(self, name, description, price, image, user):
      self.name = name
      self.description = description
      self.price = price
      self.image = image
      self.user = user


    def set_created(self, created):
      self.created = created
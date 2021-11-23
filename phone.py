
from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
       #call to super function to have access to all the attributes/ methods
       super().__init__(
           name,price, quantity
       )
       #run validations to received arguments
       assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater tham zero !"

       #assign to self object
       self.broken_phones = broken_phones
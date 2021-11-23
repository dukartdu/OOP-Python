
from item import Item


class Keyboard(Item):
    pay_rate = 0.3
    def __init__(self, name: str, price: float, quantity=0):
       #call to super function to have access to all the attributes/ methods
       super().__init__(
           name,price, quantity
       )
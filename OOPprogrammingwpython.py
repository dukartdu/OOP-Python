from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("myItem", 750, 6)
item1 = Phone("myItem", 1000, 3)
item1 = Keyboard("g213", 1900, 3)

# setting an attribute

item1.name = "othertitem"

#getting an attribute
print(item1.name)


item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)

item1.send_email()







 
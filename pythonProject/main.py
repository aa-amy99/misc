from item import Item
from phone import Phone
from keyboard import Keyboard
'''
Item.instantiate_from_csv()
print(Item.all)

phone1 = Phone('phone10', 500, 5,1)
phone2 = Phone('phone20', 1000, 5,1)
print(Item.all)
print(Phone.all)

'''
'''
1. Encapsulation
item1 = Item("myitem", 759)
#setter
item1.name = "other"
#getter
print(item1.name) #no access to private property AttributeError: 'Item' object has no attribute '__name'
item1.apply_discount()
print(item1.price)
'''

'''
2. Abstraction
item1 = Item("myitem", 759)
item1.send_email()
item1.connect() #private method not accessible by instance
'''

'''
3. Inheritance
phone1 = Phone("phone", 1000, 3)
phone1.apply_discount()
print(phone1.price)
'''

'''
4. Polymorism 
keyboard1 = Keyboard("key-00", 1000, 3)
keyboard1.apply_discount()
print(keyboard1.price)
'''

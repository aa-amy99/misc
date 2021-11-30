import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: int, quantity=0):
        # Run validation to receive arguments
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f" quantity {quantity} is not greater than 0"

        # Constructor
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        print(self.price * self.quantity)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls): #class method
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f) #{'name': "'phone'", 'price': '100', 'quantity': '1'}
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        #count the floats that are point .0 i.e. 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): #return the string to represent obj: Item(phone, 100, 1)
        return f"Item({self.name}, {self.price}, {self.quantity})"

item1 = Item('phone', 100, 1)
item2 = Item('labtop', 1000, 3)
item3 = Item('cable', 10, 5)
item4 = Item('mouse', 50, 5)
item5 = Item('keyboard', 75, 5)

'''
###### Attribute vs Instance
item1.calculate_total_price()
item2.calculate_total_price()
item1.apply_discount()
print(f"discount price: {item1.price}") #80

item2.pay_rate = 0.7
item2.apply_discount()
print(f"discount price: {item2.price}")#70

print(Item.__dict__) #show all attr at class level {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x7f9c2b8a3790>, 'calculate_total_price': <function Item.calculate_total_price at 0
print(item1.__dict__) #show all attr at instance level {'name': 'phone', 'price': 100, 'quantity': 5}
item2.has_numpad = False


###### append objects to list to be shred in class
#print(Item.all) [Item(phone, 100, 1), Item(labtop, 1000, 3), Item(cable, 10, 5), Item(mouse, 50, 5), Item(keyboard, 75, 5)]
#print(item1.all)


###### class method
Item.instantiate_from_csv()
print(Item.all)

####### static method
print(Item.is_integer(7.0))

'''



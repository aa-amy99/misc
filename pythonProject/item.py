import csv

'''
Inheritance
'''

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: int, quantity=0):
        # Run validation to receive arguments
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f" quantity {quantity} is not greater than 0"

        # Constructor
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    # Getter >> Read-Only attribute >> protect attribute to be reset  Item.name can't be set but Item._name can still set
    # use __ is equal to private attribute which can't be modify
    def name(self):
        return self.__name

    # 1. encapsulation
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, inc):
        self.__price = self.__price + self.__price * inc

    @name.setter
    #Setter
    def name(self, value):
        if len(value) > 10:
            raise Exception ("Name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        print(self.__price * self.quantity)


    @classmethod
    def instantiate_from_csv(cls): #class method
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f) #{'name': "'phone'", 'price': '100', 'quantity': '1'}
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                __price=float(item.get('price')),
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
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})"


    #2. abstraction by private methods
    def __connect(self, server):
        pass

    def __prepare_body(self):
        return f"Hello {self.name}"

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()


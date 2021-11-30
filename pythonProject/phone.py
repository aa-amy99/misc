from item import Item

class Phone(Item):
    pay_rate = 0.9
    def __init__(self, name: str, __price: int, quantity=0, broken_phones=0):

        #call super function to access all attribute/methods
        super().__init__(name, __price, quantity)

        # Run validation to receive arguments
        assert broken_phones >= 0, f" broken_phones {broken_phones} is not greater than 0"
        # Constructor
        self.broken_phones = broken_phones
        # Action to execute





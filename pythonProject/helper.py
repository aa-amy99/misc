class Item:
    @staticmethod #related to class but not unique per instance
    def is_integer(param): #not pass the class or obj as param
        return param.is_integer()

    @classmethod #related to class used to manipulate the structure of data
    def instantiate_from_csv(cls):  # class method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)  # {'name': "'phone'", 'price': '100', 'quantity': '1'}
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

#you should call from Class level not Instance like item1.is_integer()
Item.is_integer(7)
Item.instantiate_from_csv()
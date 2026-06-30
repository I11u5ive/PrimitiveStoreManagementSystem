

class Product:
    def __init__(self, name: str, toy_type: str, price: int | float, quantity: int):
        self.name = name
        self.toy_type = toy_type
        self.price = price
        self.quantity = quantity

    # Getters:

    @property
    def price(self) -> int | float:
        return self.__price

    @property
    def quantity(self) -> int:
        return self.__quantity

    # Setters:

    @price.setter
    def price(self, new_price: int | float):
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError('Price cannot be less than 0.')

    @quantity.setter
    def quantity(self, new_quantity: int):
        if new_quantity >= 0:
            self.__quantity = new_quantity
        else:
            raise ValueError('Quantity cannot be less than 0.')

    #Other methods:

    def __str__(self):
        return f'{self.name} | {self.toy_type} | {self.price}$ | {self.quantity}'


class Order:

    def __init__(self):
        self.toys = []
        self.__total_price = 0

    # Getters:

    @property
    def total_price(self) -> int | float:
        return self.__total_price

    # Other methods:

    def __str__(self):
        text = 'Order:\n'
        for toy in self.toys:
            text += toy + '\n'
        text += f'Total price: {self.total_price}$'

        return text

    def __update_total_price(self):
        self.__total_price = sum(toy.price for toy in self.toys)

    def add_toy(self, new_toy: Product, new_quantity = 1):
        if new_quantity < 1:
            raise ValueError("Quantity cannot be less then 1.")

        if new_toy.quantity >= new_quantity:
            self.toys.append(new_toy)
            new_toy.quantity(new_toy.quantity - new_quantity)
            self.__update_total_price()
            print(f'Added {new_quantity} items of {new_toy} to order.')
        else:
            print(f'Not enough {new_toy.name}`s quantity in stock.')


class Customer:

    def __init__(self, name: str, email: str, order: list[Order]):
        self.name = name
        self.email = email
        self.order = order

    # Getters:

    @property
    def email(self) -> str:
        return self.__email

    # Setters:

    @email.setter
    def email(self, new_email: str):
        if '@' in new_email:
            self.__email = new_email
        else:
            raise ValueError('Email must contain @.')

    # Other methods:

    def __str__(self):
        return f'{self.name} ({self.email})'

    def add_order(self, new_order: Order):
        if len(new_order.toys) > 0:
            self.order.append(new_order)
        else:
            raise ValueError('Order must contain at least 1 element')



def main():
    pass




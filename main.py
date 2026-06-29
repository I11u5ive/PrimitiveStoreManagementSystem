

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



class Order:

    __total_price = 0

    def __init__(self, toys: list[Product]):
        self.toys = toys
        self.__update_total_price()

    # Getters:

    @property
    def toys(self) -> list[Product]:
        return self.__toys

    @property
    def total_price(self) -> int | float:
        return self.__total_price

    # Setters:

    @toys.setter
    def toys(self, new_toys: list[Product]):
        self.__toys = new_toys
        self.__update_total_price()

    # Other methods:

    def __update_total_price(self):
        self.__total_price = sum(product.price for product in self.toys)

    def add_toy(self, new_toy: Product):
        self.__toys.append(new_toy)
        self.__update_total_price()


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

    def add_order(self, new_order: Order):
        if len(new_order.toys) > 0:
            self.order.append(new_order)
        else:
            raise ValueError('Order must contain at least 1 element')



def main():
    pass




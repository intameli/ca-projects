class House:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price can't be negative")


    def display_price(self):
        print(f'Price of the house is {self.__price}')

house = House(80_000)

house.price = -100_000

print(house.price)

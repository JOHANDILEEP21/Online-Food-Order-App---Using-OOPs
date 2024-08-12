from Models.AbstractItem import AbstractItem
from Models.FoodMenu import FoodMenu


class Restaurant:

    def __init__(self, name, rating, location, offer):
        #super().__init__(name, rating)
        self.name = name
        self.rating = rating
        self.Location = location
        self.offer = offer
        self.__FoodMenus = []

    @property
    def FoodMenus(self):
        return self.__FoodMenus

    @FoodMenus.setter
    def FoodMenus(self, items):
        for item in items:
            if not isinstance(item, FoodMenu):
                print('Invalid FoodMenu')
                return

        self.__FoodMenus = items

    def DisplayItem(self, start):
        print(f'{start}=> {self.name} => Rating: {self.rating}')
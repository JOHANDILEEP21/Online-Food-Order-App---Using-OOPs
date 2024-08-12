from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant

class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()
        #self.__FoodMenus = []

    def __PrepareFoodItems(self):
        item1 = FoodItem(name='VegBiriyani', rating=4.0, price=150, description='*****')
        item2 = FoodItem(name='ChickenBiriyani', rating=4.2, price=200, description='*****')
        item3 = FoodItem(name='Dosa', rating=4.4, price=60, description='*****')
        item4 = FoodItem(name='Parotta', rating=4.4, price=50, description='*****')
        item5 = FoodItem(name='Noodles', rating=3.8, price=100, description='*****')
        item6 = FoodItem(name='MuttonBiriyani', rating=4.6, price=250, description='*****')
        return [item1, item2, item3, item4, item5, item6]

    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()
        menu1 = FoodMenu('Veg')
        menu1.FoodItems = [FoodItems[0], FoodItems[2]]
        menu2 = FoodMenu('Non-Veg')
        menu2.FoodItems = [FoodItems[1], FoodItems[3], FoodItems[5]]
        menu3 = FoodMenu('Chinese')
        menu3.FoodItems = [FoodItems[4]]
        return [menu1, menu2, menu3]

    def __PrepareRestaurants(self):
        FoodMenus = self.__PrepareFoodMenus()

        # res1 = Restaurant.FoodMenus(name='A2B', rating=5, location='Chennai', offer=10)
        res1 = Restaurant(name='A2B', rating=5, location='Chennai', offer=10)
        res1.FoodMenus = [FoodMenus[0]]

        # res2 = Restaurant.FoodMenus(name='Muniyandivilas', rating=4.5, location='Bangalore', offer=20)
        res2 = Restaurant(name='Muniyandivilas', rating=4.5, location='Bangalore', offer=20)
        res2.FoodMenus = [FoodMenus[0], FoodMenus[1]]

        # res3 = Restaurant.FoodMenus(name='KFC', rating=4.8, location='Coimbatore', offer=15)
        res3 = Restaurant(name='KFC', rating=4.8, location='Coimbatore', offer=15)
        res3.FoodMenus = [FoodMenus[1], FoodMenus[2]]

        return [res1, res2, res3]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.name == name:
                return res

    def FindFood(self, name):
        for food in self.__PrepareFoodItems():
            if food.Name == name:
                return food

    def displayItems(self):
        FoodItems = self.__PrepareFoodItems()
        return FoodItems

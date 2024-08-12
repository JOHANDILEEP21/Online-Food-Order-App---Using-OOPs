from Controllers.FoodManager import FoodManager
from Models.Cart import Cart


class MainMenu:
    __Options = {1: 'Show Restaurants', 2: 'Show FoodItems', 3: 'Search Restaurant', 4: 'Search FoodItem', 5: 'Logout'}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItem(i)
        print()
        try:
            choice = int(input('Please select the Restaurant: '))
            res = self.__FoodManager.Restaurants[choice-1]
            self.ShowFoodMenus(res.FoodMenus)
        except Exception as e:
            print('Please select a Valid Restaurant...')

    def ShowFoodItems(self, foodItems=None):
        if foodItems is not None:
            for i, item in enumerate(foodItems, 1):
                item.DisplayItem(i)
            print()
            try:
                choices = list(map(int, input('Please choose your Food Items (eg: 1,1,2): ').split(',')))
                cart = Cart(foodItems, choices)
                cart.ProcessOrder(foodItems)
            except Exception as e:
                print('Please select the valid Food Items.')
        else:
            res = self.__FoodManager.displayItems()
            for i, item in enumerate(res, 1):
                item.DisplayItem(i)
            print()
            try:
                choices = list(map(int, input('Please choose your Food Items (eg: 1,2,3): ').split(',')))
                cart = Cart(res, choices)
                cart.ProcessOrder(res)
            except Exception as e:
                print('Please select the valid FoodItems;')

    def SearchRestaurant(self):
        resName = input('Enter Restaurant Name: ')
        res = self.__FoodManager.FindRestaurant(resName)

        if res is not None:
            print('Restaurant Found...')
            print(f'Name: {res.name}, Rating: {res.rating}, Location: {res.Location}, Offer: {res.offer}', end='\n\n')
            self.ShowFoodMenus(res.FoodMenus)

        else:
            print(f'No Restaurant found on the name {resName}')

    def SearchFoodItem(self):
        foodName = input('Enter Food Name: ')
        res = self.__FoodManager.FindFood(foodName)

        if res is not None:
            print('Food Item Found...')
            print(f'Name: {res.Name}, Rating: {res.Rating}, Price: {res.Price}, Description: {res.Description}', end='\n\n')
        else:
            print(f'No Food found on the name {foodName}\n')

    def ShowFoodMenus(self, menus):
        print('\nList of Menus available...')
        for i, menu in enumerate(menus, 1):
            menu.DisplayItem(i)
        print()
        try:
            choice = int(input('Please choose menu: '))
            fooditems = menus[choice-1].FoodItems
            self.ShowFoodItems(fooditems)
        except Exception as e:
            print('Please select a valid Menu.')

    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f'{option}. {MainMenu.__Options[option]}', end=' ')
            print()

            try:
                choice = int(input('Please enter your choice: '))
                if choice == 5:
                    exit()
                else:
                    value = MainMenu.__Options[choice].replace(' ', '')
                    print('-----------------------------------------------------------')
                    print(f'Your choice is: -- {value} --')
                    print('-----------------------------------------------------------')
                    getattr(self, value)()
            except (ValueError, KeyError):
                print('Invalid choice. :( Please enter the correct choice... :)')

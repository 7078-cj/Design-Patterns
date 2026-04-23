from abc import ABC, abstractmethod

class FoodType:
    french = 1
    american = 2
    


class Restaurant(ABC):
    @abstractmethod
    def make_food(self, food_type):
        pass
    
    @abstractmethod
    def make_drink(self, drink_type):
        pass
    
class FrenchRestaurant(Restaurant):
    def make_food(self):
        print('Making French food')
        
    def make_drink(self):
        print('Making French drink')
        
class AmericanRestaurant(Restaurant):
    def make_food(self):
        print('Making American food')
        
    def make_drink(self):
        print('Making American drink')

#abstract factory
class RestaurantFactory:
    def suggest_restaurant(self, r_type: FoodType):
        if r_type == FoodType.french:
            return FrenchRestaurant()
        elif r_type == FoodType.american:
            return AmericanRestaurant()
        else:
            raise ValueError('Invalid food type')
        
def dine_at(restaurant: Restaurant):
    restaurant.make_food()
    restaurant.make_drink()
    
if __name__ == '__main__':
    suggestion = RestaurantFactory()
    restaurant = suggestion.suggest_restaurant(FoodType.french)
    restaurant2 = suggestion.suggest_restaurant(FoodType.american)
    
    dine_at(restaurant)
    dine_at(restaurant2)
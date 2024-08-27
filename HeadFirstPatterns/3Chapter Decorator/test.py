from base_coffe import Beverage
from coffee import HoseBlend, Espresso, Decaf, DarkRoast
from condiment import Milk, Mocha, Soy, Whip


bev = Espresso()
print(bev.get_description(), bev.cost())
print("---------------------------------------")
bev1 = DarkRoast()
bev1 = Mocha(bev1)
bev1 = Mocha(bev1)
bev1 = Whip(bev1)
print(bev1.get_description(), bev1.cost())
print("---------------------------------------")
bev2 = HoseBlend()
bev2 = Soy(bev2)
bev2 = Mocha(bev2)
bev2 = Whip(bev2)
print(bev2.get_description(), bev2.cost())

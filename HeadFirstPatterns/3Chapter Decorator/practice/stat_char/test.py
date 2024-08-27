from char_stat_base import WarriorStats, RogueStats, MageStats, PristStats
from item_stat import Axe, LeatherArmor, PristBook


axe = Axe()
print(f"{axe.get_strength()} силы")
print(f"{axe.get_intelligence()} интеллекта")
print("-----------------------------")

war = WarriorStats()
war = Axe(war)
war = LeatherArmor(war)
war = PristBook(war)
print(war.get_description())
print(war.get_all_stat())
# print(war.get_strength())
# print(war.get_stamina())
# print(war.get_agility())
# print(war.get_intelligence())
# print(war.get_spirit())

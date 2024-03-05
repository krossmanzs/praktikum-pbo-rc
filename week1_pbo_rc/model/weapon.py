import random

class Weapon:
    def __init__(self, name, critical_rate, attack_base):
        self.__name = name
        self.__critical_rate = critical_rate
        self.__attack_base = attack_base
    
    def get_damage(self):
        critical_chance = random.random()

        if(self.__critical_rate > critical_chance):
            # if critical rate occurred, damage will be:
            # default_atk + random_num_between(default_atk / 2)_until_default_atk
            damage = round(self.__attack_base + random.uniform(self.__attack_base/2, self.__attack_base), 1)
            print(f"DMG: {damage} | Critical..!!")
            return damage
        else:
            damage = self.__attack_base
            print(f"DMG: {damage} | Normal hit...")
            return damage

    def get_name(self):
        return self.__name

    def show_detail(self):
        print(f"Weapon name: {self.__name}")
        print(f"Base ATK   : {self.__attack_base}")
        print(f"Crit. Rate : {self.__critical_rate*100}%")
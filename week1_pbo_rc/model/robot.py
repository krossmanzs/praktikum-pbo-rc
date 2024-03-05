import random
from .weapon import Weapon
from config.config import Config

class Robot:
    def __init__(self, name, weapon: Weapon, health: float):
        self.__name = name
        self.__weapon = weapon
        self.__health = health
        self.__base_health = health
        self.__regen_countdown = Config.DEFAULT_REGEN_COUNTDOWN
        self.__stunt_countdown = Config.DEFAULT_STUNT_COUNTDOWN
        self.__stunted = False

    ## getter methods
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def is_stunted(self):
        return self.__stunted

    def get_regen_countdown(self):
        return self.__regen_countdown

    def get_stunt_countdown(self):
        return self.__stunt_countdown

    ## setter methods
    def set_regen_countdown(self, value):
        self.__regen_countdown = value

    def set_stunt_countdown(self, value):
        self.__stunt_countdown = value

    def set_stunt_status(self, value: bool):
        self.__stunted = value

    ## main robot methods
    # method to attack an enemy
    def attack_enemy(self, target):
        print(f"{self.__name} attacking {target.get_name()}")
        target.attacked(self.__weapon)

    def stunt_enemy(self, target):
        print(f"{self.__name} use stunt to {target.get_name()}")

    # method to get attacked by someone with weapon
    def attacked(self, weapon: Weapon):
        damage = weapon.get_damage()
        if (self.__health - damage) < 0:
            self.__health = 0
        else:
            self.__health -= damage

    # method to regen
    def regen(self):
        if self.get_regen_countdown() == 0:
            regen_value = round(random.uniform(self.__base_health/2, self.__base_health) / 2, 1)

            self.__health += regen_value
            if self.__health > self.__base_health:
                self.__health = self.__base_health
                
            print(f"{self.get_name()} regen {regen_value} HP")
            self.set_regen_countdown(Config.DEFAULT_REGEN_COUNTDOWN)
        else:
            print(f"Cannot regen HP, need {self.get_regen_countdown()} more round(s)!")
    
    def stunt(self, target):
        if self.get_stunt_countdown() == 0:
            target.set_stunt_status(True)
            print(f"{self.get_name()} stunt {target.get_name()}")
            self.set_stunt_countdown(Config.DEFAULT_STUNT_COUNTDOWN)
        else:
            print(f"Cannot use stunt, need {self.get_stunt_countdown()} more round(s)!")

    # method to show detail of this robot
    def show_detail(self):
        regen = "READY" if self.get_regen_countdown() == 0 else "NOT READY"
        stunt = "READY" if self.get_stunt_countdown() == 0 else "NOT READY"
        print(f"Name: {self.__name} | HP: {round(self.__health,1)} | Regen: {regen} | Stunt: {stunt}")
from model.robot import Robot
from model.weapon import Weapon
from config.config import Config

class Game:
    def __init__(self, name):
        self.__name = name
        self.__running = True
        self.__round = 1
        print(f"{self.__name} Game Successfully Created!")

        self.__weapons = list()
        
        self.__winner = None
        self.__draw = False

    def run(self):
        print("\nSelect option:")
        print("1. Skip weapons and robot creation and use default settings instead")
        print("2. Create your own weapons and robots manually")
        print("3. Exit")
        option = int(input("Your option[1-3]: "))

        if option == 1:
            self.__apply_default_settings()
            self.__fight()
        elif option == 2:
            print("\nFirst, you need to create your own weapon and robots")
            self.__create_weapons()
            self.__show_weapons()
            self.__create_robots()
            self.__fight()
        elif option == 3:
            print("Ok, Goodbye m8")
        else:
            print("Njir, milih apa lu cok akwowkow. Dahlah males")

    def __apply_default_settings(self):
        wp1 = Weapon(Config.DEFAULT_WP1_NAME, Config.DEFAULT_WP1_CR, Config.DEFAULT_WP1_BASE_ATK)
        wp2 = Weapon(Config.DEFAULT_WP2_NAME, Config.DEFAULT_WP2_CR, Config.DEFAULT_WP2_BASE_ATK)

        self.__robot_a = Robot(Config.DEFAULT_RB1_NAME, wp1, Config.DEFAULT_ROBOT_HEALTH)
        self.__robot_b = Robot(Config.DEFAULT_RB2_NAME, wp2, Config.DEFAULT_ROBOT_HEALTH)

        self.__weapons.append(wp1)
        self.__weapons.append(wp2)

        print("Default settings successfully loaded..")

    def __create_robots(self):
        print(f"\n{'#'*20}")
        print("Creating two robots...")
        rb1_name = input("Insert Robot 1 name: ")
        rb1_wp_idx = int(input("Insert Weapon index for Robot 1: "))
        rb2_name = input("Insert Robot 2 name: ")
        rb2_wp_idx = int(input("Insert Weapon index for Robot 2: "))
        rb_health = float(input("Insert health for both robot: "))

        self.__robot_a = Robot(rb1_name, self.__weapons[rb1_wp_idx], rb_health)
        self.__robot_b = Robot(rb2_name, self.__weapons[rb2_wp_idx], rb_health)
        print("Success create robots!")

    def __create_weapons(self):
        done = False

        while not done:
            print("\n### Adding new weapon ###")
            wp_name = input("Insert weapon name: ")
            wp_atk_base = float(input("Insert weapon base attack damage: "))
            crit_rate = float(input("Insert critical rate percentage (0.0-1.0): "))
            weapon = Weapon(wp_name, crit_rate, wp_atk_base)
            self.__weapons.append(weapon)
            print(f"{wp_name} added to weapon list..")
            more = input("Add more weapon (Y/N):").lower()
            done = False if more == 'y' else True
    
    def __show_weapons(self):
        for idx, weapon in enumerate(self.__weapons):
            print(f"\n{'#'*20}")
            print(f"Weapon[{idx}]")
            weapon.show_detail()

    def __fight(self):
        print("\nThe game are good to go, let's start the journey. Good Luck Have Fun!")
        
        while self.__running:
            self.__check_win()

            if self.__winner != None:
                print(f"\n{'-'*20} Winner is {self.__winner} {'-'*20}")
                self.__running = False
            elif self.__draw:
                print(f"\n{'-'*20} The game is draw {'-'*20}")
                self.__running = False
            else:
                print(f"\nRound-{self.__round} {'='*80}")
                self.__robot_a.show_detail()
                self.__robot_b.show_detail()
                
                choose_a = ''
                choose_b = ''
                is_robot_a_stunted = self.__robot_a.is_stunted()
                is_robot_b_stunted = self.__robot_b.is_stunted()

                if is_robot_a_stunted:
                    print(f"\n{self.__robot_a.get_name()}, you are stunted!")
                    self.__robot_a.set_stunt_status(False) # reset stunt status
                elif self.__winner == None:
                    while choose_a != '1' and choose_a != '2' and choose_a != '3' and choose_a != '4' and choose_a != '5':
                        print("\n1. Attack\t2. Regen\t3. Stunt\t4. Giveup")
                        choose_a = input(f"{self.__robot_a.get_name()}, Select the action: ")
                        if choose_a == '1':
                            self.__robot_a.attack_enemy(self.__robot_b)
                        elif choose_a == '2':
                            if self.__robot_a.get_regen_countdown() != 0:
                                choose_a = ''
                            self.__robot_a.regen()
                        elif choose_a == '3':
                            self.__robot_a.stunt(self.__robot_b)
                        elif choose_a == '4':
                            print(f"{self.__robot_a.get_name()} gave up :(")
                            self.__winner = self.__robot_b.get_name()

                if is_robot_b_stunted:
                    print(f"\n{self.__robot_b.get_name()}, you are stunted!")
                    self.__robot_b.set_stunt_status(False) # reset stunt status
                elif self.__winner == None:
                    while choose_b != '1' and choose_b != '2' and choose_b != '3' and choose_b != '4' and choose_b != '5':
                        print("\n1. Attack\t2. Regen\t3. Stunt\t4. Giveup")
                        choose_b = input(f"{self.__robot_b.get_name()}, Select the action: ")
                        if choose_b == '1':
                            self.__robot_b.attack_enemy(self.__robot_a)
                        elif choose_b == '2':
                            if self.__robot_b.get_regen_countdown() != 0:
                                choose_b = ''
                            self.__robot_b.regen()
                        elif choose_b == '3':
                            self.__robot_b.stunt(self.__robot_a)
                        elif choose_b == '4':
                            print(f"{self.__robot_b.get_name()} gave up :(")
                            self.__winner = self.__robot_a.get_name()

                self.__update_cooldown(self.__robot_a)
                self.__update_cooldown(self.__robot_b)

                self.__round += 1

    def __update_cooldown(self, robot: Robot):
        cd_regen = robot.get_regen_countdown()
        cd_stunt = robot.get_stunt_countdown() 

        if cd_regen != 0:
            robot.set_regen_countdown(cd_regen-1)
        
        if(cd_stunt != 0):
            robot.set_stunt_countdown(cd_stunt-1)
    
    def __check_win(self):
        hp_a = self.__robot_a.get_health()
        hp_b = self.__robot_b.get_health() 
        if hp_a == 0:
            self.__winner = self.__robot_b.get_name()
        elif hp_b == 0:
            self.__winner = self.__robot_a.get_name()
        elif hp_a == 0:
            self.__draw = True

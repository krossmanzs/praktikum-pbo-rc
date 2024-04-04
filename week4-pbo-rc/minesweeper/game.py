import random

class Status:
    READY = "ready"
    RUNNING = "running"
    TERMINATED = "terminated"

class Minesweeper:
    def __init__(self):
        print("Initialising the game...")
        self.__setup_area()
        print("Game created successfully, ready to start..")
        
        
    def start(self):
        if self.__status == Status.READY:
            print("~~~ MINESWEEPER GAME BY LEENOOGS ~~~")
            self.__status = Status.RUNNING
            self.__run()
        
    def __run(self):
        while self.__status == Status.RUNNING:
            self.__print_area()
            
            row = int(input("\nEnter Row (0-2): "))
            col = int(input("Enter Column (0-2): "))
            
            while f"{row},{col}" in self.__selected:
                print(f"row {row} column {col} already selected!")
                row = int(input("\nEnter Row (0-2): "))
                col = int(input("Enter Column (0-2): "))
                
            while row > 2 or col > 2:
                print(f"row {row} column {col} index out of bound!")
                row = int(input("\nEnter Row (0-2): "))
                col = int(input("Enter Column (0-2): "))
            
            self.__selected.add(f"{row},{col}")
            
            if row == self.__bomb_i and col == self.__bomb_j:
                print("Yikes, you found a bomb. The end :(\n")
                self.__status = Status.TERMINATED
                self.__win = False
            else:
                print("Well, there's no bomb here. Congrats!\n")

                if len(self.__selected) == 8:
                    self.__status = Status.TERMINATED
                    self.__win = True
                
        if self.__win:
            print("You win the game, yiiihawwww!!!")
        else:
            print("You lose the game, saddddgee :(((")
            
        self.__print_area()
        
            
    def __setup_area(self):
        self.__bomb_i = random.randrange(0,2)
        self.__bomb_j = random.randrange(0,2)
        self.__status = Status.READY
        self.__selected = set()
        self.__win = False
        
    def __print_area(self):
        print(f"{'=' * 30}")
        
        for i in range(3):
            for j in range(3):
                if f"{i},{j}" in self.__selected:
                    if i == self.__bomb_i and j == self.__bomb_j and self.__status == Status.TERMINATED:
                        print("X ",end='')
                    else:
                        print("O ",end='')
                else:
                    print("? ",end='')
            print()       
        
        print(f"{'=' * 30}")
        
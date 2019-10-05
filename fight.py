import random
from player import Player
from warrior import Warrior
from bard import Bard

class Fight():

    def __init__(self):
        self.bard = Bard()
        self.player = None
        self.opponent = None

    def print_hello(self, warriors_types):
        self.bard.warriors_info(warriors_types)

    def choose_warrior(self, warriors):
        my_warrior_num = int(input("Please select warrior: 1 - strong, 2 - healthy, 3 - skill = "))
        self.player = warriors[my_warrior_num-1]
        print("You have choosen {}".format(self.player.name))

    def choose_random_warrior(self, warriors):
        self.opponent = warriors[random.randint(1, 3)]
        print("Your opponent choosen {}".format(self.opponent.name))

    def select_hit(self):
        hit = int(input("Please select kick: 1 - to head, 2 - to body, 3 - to foot = "))
        return hit

    def select_block(self):
        block = int(input("Please select block: 1 - to head, 2 - to body, 3 - to foot = "))
        return block

    def select_random_hit(self):
        op_hit = random.randint(1, 3)
        return op_hit

    def select_random_blocl(self):
        op_block = random.randint(1, 3)
        return op_block

    def battle(self):
        my_hit = self.select_hit()
        my_block = self.select_block()
        opponents_hit = self.select_random_hit()
        opponents_block = self.select_random_blocl()

        while my_hit!=opponents_block:
            print(type(self.opponent))
            self.opponent.health -= self.player.skill*self.player.power
            print(self.opponent.health)


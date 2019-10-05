from fight import Fight
from warrior import Warrior

class Game():

    power_warrior = Warrior("Power man", 15, 1.0, 100)
    healthy_warrior = Warrior("Healthy man", 10, 1.0, 150)
    skill_warrior = Warrior("Skill man", 10, 1.5, 100)

    warriors = [power_warrior, healthy_warrior, skill_warrior]

    fight = Fight()

    fight.print_hello(warriors)
    fight.choose_warrior(warriors)
    fight.battle()

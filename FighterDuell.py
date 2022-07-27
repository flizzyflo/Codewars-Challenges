
class Fighter:
    def __init__(self, name: str, health: int, damage_per_attack: int) -> None:
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        self.isAlive = True

    def get_name(self) -> str:
        return self.name

    def get_health(self) -> int:
        return self.health

    def attack_opponent(self, opponent: object) -> None:
        opponent.health -= self.damage_per_attack
        if opponent.health <= 0:
            opponent.set_alive(False)
    
    def get_isAlive(self) -> bool:
        return self.isAlive

    def set_isAlive(self, isAlive: bool) -> None:
        self.isAlive = isAlive

    def print_stats(starter: object, second: object) -> None:
        print(f"{starter.get_name()} hp: {starter.get_health()}, {second.get_name()} hp: {second.get_health()}")


def declare_first_attacker(fighter_1: object, fighter_2: object, first_attacker: str):
    if fighter_1.get_name() == first_attacker:
        first_attacker = fighter_1
        second_attacker = fighter_2

    else:
        first_attacker = fighter_2
        second_attacker = fighter_1

    return first_attacker, second_attacker


def declare_winner(fighter1: object, fighter2: object, first_attacker: str) -> None:
    
    first_attacker, second_attacker = declare_first_attacker(fighter1, fighter2, first_attacker)


    while first_attacker.get_alive() == True and second_attacker.get_alive() == True:
        
        Fighter.print_stats(first_attacker, second_attacker)
        
        first_attacker.attack_opponent(second_attacker)

        if first_attacker.get_alive() == False:
            break

        second_attacker.attack_opponent(first_attacker)

        if second_attacker.get_alive() == False:
            break
    
    Fighter.print_stats(first_attacker, second_attacker)

    if first_attacker.get_alive() == True:
        return first_attacker.get_name()

    else:
        return second_attacker.get_name()


figher_1 = Fighter(name= "kiss me", health= 6, damage_per_attack= 2)
fighter_2 = Fighter(name= "be mine", health= 9, damage_per_attack= 1)
starting_fighther: str = "be mine"

print(f"The winner is: {declare_winner(figher_1, fighter_2, starting_fighther)}")

from enum import Enum

class warriorRank(Enum):
    Pushover= 1
    Novice= 2
    Fighter= 3
    Warrior= 4
    Veteran= 5
    Sage= 6
    Elite= 7
    Conqueror= 8
    Champion= 9
    Master= 10
    Greatest= 11

class Warrior():
    
    def __init__(self) -> None:
        self.level: int = 1
        self.rank_counter = 1
        self.rank: str = warriorRank(self.rank_counter).name
        self.experience = 100
        self.achievements = []

        self.MAX_EXPERIENCE = 10000
        self.MAX_LEVEL = self.MAX_EXPERIENCE // 100
        
    def manage_experience_and_rank(self, experience: int) -> None:
        
        """Manages the whole experience and rank calculation"""

        if self.experience + experience >= self.MAX_EXPERIENCE:
            self.experience = self.MAX_EXPERIENCE
            self.level = self.MAX_LEVEL
            self.set_rank_counter()
            self.set_rank()
        else:
            self.experience += experience
            if self.validate_level(self.level):
                self.set_level()
            self.set_rank_counter()
            self.set_rank()
        
    def set_achievement(self, achievement: str) -> None:

        """Tracks the training achievements"""

        self.achievements.append(achievement)
        
    def set_level(self) -> None:

        """Calculates and sets the current level of the warrior"""

        self.level = self.experience // 100
    
    def calculate_rank(self, level: int) -> int:

        """Calculates the current rank of the warrior based on his level"""

        if self.validate_level(level):
            return level // 10 + 1
        return 11

    def set_rank_counter(self) -> None:

        """Sets the rank counter based on the current level of the warrior"""

        self.rank_counter = self.calculate_rank(self.level)
    
    def set_rank(self) -> None:

        """Sets the current rank of the warrior based on rank counter and rank enum"""

        self.rank = warriorRank(self.rank_counter).name
        
    def calculate_battle_experience(self, opponent_level: int) -> int:
        
        """Calculates the whole experience gained from battles based on the level difference between both warriors"""

        if self.level == opponent_level:
            self.manage_experience_and_rank(10)
            
        elif self.level - 1 == opponent_level:
            self.manage_experience_and_rank(5)

        elif self.level - 2 >= opponent_level:
            self.manage_experience_and_rank(0)
            
        else:
            level_diff = opponent_level - self.level

            self.manage_experience_and_rank(20 * level_diff * level_diff)

    def check_defeat(self, opponent_level: int) -> bool:
        
        """Function to evaluate if fighter can compete with opponent or 
        if opponent is to strong"""
        
        return (self.level <= opponent_level - 5) and (warriorRank(self.rank_counter).value < self.calculate_rank(opponent_level))

    def comment_fight(self, opponent_level: int) -> str:

        """Function to manage fight commenting after succesful fight"""

        if self.level >= opponent_level + 2:
            return "Easy fight"
        elif self.level >= opponent_level:
            return "A good fight"
        else:
            return "An intense fight"

    def validate_level(self, level: int) -> bool:
        
        """Validates the current level"""
        
        return 0 < level <= self.MAX_LEVEL

    def training(self, training_data: list[str, int, int]) -> str:
        
        """Function to manage the training abilities of a fighter"""

        description, experience, minumum_level = training_data

        if self.level >= minumum_level:
            self.set_achievement(description)
            self.manage_experience_and_rank(experience)
            return description
        
        else:
            return "Not strong enough"

    def battle(self, opponent_level: int) -> str:
        
        """Manages the battle of two warriors inclusive experience management etc."""

        if not self.validate_level(opponent_level):
            return "Invalid level"

        elif self.check_defeat(opponent_level):
            return "You've been defeated"
        
        else:
            fight_comment = self.comment_fight(opponent_level)
            self.calculate_battle_experience(opponent_level)
            return fight_comment


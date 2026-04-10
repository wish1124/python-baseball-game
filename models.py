from dataclasses import dataclass
from enum import Enum
from utils import generate_random_numbers
from validators import validate_numbers


# ------- GameResult -------

class GameResultStatus(Enum):
    HOMERUN = "homerun"
    NOTHING = "nothing"
    HIT = "hit"


@dataclass
class GameResult:
    strikes: int
    balls: int

    @property
    def status(self) -> GameResultStatus:
        if self.strikes == 3:
            return GameResultStatus.HOMERUN
        if self.strikes == 0 and self.balls == 0:
            return GameResultStatus.NOTHING
        return GameResultStatus.HIT

    def is_homerun(self) -> bool:
        return self.status == GameResultStatus.HOMERUN

    def is_nothing(self) -> bool:
        return self.status == GameResultStatus.NOTHING


# ------- Computer -------

@dataclass
class Computer:
    numbers: list[int]

    @staticmethod
    def generate() -> "Computer":
        return Computer(numbers=generate_random_numbers())


# ------- Player -------

@dataclass
class Player:
    numbers: list[int]

    @classmethod
    def from_input(cls, raw: str) -> "Player":
        numbers = validate_numbers(raw)
        return cls(numbers=numbers)


# ------- Referee -------

class Referee:
    @staticmethod
    def judge(computer: Computer, player: Player) -> GameResult:
        strikes = sum(c == p for c, p in zip(computer.numbers, player.numbers))
        balls = sum(p in computer.numbers for p in player.numbers) - strikes
        return GameResult(strikes=strikes, balls=balls)

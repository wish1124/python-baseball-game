from dataclasses import dataclass
from enum import Enum


class GameStatus(Enum):
    PLAYING = "playing"
    HOMERUN = "homerun"


@dataclass
class Computer:
    numbers: list[int]

    @staticmethod
    def generate() -> "Computer":
        pass


@dataclass
class Player:
    numbers: list[int]

    @classmethod
    def from_input(cls, raw: str) -> "Player":
        pass


@dataclass
class GameResult:
    strikes: int
    balls: int

    def is_homerun(self) -> bool:
        pass

    def is_nothing(self) -> bool:
        pass


class Referee:
    @staticmethod
    def judge(computer: Computer, player: Player) -> GameResult:
        pass

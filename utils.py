import random


def generate_random_numbers(count: int = 3, min_val: int = 1, max_val: int = 9) -> list[int]:
    return random.sample(range(min_val, max_val + 1), count)

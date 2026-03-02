import re
from typing import Callable


def generator_numbers(text: str):
    # витягує числа з тексту
    pattern = r"\b(\d+\.?\d*)\b"
    for match in re.finditer(pattern, text):
        yield float(match.group(1))


def sum_profit(text: str, func: Callable) -> float:
    # сумує все що поверне func
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

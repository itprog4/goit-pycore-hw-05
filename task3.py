import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'(?<!\S)\d+\.\d+(?!\S)'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))
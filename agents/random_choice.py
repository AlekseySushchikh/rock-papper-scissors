import random

def random_choice(observation, configuration):
    """
    Стратегия, которая случайным образом выбирает один из возможных ходов.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    return random.choice([0, 1, 2])

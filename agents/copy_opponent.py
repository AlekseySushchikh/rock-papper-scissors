import random

def copy_opponent(observation, configuration):
    """
    Стратегия, которая копирует последний ход противника.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    if observation.step > 0:
        return observation.lastOpponentAction  # Копируем последний ход противника
    else:
        return random.choice([0, 1, 2])  # Случайный выбор на первом шаге

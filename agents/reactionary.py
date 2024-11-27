import random

def reactionary(observation, configuration):
    """
    Стратегия, которая выбирает ход, который побеждает ход противника.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    if observation.step > 0:
        # Побеждает тот, кто выбрал то, что побеждает ход противника
        return (observation.lastOpponentAction + 1) % 3
    else:
        return random.choice([0, 1, 2])  # Случайный выбор на первом шаге

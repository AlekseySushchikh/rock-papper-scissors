import random

def counter_reactionary(observation, configuration):
    """
    Стратегия, которая контрит стратегию reactionary.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    if observation.step > 0:
        # Контрит стратегию reactionary
        return (observation.lastOpponentAction + 2) % 3
    else:
        return random.choice([0, 1, 2])  # Случайный выбор на первом шаге

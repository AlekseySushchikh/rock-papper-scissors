def delayed_reaction(observation, configuration):
    """
    Агент, который реагирует на ход противника с задержкой. На первом шаге выбирает 'Камень'.
    На последующих шагах повторяет ход противника с задержкой.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    if observation.step == 0:
        return 0  # Камень на первом шаге
    return observation.lastOpponentAction  # Повторяет ход противника с задержкой
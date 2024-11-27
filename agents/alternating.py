def alternating(observation, configuration):
    """
    Стратегия, которая поочередно выбирает ходы: камень, бумага, ножницы.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    return observation.step % 3

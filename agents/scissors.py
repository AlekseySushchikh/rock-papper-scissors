def scissors(observation, configuration):
    """
    Стратегия, которая всегда выбирает ножницы.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (2 для ножниц).
    """
    return 2  # 2 - ножницы

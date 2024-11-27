def rock(observation, configuration):
    """
    Стратегия, которая всегда выбирает камень.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня).
    """
    return 0  # 0 - камень
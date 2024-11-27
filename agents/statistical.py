import random
from collections import Counter

def statistical(observation, configuration):
    """
    Стратегия, которая выбирает ход, который побеждает наиболее частый ход противника.

    Аргументы:
    observation (object) -- объект, содержащий информацию о предыдущих шагах игры.
    configuration (object) -- объект с настройками игры.

    Возвращает:
    int -- выбор хода (0 для камня, 1 для бумаги, 2 для ножниц).
    """
    # Сохраняем информацию о предыдущих ходах противника в своем списке
    if not hasattr(observation, 'opponent_history'):
        observation.opponent_history = []

    # Добавляем последний ход противника в историю
    if observation.step > 0:  # Игрок уже сделал хотя бы один ход
        observation.opponent_history.append(observation.lastOpponentAction)

    # Подсчитываем частоту каждого хода противника
    if observation.step > 0:  # Нужно хотя бы один ход сделать
        counter = Counter(observation.opponent_history)
        most_common_move = counter.most_common(1)[0][0]  # Получаем наиболее частый ход противника
        return (most_common_move + 1) % 3  # Побеждаем этот ход
    else:
        return random.choice([0, 1, 2])  # Случайный выбор на первом шаге

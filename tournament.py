from kaggle_environments import make
from agents.rock import rock
from agents.paper import paper
from agents.scissors import scissors
from agents.copy_opponent import copy_opponent
from agents.reactionary import reactionary
from agents.counter_reactionary import counter_reactionary
from agents.statistical import statistical
from agents.alternating import alternating
from agents.random_choice import random_choice
from agents.cycle_opponent import cycle_opponent
from agents.adaptive_response import adaptive_response
from agents.delayed_reaction import delayed_reaction

# Список агентов для турнира
AGENTS = [
    rock, paper, scissors, copy_opponent, reactionary, counter_reactionary,
    statistical, alternating, random_choice, cycle_opponent, adaptive_response,
    delayed_reaction
]


def run_tournament():
    """
    Функция для проведения турнира между всеми агентами.

    Для каждого возможного сочетания агентов будет проведена игра,
    и результат будет сохранен в виде матрицы результатов.

    Матрица результатов представляет собой словарь с ключами в виде кортежей
    (выбор_агента_1, выбор_агента_2), где каждый кортеж соответствует
    одному сыгранному матчу между агентами.
    """
    # Инициализация игры
    environment = make("rps", debug=True)  # Создаем среду для игры "Камень, ножницы, бумага"
    results = {}  # Словарь для хранения результатов игр

    # Проходим по всем возможным сочетаниям агентов
    for agent_1 in AGENTS:
        for agent_2 in AGENTS:
            print(f"Running game: {agent_1.__name__} vs {agent_2.__name__}")

            # Инициализируем состояние игры для каждого сочетания агентов
            environment.reset()

            # Запускаем игру
            result = environment.run([agent_1, agent_2])

            # Получаем итоговый результат из игры
            score = result[-1][0]['reward']  # Итоговые очки

            # Сохраняем результат игры в словарь
            results[(agent_1.__name__, agent_2.__name__)] = score

    # Выводим результаты турнира
    print("Tournament Results:")
    for (agent_1, agent_2), score in results.items():
        print(f"{agent_1} vs {agent_2}: {score}")


if __name__ == "__main__":
    # Запуск турнира
    results = run_tournament()
    print(results)

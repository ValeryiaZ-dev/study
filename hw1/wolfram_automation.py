"""
Формулировка задания: написать код для одномерного клеточного автомата (вольфрам). 
Клеточный автомат должен иметь следующие правила: 
1) живая клетка (черная) с 2 живыми соседями выживает;
2) мертвая клетка (белая) с 2 живыми соседями становится живой; 
3) в других случаях все живые (белые) клетки умирают, а мертвые остаются мертвыми.
Применить алгоритмы для увеличения производительности. 
"""

import numpy as np

def wolfram_automaton(initial_state, steps):
    # Создаем массив для хранения состояний клеток
    states = np.zeros((steps + 1, len(initial_state)), dtype=int)
    states[0] = initial_state

    # Применяем правила для каждого шага
    for step in range(1, steps + 1):
        for i in range(1, len(initial_state) - 1):
            # Получаем состояние соседей
            left_neighbor = states[step - 1, i - 1]
            right_neighbor = states[step - 1, i + 1]

            # Применяем правила
            if states[step - 1, i] == 1 and left_neighbor + right_neighbor == 2:
                states[step, i] = 1
            elif states[step - 1, i] == 0 and left_neighbor + right_neighbor == 2:
                states[step, i] = 1
            else:
                states[step, i] = 0

    return states

# Пример использования
initial_state = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
steps = 10
states = wolfram_automaton(initial_state, steps)
print(states)

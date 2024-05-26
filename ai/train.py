import numpy as np
from defs import softmax
import defs
import time

# Определение функции для тренировки нейронной сети
def train_neural_network(inputs, targets, num_epochs):
    num_inputs = len(inputs[0])
    num_classes = 2   # Количество классов: 0 и 1

    # Генерация случайных весов
    weights = np.random.randn(num_inputs, num_classes)

    start = time.time()
    for epoch in range(num_epochs):
        for input_data, target in zip(inputs, targets):
            # Прямое распространение
            output_activation = softmax(np.dot(input_data, weights))

            # Обновление весов
            output_error = target - output_activation
            weights += np.dot(np.array([input_data]).T, output_error.reshape(1, -1))
        end = time.time()
        try: print(f'{epoch} | {np.round(end - start, 1)} s | {np.round(((end - start) / epoch * num_epochs / 60) - ((end-start)/60), 1)} m')
        except: pass

    return weights

# Пример обучающих данных
inputs = defs.inputs

# Оценка для каждого примера (0 или 1)
targets = defs.targets  # Кодирование классов one-hot

# Обучение нейронной сети
weights = train_neural_network(inputs, targets, num_epochs=10000)
np.save('weights.npy', weights)
import time
from framework.singletones import SingletonByName


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        with open(f'_logs_{self.name}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{text}\n')
        # print('logs: ', text)


def debug(function):
    def inner(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Функция: {function.__name__}, время выполнения: {end - start}')
        return result
    return inner

from framework.singletones import SingletonByName


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        with open(f'_logs_{self.name}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{text}\n')
        print('logs: ', text)

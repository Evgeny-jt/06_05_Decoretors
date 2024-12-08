import os
import datetime


def logger(old_function):
    # ...
    def new_function(*args, **kwargs):
        data_tame_start = datetime.datetime.now()

        result = old_function(*args, **kwargs)

        name = {old_function.__name__}

        if 'a' in kwargs:
            a = kwargs['a']
        else:
            a = None
        if 'b' in kwargs:
            b = kwargs['b']
        else:
            b = None

        if locals()['args'] == () and locals()['kwargs'] == {}:
            function_value_str = result
        elif a != None and b != None:
            function_value_str = str(result)
        elif a == None and b == None:
            a = float(args[0])
            b = float(args[1])
            function_value_str = str(result)
        elif a == None:
            a = float(args[0])
            function_value_str = result
        elif b == None:
            b = float(args[0])
            function_value_str = str(result)
        log_text = (str(data_tame_start) + ' ' + str(name) + ' ' +
                    'аргументы: ' + str(a) + ' ' + str(b) + ' ' + 'значение функции: ' + str(function_value_str) + '\n')
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(log_text)

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        print("путь существует")
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

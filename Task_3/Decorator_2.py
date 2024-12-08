import os
import datetime


def logger(path):
    if os.path.exists(path):
        os.remove(path)
    data_tame_start = datetime.datetime.now()

    def __logger(old_function):
        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)

            name = {old_function.__name__}

            if locals()['args'] == () and locals()['kwargs'] == {}:
                function_value_str = result
            else:
                log_text = (str(data_tame_start) + ' запущенная функция: ' + str(name) + ' ' +
                        'аргументы: ' + str(args) + ' значение функции: ' + str(
                        result) + ' путь к файлу: ' + path + '\n')
            with open(path, 'a', encoding='utf-8') as f:
                f.write(log_text)

            return result

        return new_function

    return __logger




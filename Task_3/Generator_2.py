import types
from Decorator_2 import logger

@logger('log_1.log')
def flat_generator(list_of_list):
    items = attachment(list_of_list, [])
    print(items)
    for item in items:
        yield (item)


@logger('log_1.log')
def attachment(attachment_list, items):  # перебираем элементы
    for item in attachment_list:
        items = item_list(item, items)
    return items

@logger('log_1.log')
def item_list(item, items):  # проверяем из чего состоит элемент
    if isinstance(item, list):
        attachment(item, items)
    else:
        items = item_save(item, items)

    return items


@logger('log.log')
def item_save(item, items):  # сохраняем найденный элемент
    items.append(item)
    return items


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    #
    # assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    #
    # assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

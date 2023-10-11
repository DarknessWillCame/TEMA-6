import collections

def create_dict(value):
    dictionary = {}
    for x in value:
        number = int(x)
        if number in dictionary: dictionary[number] = dictionary[number] + 1
        else: dictionary[number] = 1
    dictionary_to_list = list(dictionary.items())
    dictionary_to_list.sort(reverse=True, key=lambda x: x[1])

    first_three_often_values = dictionary_to_list[0:3]
    first_three_often_values.sort(key=lambda x: x[0])

    return collections.OrderedDict(first_three_often_values)

result = create_dict(input('Введите последовательность числе: '))

for x in result.items():
    print(f'Число {x[0]} встретилось {x[1]} раз(а)')

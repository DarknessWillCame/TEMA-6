example_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
example_2 = (12, 4, 901, 243678, 123, 111, 945)
example_3 = (78, 90, 23, 45, 67, 89, 80)

def get_even_numbers(values):
    new_list = []

    for x in list(values):
        if x % 2 == 0: new_list.append(x)

    return tuple(new_list)

print('Пример 1:', get_even_numbers(example_1))
print('Пример 2:', get_even_numbers(example_2))
print('Пример 3:', get_even_numbers(example_3))

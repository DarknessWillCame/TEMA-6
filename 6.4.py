example_1 = ((1, 2, 3), 8)
example_2 = ((1, 8, 3, 4, 8, 8, 9, 2), 8)
example_3 = ((1, 2, 8, 5, 1, 2, 9), 8)

def get_employee_order(value):
    source_order, id = value
    was_first_check = False

    new_list = []
    for x in list(source_order):
        if x == id and was_first_check:
            new_list.append(x)
            break

        if x == id: was_first_check = True

        if was_first_check:
            new_list.append(x)

    return tuple(new_list)

print('Пример 1:', get_employee_order(example_1))
print('Пример 2:', get_employee_order(example_2))
print('Пример 3:', get_employee_order(example_3))

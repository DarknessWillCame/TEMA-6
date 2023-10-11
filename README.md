Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):

Черезов Роман Алексеевич
ЗПИЭ-20-1
Задание	Сам_раб
Задание 1	+
Задание 2	+
Задание 3	+
Задание 4	+
Задание 5	+
знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:

к.э.н., доцент Панов М.А.
Самостоятельная работа №1
При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.
value = input('Введите последовательность чисел: ')

processed_value = value.split(' ')

print('Список:', list(processed_value))
print('Кортеж:', tuple(processed_value))
Результат.
Результат задания 1

Выводы
Я выяснил, что при помощи функции split() можно получить список. Затем из этого списка можно будет создать новый список и кортеж

Самостоятельная работа №2
Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).
example_1 = ((1, 2, 3), 1)
example_2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
example_3 = ((2, 4, 6, 6, 4, 2), 9)

def remove_element_from_tuple(value):
    source_tuple, element = value

    new_list = []
    was_removed = False
    for x in list(source_tuple):
        if x == element and was_removed == False:
            was_removed = True
            continue
        new_list.append(x)

    return tuple(new_list)

print('Пример 1:', remove_element_from_tuple((example_1)))
print('Пример 2:', remove_element_from_tuple((example_2)))
print('Пример 3:', remove_element_from_tuple((example_3)))
Результат.
Результат задания 2

Выводы
Я узнал, что для того, чтобы убрать из кортежа элемент, можно преобразовать кортеж в список, пробежаться по нему, создать новый список и уже новый список преобразовать в кортеж

Самостоятельная работа №3
Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайтеМихаил А. Панов функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.
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
Результат.
Результат задания 3

Выводы
Сначала из введённой строки создаю словарь
Затем словарь конвертирую в список, чтобы можно было отсортировать по самым частовведённым числам
Затем из отсортированного списка беру первые три значения
Эти три значения сортирую по ключу
Создаю из списка упорядоченный словарь
Самостоятельная работа №4
Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
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
Результат.
Результат задания 4

Выводы
Для решение данной задачи я преобразовал кортеж к списку, затем проитеррировался по нему и записал все необходимые значения, а затем новый список преобразовал к кортежу

Самостоятельная работа №5
Напишите функцию, которой на вход подаётся кортеж из чисел. Функция должна вернуть кортеж только с чётными числами
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
Результат.
Результат задания 5

Выводы
Преобразовываю кортеж списку, итеррируюсь по нему и проверяю значение на чётность. Формирую новый список, который затем преобразовываю в кортеж

Общие выводы по теме
При выполнении задания я выяснил, что Python имеет мощный функционал в виде списков и кортежей

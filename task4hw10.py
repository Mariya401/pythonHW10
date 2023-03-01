"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
bytes = []

for word in words:
    bytes_num = word.encode('utf-8')
    print(bytes_num)
    bytes.append(bytes_num)

for word in bytes:
    print(word.decode('utf-8'))

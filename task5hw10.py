"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for el in args:
    ping = subprocess.Popen(el, stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)


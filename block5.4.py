# myclient.py (с использованием from)
from mymod import countLines, countChars, test

test("mymod.py")  # Доступна напрямую

# myclient.py (с использованием import)
import mymod

mymod.test("mymod.py") # Нужен префикс mymod

# Тестирование (в интерактивном сеансе):
# import myclient
# или
# from myclient import *
# myclient.__dict__ # покажет, что находится в пространстве имен модуля myclient

#Выведите список файлов в указанной директории.
import os
# Указываем путь к директории
directory = input()
# Получаем список файлов
files = os.listdir(directory)
# Выводим список файлов
print(files)
# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)



# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)


# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written) # 6
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)

# fh.close()


# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()

# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)

# fh.close()



# fh = open('test.txt', 'w+')
# fh.write('hello!')

# fh.seek(1)
# second = fh.read(1)
# print(second)  # 'e'

# fh.close()


# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell()
# print(position)  # 6

# fh.seek(1)
# position = fh.tell()
# print(position)  # 1

# fh.read(2)
# position = fh.tell()
# print(position)  # 3

# fh.close()



# fh = open('text.txt', 'w')
# try:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# finally:
#     # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
#     fh.close()



# with open('text.txt', 'w') as fh:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# # Файл автоматично закриється після виходу з блоку with




# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)



# with open("example.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("example.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)



# # Відкриття текстового файлу з явними вказівками UTF-8 кодування
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)



# byte_array = bytearray(b'Kill Bill')
# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array)


# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# print(byte_array)


# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'



# string1 = "Hello World"
# string2 = "hello world"
# if string1.lower() == string2.lower():
#     print("Рядки однакові")
# else:
#     print("Рядки різні")



# text = "Python Programming"
# print(text.casefold())




# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")


# import os

# print("Текущая директория:", os.getcwd())  # Покажет, где сейчас работает скрипт
# print("Содержимое директории:", os.listdir())  # Покажет файлы и папки



# import shutil

# # Створення ZIP-архіву з вмістом директорії 'Study_repo'
# # shutil.make_archive('example', 'zip', root_dir='Study_repo')
# shutil.make_archive('example', 'zip', root_dir=r'C:\Users\Yuriy\Documents\Python\Probe\Study_repo')

# import shutil
# import os

# # Папка, куда будет распакован архив
# destination_folder = "Archive"

# # Создаем папку, если её нет
# os.makedirs(destination_folder, exist_ok=True)

# # Распаковываем архив
# shutil.unpack_archive("example.zip", destination_folder)

# print(f"Архив успешно распакован в {destination_folder}")



# from pathlib import PurePath

# p = PurePath("/usr/bin/simple.jpg")
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)


# from pathlib import Path

# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 



# # Відкриття текстового файлу з явними вказівками UTF-8 кодування
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)



# with open("example.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("example.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)



# import math

# sin_pi = math.sin(math.pi)
# print(sin_pi)


# from math import pi, sin

# sin_pi = sin(pi)
# print(sin_pi)

# # mymodule.py
# def say_hello(name):
#     return f"Hello, {name}!"

# # main.py
# import mymodule

# print(mymodule.say_hello("World"))


# # main.py
# from mymodule import say_hello

# print(say_hello("World"))


# # main.py
# from mymodule import say_hello as greeting

# print(greeting("World"))



# # main.py
# from mymodule import say_hello as greeting

# print(dir())
# print(greeting("World"))



# # main.py
# from mymodule import say_hello as greeting

# print(greeting("World"))


# import sys
# import os

# print(sys.modules["os"])

# import sys
# import os

# print(sys.modules.keys())


# import sys

# for arg in sys.argv:
#     print(arg)

# python echo.py test --user -hello some text 


# import sys

# def main():
#     if len(sys.argv) > 1:
#         print(sys.argv[1])

# if __name__ == "__main__":
#     main()

# python arg.py 123


# import random
# import pathlib

# current_dir = pathlib.Path(__file__).parent

# def get_random_joke():
#     try:
#         with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
#             jokes = file.readlines()
#             return random.choice(jokes).strip()
#     except FileNotFoundError:
#         return "Не вдалося знайти файл з анекдотами."


# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(27))
# print(is_even(12))


# def is_even(number: int) -> bool:
#     return number % 2 == 0
# print(is_even(27))
# print(is_even(12))


# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     length = len(s)
#     for i in range(length // 2):
#         if s[i] != s[length - i - 1]:
#             return False
#     return True

# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True



# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     return s == s[::-1]

# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True


# # Розрахунок площі 
# length1, width1 = 5, 10
# area1 = length1 * width1

# # Багато різного коду
# length2, width2 = 7, 12
# area2 = length2 * width2

# print(area1)
# print(area2)


# def calculate_area(length: float, width: float) -> float:
#     return length * width

# area1 = calculate_area(5, 10)
# area2 = calculate_area(7, 12)
# print(area1)
# print(area2)


# from math_operations import calculate_area

# area1 = calculate_area(10, 5)
# area2 = calculate_area(20, 15)
# print(area1)
# print(area2)





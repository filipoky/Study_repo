# from datetime import datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

# converted_date = string_to_date(date_string)
# print(converted_date)



# from datetime import datetime

# date_string = "2023.03.14"

# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу




# from datetime import datetime


# def string_to_date(date_string):
    
#     converted_date = datetime.strptime(date_string, "%Y.%m.%d")
#     print(converted_date)

# string_to_date("2024.01.01")

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)
# date_string = date_to_string(converted_date)
# print(date_string)




# from datetime import datetime    

# def string_to_date(date_string):
#     converted_date = datetime.strptime(date_string, "%Y.%m.%d").date()
#     return converted_date  

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# date_string = date_to_string(converted_date)
# print(date_string)




# from datetime import datetime

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def prepare_user_list(user_data):
#     return [{"name": user["name"], "birthday": string_to_date(user["birthday"])} for user in user_data]

# # Входные данные
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# # Обработка данных
# prepared_users = prepare_user_list(users)

# # Вывод результата
# print(prepared_users)



# from datetime import datetime, timedelta

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def find_next_weekday(start_date, weekday = 0):
#     current_weekday = start_date.weekday()  # Определяем день недели для start_date
#     days_ahead = (weekday - current_weekday) % 7  # Вычисляем разницу
#     if days_ahead == 0:
#         days_ahead = 7  # Если день недели совпадает, берем следующий такой же
#     return start_date + timedelta(days = days_ahead)  # Прибавляем дни и возвращаем дату

# # Пример использования
# start_date = string_to_date("2024.03.26")
# next_monday = find_next_weekday(start_date, 0)  # Следующий понедельник
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4)  # Следующая пятница
# print(next_friday)

# next_sunday = find_next_weekday(start_date, 6)
# print(next_sunday)
# next_tuesday = find_next_weekday(start_date, 1)
# print(next_tuesday)




# from datetime import datetime, date

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])} )
#     return prepared_list

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
    
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year = today.year)
#         days_difference = (birthday_this_year - today).days
        
#         if 0 <= days_difference <= days:
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": date_to_string(birthday_this_year)
#             })
    
#     return upcoming_birthdays

# # Пример использования
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]

# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users, 7))



# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days = days_ahead)

# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:  # 5 - суббота, 6 - воскресенье
#         return find_next_weekday(birthday, 0)  # Следующий понедельник
#     return birthday  # Если будний день, возвращаем без изменений

# from datetime import datetime

# # Преобразуем строки в даты
# b1 = string_to_date("2024.03.30")  # Суббота
# b2 = string_to_date("2024.03.31")  # Воскресенье
# b3 = string_to_date("2024.04.01")  # Понедельник

# # Проверяем корректировку дат
# print(adjust_for_weekend(b1))  # 2024-04-01 (перенесено на понедельник)
# print(adjust_for_weekend(b2))  # 2024-04-01 (перенесено на понедельник)
# print(adjust_for_weekend(b3))  # 2024-04-01 (без изменений)



from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days = days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # 5 - суббота, 6 - воскресенье
        return find_next_weekday(birthday, 0)  # Следующий понедельник
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        congratulation_date = adjust_for_weekend(birthday_this_year)

        if 0 <= (congratulation_date - today).days <= days:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays




# Тестовые данные
users = [
    {"name": "Bill Gates", "birthday": "1955.03.25"},
    {"name": "Steve Jobs", "birthday": "1955.03.21"},
    {"name": "Jinny Lee", "birthday": "1956.03.22"},
    {"name": "Sarah Lee", "birthday": "1957.03.23"},
    {"name": "Jonny Lee", "birthday": "1958.03.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

prepared_users = prepare_user_list(users)
print(get_upcoming_birthdays(prepared_users, 7))



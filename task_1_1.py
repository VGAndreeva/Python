# задание 1.
# a), b), c), d)*
user_number = int(input('duration = '))
day = user_number // 86400
hour = (user_number - (day * 86400)) // 3600
min = (user_number - ((day * 86400) + (hour * 3600))) // 60
sec = user_number - ((day * 86400) + (hour * 3600) + (min * 60))
if 0 < user_number < 60:
    print(user_number, 'сек')
if 60 <= user_number < 3600:
    print(min, 'мин', sec, 'сек')
if 3600 <= user_number < 86400:
    print(hour, 'час', min, 'мин', sec, 'сек')
if 86400 <= user_number < 2678400:
    print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')
# хотела попробовать с циклом, но что-то пошло не так :)
# так что, оставлю в таком виде.
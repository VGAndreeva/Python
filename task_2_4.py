# задание 4
user_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
ls = user_list[0]
ls2 = user_list[1]
ls3 = user_list[2]
ls4 = user_list[3]
parts = ls.split()
parts2 = ls2.split()
parts3 = ls3.split()
parts4 = ls4.split()
ls = parts[1:]
ls2 = parts2[2:]
ls3 = parts3[3:]
ls4 = parts4[1:]
name, name2, name3, name4 = ls + ls2 + ls3 + ls4
hello = f'Привет, {name}!'
hello2 = f'Привет, {name2}!'
hello3 = f'Привет, {name3}!'
hello4 = f'Привет, {name4}!'
print(hello.title())
print(hello2.title())
print(hello3.title())
print(hello4.title())
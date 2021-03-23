# задание 3.
proc = ['процент', 'процента', 'процентов']
num = int(input('Введите число: '))
if 0 < num < 2:
    print(proc[0])
if 2 <= num < 5:
    print(proc[1])
if 5 <= num < 21:
    print(num, proc[2])
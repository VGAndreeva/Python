# задание 2
user_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
user_list[1] = '"05"'
user_list[3] = '"17"'
user_list[8] = '"+05"'
user_ls = ' '.join(user_list)
print(user_ls)
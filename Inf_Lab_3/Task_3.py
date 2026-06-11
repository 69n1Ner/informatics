from re import *
#fst_2nd_3rd_4th = r'^(?=.*[A-Z])(?=.*\d)\S{5,}$'
#pswd=input("Введите пароль: ")

pass_list=['asd', 'Asd', 'asdasd','ASDasd','ASDasd0','ASDasd0,','ASDasd0 ,', 'ASdasd0,25july','ASdasd.12@13may']

#while True:
for pswd in pass_list:
    flag=True
    months = r'january|february|march|april|may|june|july|august|september|october|november|december'
    count_times_reg = r'^.{5,}$'
    uppercase_reg = r'[A-Z]+'
    dig_reg = r'\d+'
    symbol_reg = r'[^\w\\]'
    print(pswd)
    lst=(lambda x: (not findall(symbol_reg, x) or ' ' in findall(symbol_reg, x)),
         lambda x: x)

    for q in lst:
        if q(pswd):
            pass

    if not search(count_times_reg, pswd):
        print("Минимальная длина пароля 5 символов")
        flag=False
    if not search(uppercase_reg, pswd):
        print("Нет заглавных букв")
        flag = False
    if not search(dig_reg, pswd):
        print("Нет цифр")
        flag = False
    #полезное
    if findall(symbol_reg, pswd) and ' ' == findall(symbol_reg, pswd)[-1]:
        ind=pswd.index(' ')
        pswd=pswd[:ind]

    if not findall(symbol_reg, pswd) or ' ' in findall(symbol_reg, pswd):
        print("Нет спец символов или присутствует пробел")
        flag = False
    if sum(map(int, findall(dig_reg, pswd))) != 25:
        print("Сумма чисел не 25")
        flag = False
    if not search(months, pswd, I):
        print("Нет месяца")
        flag = False
    if flag:
        if pswd == pass_list[-1]:
            print("Доступ разрешен")
            break
        else:
            print("Доступ разрешен")
            continue
    # else:
    #     pswd=input("Введите пароль: ")



def f_n_machine(tmp):
    fib_nums=[1,2]+[0]*tmp
    for i in range(2,len(fib_nums)):
        fib_nums[i]=fib_nums[i-2]+fib_nums[i-1]
    return fib_nums[::-1]

fibs=f_n_machine(3)
def fcc_machine(x):
    ost=0
    ans=[]
    n=x
    for f in fibs:
        if n>=f:
            ans.append('1')
            n-=f
        else:
            ans.append('0')
    return ''.join(ans)

x=int(input("Введите число в десятичной сс: "))
calc=fcc_machine(x)
while '11' in calc:
    fibs = f_n_machine(len(fibs) + 5)
    calc=fcc_machine(x)
print('Число в сс Фибоначчи: ',int(calc))


def f_n_machine(tmp):
    fib_nums=[1,1]+[0]*(tmp-1)
    for i in range(2,len(fib_nums)):
        fib_nums[i]=fib_nums[i-2]+fib_nums[i-1]
    return fib_nums[::-1]
x=int(input("Введите число в сс Фибоначчи: "))
sx=str(x)
fibs=f_n_machine(len(sx))
ans=0
for d in sx:
    if d=='1':
        ans+=fibs[sx.index(d)]
        sx=sx.replace('1','0',1)
print("Число в десятичной сс: ",ans)
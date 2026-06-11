from re import *
txt='корма корка корчма'
txt2="оКоРнАс КККоРиАндРоККоРоА%АААА слово"
reg=r'\w*(?:к[^кра]{1}р[^кра]{1}а)+\w*'
x=findall(reg,txt,I)
y=findall(reg,txt2,I)
print(x)
print(y)
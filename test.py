import math
maxlen=input('请输入要获取第几个的质数（大于2）：')
n=3 #除去小于5的质数1-2-3
x=4
def isPrime(num):
    if num%6!=1 and num%6!=5:
        return False
    sqprnum=math.sqrt(num)
    i=5
    while(i<=sqprnum):
        if num%i==0:
            return False
        elif num%(i+2)==0:
            return False
        else:
            i+=6
    return True
#该算法是以5开始的自然数以6的倍数为规律计算
while(n<int(maxlen)):
    x+=1
    if isPrime(x)==True:
        n+=1

print('第',n,'个质数')
print('质数是：',x)

maxlen=input('请输入要获取第几个的质数（大于2）：')
n=2
x=2
while(n<int(maxlen)):
    isnotnum=0
    x+=1
    print(n)
    for i in range(2,x):
        if x%i==0:
            isnotnum=1
            break
    if isnotnum==0:
        n+=1
print('第',n,'个质数')
print('质数是：',x)

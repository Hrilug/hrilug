import random

m=random.randint(1,100)
i=0
while True:
    n=int(input("输入0到100的数"))
    if n>m:
        print("猜大了")
    elif n<m:
        print("猜小了")
    elif n==m:
        print("猜对了")
        break    
    i+=1
    if i==5:
        print('你没有机会了哦')    
        break
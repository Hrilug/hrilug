def CalCircleAreea(r):
    s=3.14*r*r
    print("半径为%.2f的圆的面积为%.2f"%(r,s))
def CalRectArcea(a,b):
    s=a*b
    print("边长为%.2f和%.2f的长方形的面积为%.2f"%(a,b,s))

a=eval(input("请输入圆的半径："))
x=eval(input("请输入长方形的一条边长"))
y=eval(input("请输入长方形的另一条边长"))

CalCircleAreea(a)
CalRectArcea(x,y)
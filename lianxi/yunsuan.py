def add(n1,n2):
    value = n1+n2
    print('%d+%d=%d'%(n1,n2,value))

def mins(n1,n2):
    value=n1-n2
    print('%d-%d=%d'%(n1,n2,value))

def multiply(n1,n2):
    value=n1*n2
    print('%d*%d=%d' % (n1, n2, value))

def divide(n1,n2):
    try:
        n2!= 0
        value=n1/n2
        print('%d/%d=%d' % (n1, n2, value))
    except ZeroDivisionError as f:
        print('除数不能为0')
dict={1:add,2:mins,3:multiply,4:divide}
#operator= int(input('1 is + ,2 is - ,3 is * ,4 is / ，请输入1/2/3/4' ))

def get_op():
    operator = int(input('请输入1/2/3/4'))
    try:
        if operator not in [1,2,3,4,]:
            print('请输入正确的运算符')
            return get_op()
        else:
            return operator
    except ValueError as f:
        print('请输入正确的运算符')
        return get_op()

def get_num1():
    num1=input('请输入一个数')
    try:
        num1 =int(num1)
        return num1
    except ValueError as f:
        print('请输入一个整数')
        return get_num1()

def get_num2():
    num2=input('请输入一个数')
    try:
        num2 = int(num2)
        return num2
    except ValueError as f:
        print('请输入一个整数')
        return get_num2()
print('1 is + ,2 is - ,3 is * ,4 is /')
op= get_op()
j=get_num1()
k=get_num2()
dict[op](j,k)
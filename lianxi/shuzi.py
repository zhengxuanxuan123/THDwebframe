A= range(101)
for a in A:
    if a == 0:
        print(a)
    elif a%3 == 0:
        if a%5 ==0:
            print('FizzBizz',a)
        else:
            print('Fizz',a)
    elif a%5 == 0:
        print('Bizz',a)
    else:
        print(a)
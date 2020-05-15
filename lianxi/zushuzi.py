a=[]
for i in [1,2,3,4]:
    for c in [1,2,3,4]:
        for b in [1, 2, 3, 4]:
                k=i*100+c*10+b
                a.append(k)
print(a)

list = []
sum = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                num=i*100+j*10+k
                list.append(num)
                sum+=1
print(list)
print(sum)
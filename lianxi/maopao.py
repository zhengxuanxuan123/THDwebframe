shu=[12,45,7,6,465,7,45,64,56,56]
def get_xu():
    for i in range(len(shu)-1):
        for j in range(len(shu)-i-1):
            if shu[j] >shu[j+1]:
                shu[j+1],shu[j] = shu[j],shu[j+1]
    return shu
a =get_xu()
n=len(a)
print(a)
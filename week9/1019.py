a=list(range(1,100,3))
print(a)

b=list(range(100,-100,-2))
b.reverse
print(b)

c=list(range(100,-100,-2))
c.reverse
print(c)

a.extend(c)

d=2382
d=bin(d)
print(d)

e='10110111'
f=int(e,2) 
print(f)


a= []
#11에 append만 써야되 [1,2,3,[5,6,7],88,11,[2,4,[5,6,7]]]

a=[]
a.append(1)
a.append(2)
a.append(3)
a.append([5,6,7])
a.append(88)
a.append(11)
a.append([2,4,[5,6,7]])
print(a)
 
#[1,2,3,[5,7],88,[2,[5,7]]]
# del a[3][1]
# del a[5]
# del a[5][1]
# del a[5][1][2]

# print(a)

del a[3][1]
del a[5]
del a[5][1]
del a[5][1][2]

print (a)



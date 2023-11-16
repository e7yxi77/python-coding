# # d = {'data': 1, 'data2': 2, 'data3': [1, 2, 3, 4]}
# # a = list(reversed(d['data3']))
# # print(a)

# b={'li':[1,2,3,4,5]}
# c=b['li']
# c.extend([6,7,8,9,10])
# print(c)

# f =[1,2,3,4,5,6,7,8,9,10]
# f.insert(3,55)
# f.insert(9,22)
# print(f)

# c = set(c)
# f = set(f)
# print(c)
# print(f)

# print(c&f)

# d=[4,3,2,1,["1","2","3","4"],6,[-1 부터 -5까지]]]

# d={"li":[1,2,3,4,[1,2,3,4],5]}

# a=d["li"]
# a[0]=4
# a[1]=3
# a[2]=2
# a[3]=1

# a[4][0]=str(a[4][0])
# a[4][1]=str(a[4][1])
# a[4][2]=str(a[4][2])
# a[4][3]=str(a[4][3])

# a[5]=6

# a.append(list(range(-1,-6,-1)))
# print(a)


#d= {"li" :1, "wang" :2, "zhang" :3, "zhao" :4,"qian" :5, "sun":6, "liu" :7, "chen" :8, "yang" :9, "zhou" :10}
#x=d["chen"]+d["wang"]+d["zhang"]+d["zhao"]+d["qian"]+d["sun"]+d["liu"]+d["chen"]+d["yang"]+d["zhou"]
#print(x)

d={'li':[1,2,3,4],'wang':[100,1,2],'zhang':[1,3,2,1],'zhao':[2,3,5,10],'qian':[12312312,12321],
   'sun':[1,2,3,4],'liu':[100,10,2],'chen':[1,23,4],'yang':[89],'zhou':[1]}

a=d.values()
print(a)
#set=d["chen",'li','liu','qian','sun','wang','yang','zhang','zhang','zhao','zhou']









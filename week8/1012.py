# #숙제 23.10.10
# a=list(range(-10,1))

# b=list(range(1,11))

# a.extend(b)

# print(a)

# print(len(a))

# c = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# c[0] = c[0]*10
# c[1] = c[1]*10
# c[2] = c[2]*10
# c[3] = c[3]*10 
# c[4] = c[4]*10
# c[5] = c[5]*10
# c[6] = c[6]*10
# c[7] = c[7]*10
# c[8] = c[8]*10
# c[9] = c[9]*10
# c[10] = c[10]*10
# c[11] = c[11]*10
# c[12] = c[12]*10
# c[13] = c[13]*10
# c[15] = c[15]*10
# c[16] = c[16]*10
# c[17] = c[17]*10
# c[18] = c[18]*10
# c[19] = c[19]*10
# c[20] = c[20]*10
# c[21]= c[21]*10



# a = [10,2,3,[10,2,[3,4,51]],1]

# del a[3][2]
# print(a)


# b = [10,2,3,[10,2,[3,4,51]],1]

# #[10,2,[2,[3,4]],1]

# # del b[2]

# # del b[2][0]

# # del b[2][1][2]

# # print(b)

# b.remove(3)
# b[2].remove(10)
# b[2][1].remove(51)
# print(b)

# a=[]
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.append(6)
# a.append(7)
# a.append(8)
# a.append(9)
# a.append(10)
# print(a)

# #[1,2,3,[10,2,3],5,[1,2,3]]
# b = []
# b.append(1)
# b.append(2)
# b.append(3)
# b.append([10,2,3])
# b.append(5)
# b.append([1,2,3])

# print(b)

li = [1,2,3,4]
li.reverse()
print(li)
b = list(reversed(li))
print(b)
# # # 1.라즈베리파이라는 문자를 변수에 담고 이를 역순으로 출력
# # a = "라즈베리파이"
# # b = a[::-1]
# # print(b)

# # # 2. 1024를 각각 2, 8, 16진수로 출력

# # a = 1024

# # b = bin(a)[2:]    
# # c = oct(a)[2:]
# # d = hex(a)[2:]

# # print(a)
# # print(b)
# # print(c)
# # print(d)

# # # 3. 첫번째 리스트를 range() 함수를 사용하여 생성 -100- 0

# a=list(range(-100,1))

# # # 4. 첫번째 리스트를 range() 함수를 사용하여 생성 0- 100

# b=list(range(-1,101))

# # 5. 두번째 3,4번에서 만들어진 리스트를 어떤 함수를 통해 합쳐서 출력

# a.extend(b)
# print(a)

# # 6. 5번에서 만들어진 리스트를 역순으로 출력 (변수에 담아서)

# c=a[::-1]
# print(c)


# # 7. 6번에서 만들어진 리스트에 [1,2,3,4,5]를 추가하여 출력

# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)

# a.append([1,2,3,4,5])

# a = [50, 2, 3, 4]
# b = [5,6,3,2]
# c = [1,3,2]

# a.sort()
# b.sort()
# c.sort()

# c.append(a)
# c.append(b)

# print(c)

# a = [1,2,3]
# a. index (4)
# print(a.index(3))

# a = [1,2,3,['a', 'b','g'],['o', 'p', 'a'],['d']]
# # good
# result=''
# g=a[3].index('g')
# o=a[4].index('o')
# o=a[5].index('d')
# d=a[5].index('d')

# result += a[3][g]
# result += a[4][o]
# result += a[4][o]
# result += a[5][d]

# print(result)

# a=['apple','bannana','orange','apple']
# print(a.count('apple'))

# a = ["apple", "banana",[1, "okay", [1,2,3]],"orange",
# [1, "good"],"apple"]

# # a = ["apple",[1,"okay",[3]],["good"],"apple"]

# a.pop(1) 
# a[1][2].pop(0)
# a[1][2].pop(0)
# a[3].pop(0)
# a.pop(2)

# print(a)

# li=list(range(2,12,2))
# li.insert(0,1)
# li.insert(2,3)
# li.insert(4,5)
# li.insert(6,7)
# li.insert(8,9)
# print(li)

# a = []

# a.append(1)
# a.append(2)
# a.append(3)

# b = [5, 4, 3, 2, 1]
# a.append(b)

# a.append(4)

# c = [[5, 4, 3]]
# a.extend(c)

# d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a.extend([d])

# a.append(1)

# print(a)









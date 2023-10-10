# a = [1, 2, 3, ['a', 'b',['t',2 , 3,[1, 2]], 'C'], 4, 5]

# b=a[3][1:3]
# print(b)
# c=b[::-1]
# print(c)

# print(a[2:5]) # 3, ['a', ‘b',['t',2 , 3,[1, 2]], 'C'], 4,
# # 출력값:[3, ['a', 'b', ['t', 2, 3, [1, 2]], 'C'], 4] 
# #      ^^                                         ^^  -> 왜 괄호가 생기는거에요??? (위에는 없음)

# print(a[2:5:-1]) # 3, ['a', ‘b',['t',2 , 3,[1, 2]], 'C'], 4,
# # 출력값:[]????? -> 왜 출력값이 list이에요???. 끝에 "-1" 붙이면 되는줄알았는데..? 
# b=a[::-1]
# print(b)

# a=list(range(1,100,3))
# print(a)

# b=list(range(-100,0,1))
# print(b)

# c = 3,['a', 'b',['t',2 , 3,[1, 2]], 'C'], 4
# print(c[::-1]

# a.extend()
# b.reverse() -> "b" reverses and changes permanently 
# c = reversed(b) -> "b" is copied and reverses b and inserts it into function c.

# a=list(range(-100,1))
# b=list(range(2,100))

# a.extend(b)
# print(a)

# a.reverse(b)
# print(a)

# d = reversed(b)

# a =[1,2,3,[4,5,[6,7,8],1]]

# # n=(a[3][:3]) #[4,5,[6,7,8]
# # print(n*5)

# print(len(a)) # --> die Laenge von eine variable messen


a = [1,2,3,4,[2,3,5,[8,10,11]]]

a[4][0] = 5
a[4][1] = 6
a[4][2] = 7
a[4][3][0] = 8
a[4][3][1] = 9
a[4][3][2] = 10

print(a)







#1012숙제 -> 

# # 문제 1
# a = [1,2,3,[7,6,5]]
# # 결과값
# a= [1,2,3,[5,6,7],8,9,10] # append랑, reverse 또는 reversed를 통해서 구현

a=[1,2,3,[7,6,5]]

a.append(8)
a.append(9)
a.append(10)
a[3].reverse()

print(a)


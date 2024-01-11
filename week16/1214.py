#a,b,c=map(int,input().split())


# a,b,c = map(int, input().split())
# d=str(a)
# e=str(b)
# f=str(c)

# if c < 10:
#     print(d+e+'0'+f)

# else:
#     print(d+e+f)


# a = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


# b = input()
# c=int(b)

# if c in [1,3,5,7]:
#     print("oh my god")

# else:
#     print("enjoy")



# a = int(input())

# if a > 0:
#     print("양수")
# elif a < 0:
#     print("음수")
# else:
#     print("0")


# a,b,c = map(int, input().split())
# d=str(a) #학년
# e=str(b) #반
# f=str(c) #번호

# if e < 10:
#     print(d+'0'+e+f)
# if f < 100:
#     print(d+'0'+e+'00'+f)

# else:
#     print(d+e+f)

# a, b, c = map(int,input().split())
# e = str(a)
# f = str(b)
# g = str(c)

# if b < 10 :
#     f = '0' + f

# if c < 10 :
#     g = '00' + g

# elif c < 100 :
#     g = '0' + g

# x = e + f + g

# print(x)

BMI = int(input())
if BMI <= 10: 
    print('정상') 
elif BMI <= 20:
    print("과체중")
        
else: print('비만')
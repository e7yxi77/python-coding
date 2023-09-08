print("'hi'")
print("hello\nworld")
a,b,c=map(int,input().split())
print(a,b,c)
a=1
print(type(a))
str(a)
float(a)
print("a","b",sep=".")
print("a","b",end=" ")
print("a","b")
print("a","b")
year=2023
month=9
day=7
print(year,month,day,sep="-",end="T")

print(2>3) # 초과 -> false
print(2>=3) # 이상 -> false
print(1<2) # 미만 -> true
print(1<=2) #이하 -> true

print(1==1) # same -> true
print(1!=1) # diffrent -> false

print("python"=="python") # -> true
print("python"!="python") # -> false

print(not True) # -> false

print(1 is 1) # -> true

a=1
b=1
print(a is b)

print(True and True) # true 
print(True and False) # false
print(False and False) # false
print(True or True) # true
print(True or False) # true
print(False or False) #false

print(not True and not False or not False)
print(False and True or True) 

print((not True) and False) or (not False)

print(10 == 10 and 10 != 5) # True and True
print(10 > 5 or 10 < 3) # True or False
print(not 10 > 5) # not True -> False
print(not 1 is 1.0) # not False ->< True


#숙제: 토딩 도장 8.3
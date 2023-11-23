# # d= {"dict": {"1":2, "2":4, "data":{"data":[1,2,34]}}}
# # a=d["dict"]
# # b=a["1"]
# # c=a["2"]
# # e=a["data"]
# # f=e["data"]
# # print(b)
# # print(c)
# # print(f)

# # print(2>3) # 초과 
# # print(2>=3) # 이상 
# # print(1<2) # 미만 
# # print(1<=2) #이하 
# # print(1==1) # 같다 
# # print(1!=1) # 같지 않다 

# # Password=1234
# # a=input() 
# # Password=str(Password)
# # a=str(a)
# # if a==Password: 
# #     print("hello")
# #     print("welcome")
# #     print("hi")

# # else:
# #     print("wrong password")

# dic = {"key":{"key2":"value","key3":["value1","value2","value3"]}}

# if len(dic) > 1:
#     print("okay")

# else:
#     print("not okay")

# if len(dic["key"]["key3"]) < 2:
#     print("okay")

# else:
#     print("not okay") 

# if dic["key"]["key3"][1] == "value2":  
#     print("okay")

# else:
#     print("not okay") 

money = input()
money=int(money)
if money >= 5000:
    print("택시를 타세요.")

    if money >= 10000:
        print("비행기를 타세요.")

        if money >= 100000:  
            print("배를 타세요.")
            
        else: 
            print("다시 택시를 타세요")

else:
    print("걸어가세요.")



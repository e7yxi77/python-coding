# # money = input()
# #   if money <= 5000:
# #         print("다시 택시를 타시오")
# # if money == 100000:  
# #     print("배를 타세요.")
  

# #     if money >= 5000:
# #         print("뛰어가세요.")

# # else: 
# #     print("다시 택시를 타세요")


# money=int(input())
# if money >= 5000:
#     print("택시를 타세요.")

#     if money >= 10000:
#         print("비행기를 타세요.")

#         if money >= 100000:  
#             print("배를 타세요.")
            
#             if money >= 5000:
#                 print("뛰어가세요.")
      
            
#         else: 
#             print("다시 택시를 타세요")

# else:
#     print("걸어가세요.")

# pocket=['paper','cellphone','money']
# if 'money' in pocket:
#     print('go by taxi')
# else:
#     print('walk')

# pocket=['paper','cellphone']
# card = True
# if 'money' in pocket:
#     print("go by taxi")
# elif card:
#     print("go by taxi")
# else:
#     print('walk')

# if 'moeny' in pocket: pass
# else: print('카드를 꺼내라')

# li = [1, 2, 3, ['good']]

# message = "okay" if 'good' in li[3] else "not okay"

# print(message)
# pocket = ['paper', 'cellphone']
# card = True

# message = "택시를 타고 가세요." if 'money' in pocket else "카드가 있으니 택시를 타고 가세요." if card else "돈도 없고 카드도 없으니깐 걸어가세ㅔ요."
# print(message)

# money=int(input())
# card=True
# if money >= 3000 or card:
#     print('taxi')
# else:
#     print('walk')

li = [2, 3, 4, 5, ["good", "bad", [100, 200, ["hello"]]]]
li=str(li)

if "good" in li[4] and 100 in li[4][2] and "hello" not in li[4][2][2]:
    print("힘들다")















    
elif 3 in [0]:
    print("힘들다2")
else:
    print("힘들다3")

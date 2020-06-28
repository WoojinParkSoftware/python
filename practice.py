# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
# print(5 > 10)
# print(5 < 10)
# print(True)

# #애완동물을 소개해 주세요~
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# ''' 주석처리
# 된다 '''
# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# station = "사당"
# print(station + " 행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + " 행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + " 행 열차가 들어오고 있습니다.")

# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2

# print(2**3) # 2^3=8
# print(5%3) # reaminers 2
# print(10%3) # 1
# print(5//3) # 1
# print(10//3) #3

# print(10 > 3) #ture
# print(4 >= 7) #false
# print(5 <= 5) #true

# print(3 == 3) # true
# print(3 + 4 == 7) #true

# print(1 != 3) # true
# print(not(1 != 3)) #false

# print((3 > 0) and (3 < 5)) #all true
# print((3 > 0) & (3 < 5)) #all true

# print((3 > 0) or (3 > 5)) #true from any
# print((3 > 0) | (3 > 5)) #ture
# print(5 > 4 > 3) #true
# print(5 > 4 > 7) #false

# print(2 + 3 * 4) 
# print((2 + 3) * 4)
# number = 2 + 3 * 4 #14
# print(number)
# number = number + 2 #16
# print(number) #16
# number += 2 #18
# print(number)
# number *= 2 #36
# print(number)

# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))
# print(round(4.99))

# from math import *
# print(floor(4.99)) #4
# print(ceil(3.14)) #4
# print(sqrt(16)) #4

# from random import *

# print(random()) # 0.0 ~ 1.0
# print(random() * 10) # 0.0 ~ 10.0
# print(int(random() * 10)) # 0 ~ 10 미만
# print(int(random() * 10) + 1) # 1 ~ 10 이하

# print (randrange(1, 46)) #1~46 미만
# print(randint(1, 45)) #1~45이하

# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정 되었습니다.")

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """ 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990223-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #(0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) #from the beginning
# print("뒤 7 자리 : " + jumin[7:]) #till the end
# print("뒤 7 자리 (뒤에부터): " + jumin[-7:]) #from the end 

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0] .isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) #after the previous one
print(index)

print(python.find("n"))

print(python.find("Java")) #gives -1 and dont shut down
#print(python.index("Java")) #makes error and shut down
print(python.count("n"))

#print("a" + "b")
#print("a", "b")

# # option 1
# print("나는 %d살입니다." % 20) #int
# print("나는 %s을 좋아해요" % "파이썬") #string
# print("Apple 은 %c로 시작해요." % "A") #character
# # %s 
# print("나는 %s 색과 %s 색을 좋아해요" %("파란", "빨간"))

# #option 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

#option 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age = 20))

#option 4

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")



# print("백문이 불여일견\n백견이 불여일타")

# print("저는 '나도 코딩'입니다.")
# print('저는 "나도 코딩"입니다.')
# print("저는 \"나도 코딩\"입니다.")
# print("저는 \'나도 코딩\'입니다.")

# print("C:\\Users\\CODING ONLY\\Desktop\\Python>")

# print("Red Apple\rPine")
# print("Redd\bApple")

# print("Red\tApple")

# url = "http://naver.com"
# my_str = url.replace("http://", "")
# print(my_str)
# my_str = my_str[:my_str.index(".")] #my_str[0:5]
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f"{url}의 생성된 비밀번호는 : {password} 입니다.")
# print("{0}의 생성된 비밀번호는 : {1} 입니다." .format(url, password))
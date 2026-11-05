# 함수
# 
# 함수 정의
# def say_hello(name, age):
#     print("안녕하세요")
#     print("저는"+ name +"입니다")
#     print("나이는"+ age +"살 입니다")
#     print("안녕히가세요")

# # 함수 호출
# say_hello("우진", "13")
# say_hello("지완", "12")

# 전체 누적 합을 계산해주는 함수

# def get_sum(start, end):
#     sum = 0
#     for i in range(start, end+1):
#         sum += i
#     print("합:", sum)

# get_sum(1,10)

# 두 수를 전달받아서 합을 출력해주는 함수 add()를 만들어봅시다.
# def add(a, b):
#     print(a+b)

# add(1000, 1)

## 두 수 중 큰 수를 알려주는 함수
#두 개의 숫자를 전달받아 더 큰 숫자를 출력하는 `max_number()` 함수를 만들어 보세요.

# def max_number(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# number = max_number(1,10)
# print(number)

# def judge(num):
#     if num % 2 == 0:
#         print("짝수")
#         return
#     print("홀수")

# num = int(input("자연수를 입력하세요:"))
# judge(num)  

# def abc():
#     return 1,2

# x, y = abc()
# print(x, y)

# import turtle
# t= turtle.Turtle()
# t.shape("turtle")

# def square(length):
#     for i in range(4): # square
#         t.forward(length) # 변을 함수의 매개변수로 받도록
#         t.left(90)

# square(1000)

# t.up()
# t.goto(-200,0)
# t.down()

# square(100)


# 리스트의 모든 숫자를 더하는 함수
# sum_list 
# total 변수 사용 (전체 합)

# def sum_list(num_list):
#     total = 0
#     for num in num_list:
#         total += num
#     print(total) 

# sum_list([1,2,3,4,5])

# 시험 점수(score)를 인수로 받아
# 점수가 60점 이상이면 "통과", 
# 60점 미만이면 "탈락"을 반환(return)하는 
# 함수 check_pass를 작성하세요

# print(check_pass(85))

#분식집에서 떡볶이 한 접시의 가격(price)과 개수(count)를 알려주면, 
#전체 가격을 계산해서 알려주는 똑똑한 계산기 함수를 만들려고 해요.

#500원짜리 떡볶이 3인분의 총가격을 구하는 코드를 완성해 볼까요?

# def calculate(price, count):
#     total = price * count
#     return total

# a = calculate()

# 문제
# 놀이공원 매표소 직원 로봇을 만들려고 합니다. 손님의 나이(age)를 입력하면, 
# 나이에 따라 티켓 가격을 계산해서 돌려주는 함수 calculate(age)를 만들어야 해요

# 💰 할인 규칙
# 8살 미만 (어린이): 무료 (0원)
# 8살 이상 19살 이하 (학생): 8,000원
# 20살 이상 (어른): 15,000원


# 거북이가 마법의 주문을 외우며 반짝이는 별 모양을 그리는 프로그램을 만들려고 합니다. 
# 별은 앞으로 150만큼 갔다가 오른쪽으로 144도 회전하는 동작을 5번 반복하면 완성돼요.
# 이 과정을 draw_star()라는 함수로 만들어 볼까요?

# t.color("purple")
# t.pensize(3)
# t.speed(3)


# 영화관에서 영화를 보려고 합니다. 
# 손님의 나이(age)와 보고 싶은 영화가 
# 청소년 관람 불가 영화인지 여부(adult_only)를 입력받아, 
# 볼 수 있는지 판별해 주는 함수를 만들어 보세요!

# 📝 규칙
# 보고 싶은 영화가 청소년 관람 불가(True)인데 
# 나이가 19세 미만이면: "관람 불가"
# 그 외의 경우는 모두: "관람 가능"

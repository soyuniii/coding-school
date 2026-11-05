# 조건문

# 점수 60점 이상이면 합격,수고하셨습니다.

# score = 80
# if score >= 60:
#     print("합격입니다!")
# else:
#     print("")
# print("수고하셨습니다")


# 사용자의 나이를 입력받고, 영화 관람 여부를 출력하는 프로그램
# 15세 이상이면, 영화 관람 가능. 아니면 불가.




# 점수 score 를 60점 이상이면 합격, 수고하셨습니다.

# score = int(input("점수를 입력하세요: "))
# if score >= 60:
#     print("합격입니다!")
#     print("100만원 장학금을 받으세요")
# else:
#     print("공부를 좀 더 하세요...")
# print("수고하셨습니다")

# box = int(input("상자를 골라보세요 (1,2,3,4 중 선택:)"))

# if box == 1:
#     print("100만원 당첨되었어요!")

# if box == 2:
#     print("함정에 빠졌습니다!")

# if box == 3:
#     print("도마뱀이 나왔습니다")

# if box == 4:
#     print("보물 대신 감자가 나왔어요")

# 사용자의 나이를 입력하면 영화관람 가능 / 불가능 여부를 화면에 출력

# 숫자 입력받고 짝수/홀수 판별

# n = int(input("숫자를 입력하시오: "))

# if n%2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 정수 (int) 
# 양(1 2 3 4 ...)
# 음(-1, -2, -3 ...)
# 0
# n = int(input("정수를 입력하시오: "))
# if n > 0:
#     print("양수")
# elif n == 0:
#     print("0입니다")
# else:
#     print("음수")

# n = int(input("정수를 입력하시오: "))
# if n >= 0:
#     if n > 0:
#         print("양수")
#     else: 
#         print("0")
# else:
#     print("음수")

# 직각 삼각형
# 피타고라스 정리 공식a,b,c (a+b>c)

# a*a + b*b = c*c

# a,b,c길이 입력받고,
# 직각삼각형 인지 아닌지 판단

# a = int(input("변 a의 길이:"))
# b = int(input("변 b의 길이:"))
# c = int(input("변 c의 길이:"))

# if a*a + b*b == c*c:
#     print("직각삼각형 입니다")
# else:
#     print("직각삼각형 아닙니다")

# import random
# print("주민등록번호의 성별 번호를 생성합니다.")
# gender = random.randrange(4) # 0-3
# gender = gender+1 # 1-4 무작위 수
# print("생성 번호:", gender)

# 조건문 사용해서  and, or
# 1 또는 3 -> 남성
# 2 또는 4 -> 여성 

# random 동전 앞뒷면 맞추기 게임
# import random
# print("동전 앞,뒤 맞추기 게임")

# # 컴퓨터가 동전을 던지게 (0: 앞면, 1: 뒷면)
# coin = random.randint(0,1)

# # 사용자 입력
# guess = input("앞면 또는 뒷면을 입력하세요:")

# # 컴퓨터 결과를 문자로 변환
# if coin == 0:
#     result = "앞면"
# else:
#     result = "뒷면"

# # 정답 판별하기
# if guess == result:
#     print("맞췄습니다!")
# else:
#     print("틀렸습니다...")


# 컴퓨터에게 1부터 3까지의 숫자 중 하나를 뽑게 한 뒤, 
# 조건문을 이용해 1이면 "가위", 2이면 "바위", 3이면 "보"라는 글자로 바꿔줘요.
# 우리가 배운 if-elif-else 조건문을 사용해서 만들어 봅시다.

import random

r = random.randint(1,3)

# 내가 선택하기 (가위,바위,보)
player = input("가위, 바위, 보 ! :")

# 컴퓨터의 선택 (1,2,3) -> (가위,바위,보)로 바꿔주기

if r == 1:
    computer = "가위"
elif r == 2:
    computer = "바위"
else:
    computer = "보"

# 컴퓨터랑 내가 선택한 결과 print
print("컴퓨터 선택:", computer)
print("내 선택:", player)

# 비교 -> 승부판정
if player == computer:
    print("비겼음!")

elif ((player == "가위" and computer == "보")or(player =="바위" and computer == "가위")or(player == "보" and computer=="바위")):
    print("이겼어요!")

else:
    print("졌음 ㅜㅜ")

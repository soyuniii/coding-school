# 🎲 주사위 대결 게임 (컴퓨터 vs 나)
# 컴퓨터와 내가 주사위를 하나씩 던집니다! 
# 1부터 6까지의 눈 중에서 더 큰 숫자가 나오는 사람이 승리하는 게임이에요.

import random

input("주사위를 던지려면 엔터 키를 누르세요! ")

# 컴퓨터와 내가 1부터 6 사이의 숫자를 무작위로 뽑기
com_dice = random.randint(1, 6)
my_dice = random.randint(1, 6)

# 결과 출력
print(f"\n🤖 컴퓨터의 주사위 눈: {com_dice}")
print(f"🧑 나의 주사위 눈: {my_dice}\n")

# 조건문으로 승부 판정하기
if my_dice > com_dice:
  print("축하합니다! 당신이 주사위 눈이 더 커서 이겼습니다! 🎉🏆")

elif my_dice < com_dice:
  print("아쉽습니다! 컴퓨터의 주사위 눈이 더 커서 졌습니다! 😭")

else:
  print("무승부입니다! 주사위 눈이 똑같이 나왔어요! 🤝")
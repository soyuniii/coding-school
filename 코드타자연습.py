import random
import time


def check_typing(quiz, user_input):
  """문제를 올바르게 입력했는지 확인하고 결과를 반환하는 함수"""
  if quiz == user_input:
    return "정답"
  else:
    return "오답"


def run_typing_game():
  """타자 연습 게임을 전체적으로 실행하는 함수"""
  # 연습할 파이썬 기초 코드 목록 (리스트)
  code_list = [
      "print('Hello, World!')",
      "for i in range(5):",
      "if score >= 60:",
      "def my_function():",
      "import random",
      "while True:",
      "my_list = [1, 2, 3]",
      "return total",
  ]

  # 게임 시작 준비
  random.shuffle(code_list)  # 코드를 무작위로 섞음
  score = 0  # 맞춘 개수 저장
  total_questions = 3  # 총 연습할 문제 수

  print("================================")
  print("       파이썬 코드 타자 연습      ")
  print("================================")
  print(" 화면에 나오는 코드를 똑같이 입력하세요.\n")

  start_time = time.time()  # 시작 시간 기록

  # 연습 진행 (3문제)
  for i in range(total_questions):
    quiz = code_list[i]
    print(f"\n[{i+1}번 문제] {quiz}")

    user_input = input("👉 입력: ")

    # 중요: 함수(check_typing)를 호출하여 인수 전달 후 return 값 받기
    result = check_typing(quiz, user_input)

    if result == "정답":
      print("⭕ 정확하게 입력했습니다!")
      score += 1
    else:
      print("❌ 오타가 있습니다! 다시 집중해 보세요.")

  end_time = time.time()  # 종료 시간 기록
  total_time = end_time - start_time  # 걸린 시간 계산

  # 결과 출력
  print("\n================================")
  print("           연습 결과            ")
  print("================================")
  print(f"▶︎ 맞춘 개수: {score} / {total_questions}")
  print(f"▶︎ 총 걸린 시간: {total_time:.2f}초")
  print("================================")


# 프로그램 실행
run_typing_game()

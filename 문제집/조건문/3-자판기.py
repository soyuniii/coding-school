# 스마트 편의점 계산기

# 💰 자판기 메뉴판
# 1번: 콜라 (800원)
# 2번: 불닭 (1600원)
# 3번: 과자 (1000원)

# money로 돈을 넣고, choice로 선택하세요
money = int(input("돈을 입력하세요: "))
choice = int(input("상품 번호를 입력하세요 (1~3): "))

# 고른 번호에 따라 상품이름 name, 가격 price 정하기
if choice == 1:
    name = "콜라"
    price = 800


# 돈 계산해서 결과와 잔돈 출력하기
if money >= price: # 내돈이 더 클때
    print(name,"구매완료!", "잔돈:",money-price)
else: # 돈이 부족할때
    print("돈이", price-money,"원 부족해요!")
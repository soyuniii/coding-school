map = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]  

a = int(input("행을 입력하세요: "))
b = int(input("열을 입력하세요: "))

if map[a][b] == 1:
    print("보물을 찾았어요")
else:
    print("보물을 찾지 못했어요...")
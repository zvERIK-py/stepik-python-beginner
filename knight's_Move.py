 # ход коня в шахматах

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x1 - x2
dy = y1 - y2


if (dx * dx + dy * dy == 5):  # 2² + 1² = 5, 1² + 2² = 5
    print("YES")
else:
    print("NO")
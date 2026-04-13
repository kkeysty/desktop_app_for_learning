def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0

    n = int(input[ptr])
    ptr += 1

    a = list(map(int, input[ptr:ptr + n]))
    ptr += n

    b = list(map(int, input[ptr:ptr + n]))
    ptr += n

    m = int(input[ptr])
    ptr += 1

    x = list(map(int, input[ptr:ptr + m]))
    ptr += m

    y = list(map(int, input[ptr:ptr + m]))

    # Проверка корректности трассы
    for i in range(n - 1):
        L_i = 1 if b[i] == 1 else 2 if b[i] == 2 else 4
        if a[i + 1] <= a[i] + L_i:
            print(0)
            return

    # Сортируем прыжки по координате начала
    jumps = sorted(zip(x, y), key=lambda p: p[0])

    score = 0
    for i in range(n):
        L_i = 1 if b[i] == 1 else 2 if b[i] == 2 else 4
        obstacle_start = a[i]
        obstacle_end = a[i] + L_i

        # Бинарный поиск: ищем первый прыжок, который начинается после obstacle_start
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if jumps[mid][0] > obstacle_start:
                right = mid
            else:
                left = mid + 1

        # Проверяем прыжки до left
        covered = False
        for j in range(left):
            if jumps[j][0] + jumps[j][1] >= obstacle_end:
                covered = True
                break

        if covered:
            score += 1 if b[i] == 1 else 3 if b[i] == 2 else 5
        else:
            score -= 1

    print(max(score, 0))

solve()

n = [2, 3, 1, 0, 4]


def jump(n):
    goal = len(n)-1

    for i in range(len(n) - 1, -1, -1):
        if i + n[i] >= goal:
            goal = i
    return True if goal == 0 else False


print(jump(n))
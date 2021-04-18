import random


def compare(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        return a[0] > b[0]
    else:
        return False


def sort_igrok():
    kol = int(input('количество игроков: '))
    igroki = [[random.randint(100, 1000), random.randint(1, 100)] for i in range(kol)]
    for i in range(1, len(igroki)):
        bb = igroki[i]
        j = i - 1
        while j >= 0 and compare(bb, igroki[j]):
            igroki[j + 1] = igroki[j]
            j -= 1
        igroki[j + 1] = bb
    return igroki


print("Отсортированные участники по баллам,\n[игрок, балл]: ", sort_igrok())



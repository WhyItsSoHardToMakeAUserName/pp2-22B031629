import itertools
import math
import random


def gramstoOunces(a):
    return a * 28.3495231


def ftocel(a):
    return (5 / 9) * (a - 32)


def head_legs(heads, legs):
    rabbit_count = (legs - 2 * heads) / 2
    chicken_count = heads - rabbit_count
    print("chicken {}, rabbits {}".format(int(chicken_count), int(rabbit_count)))


def filter_prime(arr):
    cnt = 0
    arr = arr.split(' ')
    for i in arr:
        i = int(i)
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 2 or i == 1:
            print(i)
        cnt = 0


def perstr(s):
    permutations = list(itertools.permutations(s, len(s)))
    for i in permutations:
        print("".join(i))


def rev_word(s):
    l = s.split()
    l = reversed(l)
    print(" ".join(l))


def has_33(arr):
    cnt = 0
    for i in range(1, len(arr) - 1):
        if arr[i] == 3:
            if arr[i - 1] == 3 or arr[i + 1] == 3:
                cnt += 1
    if arr[0] == 3:
        cnt += 1
    if arr[len(arr) - 1] == 3:
        cnt += 1

    if cnt == arr.count(3):
        print("True")
    else:
        print("False")


def spy_games(arr):
    for i in range(len(arr)):
        t = arr[i]
        arr[i] = str(t)
    z = "".join(arr)
    print("007" in z)


def volume_sphere(r):
    v = 4 / 3 * (math.pi * pow(r, 3))
    print(v)


def Uniq(arr):
    for i, k in enumerate(arr):
        if arr.count(k) > 1:
            arr.remove(k)
    print(arr)


def Pal(s):
    print(s == s[::-1])


def his(arr):
    for i in arr:
        print("*" * i)


def Game():
    gn = int(input())
    n = random.randint(1, 20)
    while gn != n:
        if gn > n:
            print("high")
        else:
            print("low")
        gn = int(input())
    print("Good job")


filter_prime("1 2 3 4 5 6 7 8 9 11")
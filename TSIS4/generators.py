def squares(n):
    for i in range(n):
        yield i ** 2


# a = squares(5)
# for i in a:
#     print(i)


def filter(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# num = int(input())
# b = filter(num)
# for i in b:
#     print(i)

def devide3_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# num = int(input())
# c = devide3_4(num)
# for i in c:
#     print(i)

def squares2(a, b):
    for i in range(a, b):
        yield i ** 2


# d = squares2(1, 5)
# for i in d:
#     print(i)

def fifth(n):
    while n >= 0:
        yield n
        n -= 1

# e = fifth(5)
# for i in e:
#     print(i)

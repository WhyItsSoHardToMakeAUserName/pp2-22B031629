from function1 import  filter_prime
class first:
    def Getstring(self, a, b):
        self.b = b
        self.a = a

    def printString(self):
        print(self.a + " " + self.b)


class Shape:
    def area():
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(int(self.length) ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(int(self.length) * int(self.width))


class Point:
    s = [0, ".", 0, 0, 0, ".", 0 , 0]

    def show(self):
        for k, i in enumerate(self.s):
            if i == ".":
                print(k)

    def move(self, x, y):
        self.x = x
        self.y = y
        for k, i in enumerate(self.s):
            if i == ".":
                self.s[k] = 0
        self.s[x] = "."
        self.s[y] = "."
        print(self.s)

    def dist(self):
        print(self.s)
        cnt = 0
        d = 0
        for i in self.s:
            if i == ".":
                cnt += 1
            if cnt == 1:
                d += 1
        print(d-1)



class Bank:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def deposit(self, m):
        self.bal += m

    def withdraw(self, n):
        if self.bal>=n:
            self.bal-=n
        else:
            print("not enough money")

    def GetBal(self):
        print(self.bal)


print(lambda arr: filter_prime(arr)("1 2 3 4 5 6 7"))




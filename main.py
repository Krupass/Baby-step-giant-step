import math
import time


def inverse(number, power, modulo):
    return (number ** (modulo - 1 - power)) % modulo

def bsgs(a, b , m):

    n = m - 1
    h = math.ceil(math.sqrt(n))

    for i in range(0, h):
        left = (b * (inverse(a, (h * i),m))) % m

        for j in range(0, h):
            right = (a ** j) % m
            print("Difference between left and right: " + str(abs(left - right)), end="\r")
            time.sleep(.001)

            if(left == right):
                return ((i * h) + j)


if __name__ == '__main__':
    a = int(input("Zadej A: "))
    b = int(input("Zadej B: "))
    mod = int(input("Zadej modulo: "))
    result = bsgs(a, b , mod)
    print("\nBrutforced X: "  + str(result))


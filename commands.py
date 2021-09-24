from codec.elias import Elias_decode, Elias_encode


def com1():
    arr = list(map(int, input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))


def com2():
    arr = list(map(lambda x: int(x, 2), input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))


def com3():
    arr = list(map(lambda x: str(int(x, 2)), input("Enter data\n >> ").split()))
    print(" <<", " ".join(arr))


def com4():
    arr = input("Enter data\n >> ")
    print(" << ", end="")
    for i in arr.encode('cp1251'):
        print(i, end=" ")
    print()


def com5():
    arr = input("Enter data\n >> ")
    print(" << ", end="")
    for i in arr.decode('cp1251'):
        print(i, end=" ")
    print()


def com6():
    arr = input("Enter data\n >> ").replace(" ", "")
    print(" <<", Elias_decode(arr))


def com7():
    arr = input("Enter data\n >> ")
    print(" <<", Elias_encode(arr))

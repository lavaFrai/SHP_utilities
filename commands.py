from codec.elias import Elias_decode, Elias_encode
from codec.siberian import Siberian_decode, Siberian_encode
from codec.systems import convert_numerical_system
import codec.numsys.__init__


def com1():
    arr = list(map(int, input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))


def com2():
    arr = list(map(lambda x: int(x, 2), input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))


def com3():
    from_base = int(input("Enter from base\n >> "))
    to_base = int(input("Enter to base\n >> "))
    arr = list(map(lambda x: convert_numerical_system(x, to_base, from_base), input("Enter data\n >> ").split()))
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


def com8():
    arr = input("Enter data\n >> ")
    print(" <<", Siberian_decode(arr))


def com9():
    arr = input("Enter data\n >> ")
    print(" <<", Siberian_encode(arr))


def com10():
    from_base = int(input("Enter from base\n >> "))
    to_base = int(input("Enter to base\n >> "))
    arr = list(map(lambda x: codec.numsys.rebase(x,  from_base, to_base), input("Enter data\n >> ").split()))
    print(" <<", " ".join(arr))

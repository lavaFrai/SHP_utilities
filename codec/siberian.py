def Siberian_index(a, b):
    if b == 0 and a == 0:
        return 0
    if b == 0:
        if a % 2 == 0:
            return Siberian_index(a - 1, b) + 1
        else:
            return a * 2 + Siberian_index(a - 1, b)
    else:
        if bool(b % 2 == 1) != bool(a % 2 == 1):
            return Siberian_index(a, b - 1) + (2 * a + 1)
        else:
            return Siberian_index(a, b - 1) + (2 * b)

# =ЕСЛИ(C$1=0;
#   ЕСЛИ(ОСТАТ($A2;2)=0;
#       C1+1;
#       $A2*2+C1);
#   ЕСЛИ(ИСКЛИЛИ(ОСТАТ(C$1;2)=1;ОСТАТ($A2;2)=1);
#       B2+(2*$A2+1);
#       B2+2*C$1))


def Siberian_decode(data):
    a = len(data)
    if a == 0:
        return ""
    b, k = 0, 0
    print("Input data len:", a)
    while b < a:
        k += 1
        b = (k * (k + 1)) / 2
    b = int(b)
    print("Sizeof cone:", b)
    res = []
    for i in range(a):
        pass
    return "".join(res)


def Siberian_encode(data):
    a = len(data)
    if a == 0:
        return ""
    b, k = 0, 0
    print("Input data len:", a)
    while b < a:
        k += 1
        b = (k * (k + 1)) / 2
    b = int(b)
    print("Sizeof cone:", b)

    return

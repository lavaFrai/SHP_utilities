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


def SibF(x):
    x *= 2
    n = -1 + ((1 + 4 * x) ** 0.5) / 2
    return int(n + 0.5)

# =ЕСЛИ(C$1=0;
#   ЕСЛИ(ОСТАТ($A2;2)=0;
#       C1+1;
#       $A2*2+C1);
#   ЕСЛИ(ИСКЛИЛИ(ОСТАТ(C$1;2)=1;ОСТАТ($A2;2)=1);
#       B2+(2*$A2+1);
#       B2+2*C$1))


def Siberian_encode(data):
    a = len(data)
    if a == 0:
        return ""
    b, k = 0, 0
    # print("Input data len:", a)
    while b < a:
        k += 1
        b = (k * (k + 1)) / 2
    b = int(b)
    # print("Sizeof cone:", b)
    data += ' ' * (b - a)
    # print("First line size:", SibF(b))
    res = []
    k = 0
    for i in range(SibF(b), 0, -1):
        res.append([' ' for j in range(i)])
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = data[Siberian_index(i, j)]
    # for i in res:
    #     print(i)
    res = map(lambda x: ''.join(x), res)
    return "".join(res)


def Siberian_decode(data):
    b = 0
    k = 0
    while b < len(data):
        k += 1
        b = (k * (k + 1)) / 2
    b = int(b)
    data += ' ' * (b - len(data))
    b = 0
    k = 0

    a = len(data)
    tmp = []
    k = 0
    # print("Data len:", a)

    for i in range(SibF(a), 0, -1):
        # print(i, k)
        tmp.append(data[k:k+i])
        k += i
    res = []
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            # print(Siberian_index(i, j), end='\t')
            res.append([tmp[i][j], Siberian_index(i, j)])
        # print()
    res.sort(key=lambda x: x[1])
    res = map(lambda x: x[0], res)
    return "".join(res)


def Siberian_decode2(data):
    b = 0
    k = 0
    while b < len(data):
        k += 1
        b = (k * (k + 1)) / 2
    b = int(b)
    data += ' ' * (b - len(data))
    b = 0
    k = 0

    a = len(data)
    tmp = []
    k = 0
    # print("Data len:", a)

    for i in range(SibF(a), 0, -1):
        # print(i, k)
        tmp.append(data[k:k+i])
        k += i
    res = []
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            # print(Siberian_index(i, j), end='\t')
            res.append([tmp[i][j], Siberian_index(i, j)])
        # print()
    res.sort(key=lambda x: x[1])
    res = map(lambda x: x[0], res)
    return "".join(res)


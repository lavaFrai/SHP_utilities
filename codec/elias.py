def Elias_decode(arr):
    key = arr[0]
    arr = arr[1:]
    res = []
    i, ik = 0, 0
    while i < len(arr):
        if arr[i] == '1':
            i += 1
            res.append("1")
        else:
            if arr[i + 1] == '1':
                if arr[i + 2] == '0':
                    i += 3
                    res.append("010")
                else:
                    i += 3
                    res.append("011")
            else:
                if arr[i + 2] == '1':
                    if arr[i + 3] == '1':
                        if arr[i + 4] == '1':
                            i += 5
                            res.append("00111")
                        else:
                            i += 5
                            res.append("00110")
                    else:
                        if arr[i + 4] == '1':
                            i += 5
                            res.append("00101")
                        else:
                            i += 5
                            res.append("00100")
                else:
                    if arr[i + 5] == '1':
                        i += 7
                        res.append("0001001")
                    else:
                        i += 7
                        res.append("0001000")
    arr = list(map(lambda x: int(x, 2), res))
    res = ""
    for i in range(len(arr)):
        res += str(key) * arr[i]
        if key:
            key = 0
        else:
            key = 1
    arr = []
    for i in range(0, len(res), 8):
        arr.append(res[i:i + 8])
    arr = ''.join(list(map(lambda x: bytes([int(x, 2)]).decode('cp1251'), arr)))
    return arr


def Elias_encode(arr):
    arr = list(map(int, arr.encode('cp1251')))
    arr = list(map(lambda x: (str(bin(x))[2:]).zfill(8), arr))
    arr = ''.join(arr)
    res = []
    k, f = -1, arr[0]
    for i in arr:
        if i == f:
            k += 1
        else:
            res.append(k + 1)
            k = 0
            f = i
    res.append(k + 1)
    key = arr[0]
    arr = list(map(lambda x: str(bin(x))[2:], res))
    for i in range(len(arr)):
        while arr[i] not in ["1", "010", "011", "00100", "00101", "00110", "00111", "0001000", "0001001"]:
            arr[i] = "0" + arr[i]
    arr = [key] + arr
    arr = ''.join(arr)
    return arr

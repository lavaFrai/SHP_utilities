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

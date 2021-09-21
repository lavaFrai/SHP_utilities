mode = input("Enter mode from list (enter number)\n\t"\
    "1. DEC ascii decode\n\t"\
    "2. BIN ascii decode\n\t"\
    "3. BIN array to DEC\n\t"\
    "4. ASCII encode to DEC\n\t"\
    "5. Elias code decode (not work)\n >> ")
if mode == '1':
    arr = list(map(int, input("Enter data\n >> ").split()))
    #  list(map(chr, arr))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))
elif mode == '2':
    arr = list(map(lambda x: int(x, 2), input("Enter data\n >> ").split()))
    #  list(map(chr, arr))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))
elif mode == '3':
    arr = list(map(lambda x: str(int(x, 2)), input("Enter data\n >> ").split()))
    #  list(map(chr, arr))
    print(" <<", " ".join(arr))
elif mode == '4':
    arr = input("Enter data\n >> ")
    #  list(map(chr, arr))
    print(" << ", end="")
    for i in arr.encode('cp1251'):
        print(i, end=" ")# int.from_bytes(i, "big", signed="True"), end=" ")
    print()
elif mode == '5':
    arr = list(map(lambda x: str(int(x, 2)), input("Enter data\n >> ").split()))
    #  list(map(chr, arr))
    print(" <<", " ".join(arr))
else:
    print("can not parse run mode")

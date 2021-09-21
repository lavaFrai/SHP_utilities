from codec.elias import Elias_decode, Elias_encode


mode = input("Enter mode from list (enter number)\n\t"
             "1. DEC ascii decode\n\t"
             "2. BIN ascii decode\n\t"
             "3. BIN array to DEC\n\t"
             "4. ASCII encode to DEC\n\t"
             "5. BIN Elias code decode\n\t"
             "6. BIN Elias code encode\n >> ")


if mode == '1':
    arr = list(map(int, input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))
elif mode == '2':
    arr = list(map(lambda x: int(x, 2), input("Enter data\n >> ").split()))
    print(" <<", "".join(bytearray(arr).decode('cp1251')))
elif mode == '3':
    arr = list(map(lambda x: str(int(x, 2)), input("Enter data\n >> ").split()))
    print(" <<", " ".join(arr))
elif mode == '4':
    arr = input("Enter data\n >> ")
    print(" << ", end="")
    for i in arr.encode('cp1251'):
        print(i, end=" ")
    print()
elif mode == '5':
    arr = input("Enter data\n >> ").replace(" ", "")
    print(" <<", Elias_decode(arr))
elif mode == '6':
    arr = input("Enter data\n >> ").replace(" ", "")
    print(" <<", Elias_encode(arr))
else:
    print("can not parse run mode")

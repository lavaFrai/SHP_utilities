from commands import *


print("Enter mode from list (enter number)\n\t"
      "1. DEC ascii decode\n\t"
      "2. BIN ascii decode\n\t"
      "3. Numerical System convert\n\t"
      "4. ASCII encode to DEC\n\t"
      "5. ASCII decode to DEC\n\t"
      "6. BIN Elias code decode\n\t"
      "7. BIN Elias code encode\n\t"
      "8. Siberian code decode\n\t"
      "8A. Siberian code decode with fix\n\t"
      "9. Siberian code encode\n\t"
      "10. numsys Numerical System convert\n")

while True:
    try:
        exec("com" + str(input(" >> ")) + "()")
    except NameError:
        print("can not parse run mode")
    except BaseException as e:
        print("Unhandled Execution Exception:", str(e))
        print("Report this to the developer or check the entered data.")
    print()

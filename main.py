from commands import *

print("Enter mode from list (enter number)\n\t"
      "1. DEC ascii decode\n\t"
      "2. BIN ascii decode\n\t"
      "3. BIN array to DEC\n\t"
      "4. ASCII encode to DEC\n\t"
      "5. ASCII decode to DEC\n\t"
      "6. BIN Elias code decode\n\t"
      "7. BIN Elias code encode\n")

try:
    exec("com" + str(input(" >> ")) + "()")
except NameError:
    print("can not parse run mode")

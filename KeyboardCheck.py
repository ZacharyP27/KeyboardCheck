import sys

arg1 = sys.argv[1]     

def checkKeyboard():
    print("Your keyboard works, yay")

def help():
    print("Welcome to KeyboardCheck! \n In order to check your keyboard simply type the argument 'check' \n ('check' is the only working argument)")

if(arg1 == "check"):
    if len(sys.argv) < 3:
        checkKeyboard()
else:
    print("There is only one argument")
if len(sys.argv) > 2:
    print("There is only one argument")

if(arg1 == "--help"):
    help()

import os
import functions
import color
def clear(): return os.system('cls')


output = 0
Allnumbers = []
active = True
answer = "n"

while active == True:
    print(color.bcolors.OKGREEN +
          "\nwelcome to MY suka balde calculator bim bom boomm\n")
    while answer == "n":
        output = functions.new_output()
        print(output)
        Allnumbers.append(output)
        answer = input(
            'press N for new output press C to conteniue press H for history\n')
        clear()
        if answer == 'e':
            print(Allnumbers)
            active = False

    while answer == 'c':
        output = functions.con(output)
        print(output)
        answer = input(
            'press N for new output press C to conteniue press H for history\n')
        clear()
        if answer == 'n' or answer == 'h':
            Allnumbers.append(output)
        elif answer == 'e':
            print(Allnumbers)
            active = False

    while answer == 'h':
        output = functions.history(Allnumbers)
        print(output)
        Allnumbers.append(output)
        answer = input(
            'press N for new output press C to conteniue press H for history\n')
        clear()
        if answer == 'e':
            active = False



def new_output():
    Numbre1 = int(input('Number1 >>>> '))
    Numbre2 = int(input('Number2 >>>> '))
    operator = input("Enter your operator >>> ")
    match operator:
        case "+": return Numbre1 + Numbre2
        case "-": return Numbre1 - Numbre2
        case "*": return Numbre1 * Numbre2
        case "/": return Numbre1 / Numbre2


def con(output):

    newnum = int(input('New number >>>>  '))
    operator = input('Operator >>>> ')

    match operator:
        case "+": return output + newnum
        case "-": return output - newnum
        case "*": return output * newnum
        case "/": return output / newnum


def history(arrey):
    print(arrey)
    select = int(input("Select your Number hint:(indext number) "))
    newnum = int(input('New number >>>  '))
    operator = input('opreator >>> ')
    match operator:
        case "+": return arrey[select] + newnum
        case "-": return arrey[select] - newnum
        case "*": return arrey[select] * newnum
        case "/": return arrey[select] / newnum

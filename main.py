import random
# ? This sys right here (not step sis, sadly) will let us
# ? close the program
import sys
import os

options = ["Dizer olá", "Calculadora", "Sair"]

# ? After getting the data from other functions we greet the user, as asked
def greetings():
    name = getName()

    print(chooseGreeting() + " " + name)

# ? This function is lame, we just get the user's name and return it
def getName():
    name = input("Olá! Por favor introduz o teu nome: ")

    while name.strip() == "":
        print("Por favor introduza um nome válido!")
        name = input("Olá! Por favor introduz o teu nome: ")

    return name

# ? Choosing in an array of greetings, we will return a random one 
# ? and append it in the text from the function getName()
def chooseGreeting():
    greetings = ["Hello", "Hola", "Olá!", "Heyooo", "こんにちは"]
    # ? With the help of the "random" library we select a random greeting by index
    greetingIndex = random.randint(0, 4)

    return greetings[greetingIndex]

# ? Pffffftttt easy one
# ? Here we will just display the menu according to the options array
def showMenu():
    i = 0

    for option in options:
        i += 1
        print(str(i) + " - " + option + "\n")

# ? This cute function will only be called by other function (executeOption())
# ? and here we are just asking for which option the user wants to execute
def chooseOption():
    option = input("Escolhe uma opção (1, 2, ...) » ").strip()

    # ? We use this while loop just to verify if the option is valid
    while int(option) < 1 or int(option) > len(options):
        print("Por favor seleciona uma opção válida")
        option = input("Escolhe uma opção (1, 2, ...) » ").strip()

    return int(option)

# ? The following function will ask which function the user typed
# ? and then it will execute it, calling other functions
def executeOption():
    selectedOption = chooseOption() - 1

    if selectedOption == 0:
        greetings()
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    elif selectedOption == 1:
        calculadora()
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        print("Obrigador por usares o nosso programa")
        sys.exit()

# ? Uuuu this function is pretty simple.
# ? We just get two input numbers (without verification ehehe)
# ? and an operation. After that we just do the math
def calculadora():
    num1 = input("Por favor introduz o primeiro número » ")
    num2 = input("Por favor introduz o segundo número » ")

    operation = input("Por favor introduz uma operação » ")

    if operation == "+":
        print(str(int(num1) + int(num2)))
    elif operation == "-":
        print(str(int(num1) - int(num2)))
    elif operation == "*":
        print(str(int(num1) * int(num2)))
    else:
        print(str(int(num1) / int(num2)))

def main():
    showMenu()
    executeOption()

main()
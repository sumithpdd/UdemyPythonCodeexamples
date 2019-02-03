import re

print("Our Magical Calculator")
print("Type 'quit to exit")

answer = 0
run = True


def performMath():
    global run
    global answer

    if answer == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(answer))

    if equation == 'quit':
        run = False
        print("Goodbye!")
    else:
        equation = re.sub('[a-zA-Z,.:()=]', '', equation)

    if answer == 0:
        answer = eval(equation)
    else:
        answer = eval(str(answer) + equation)

        print("Answer", answer)


while run:
    performMath()

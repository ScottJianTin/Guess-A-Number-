import random


## This function allows users to guess a random number generated by computer
# def guess(x):
#     ans = random.randint(1, x)
#     guess = 0
#     while guess != ans:
#         guess = int(input("Guess a number: "))
#         if guess > ans:
#             print("Guess a smaller number...")
#         elif guess < ans:
#             print("Guess a larger number...")
#
#     print("Congratulations, you guessed the correct number!")
#
# guess(100)

## This function allows computer to guess user's number in mind
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        num = random.randint(low, high)
        print('Current number: {}'.format(num))
        feedback = input('Is the number too large (L)? Too small (S)? Or is it the correct answer (C)?').upper()
        if feedback == 'L' or feedback == 'l':
            high = num - 1
        elif feedback == 'S' or feedback == 's':
            low = num + 1
        else:
            print("Select 'S', 'B' or 'C' only!!! ")
    print('Congratulations, you have guessed the correct number !!!')

computer_guess(100)



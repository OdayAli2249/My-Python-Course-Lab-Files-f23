import random

# generate random number in scope from 1 to 20 and store the result in variable n
n = random.randrange(1, 20)
#print(n) for debuging

# variable where we store maximum number of wrong guesses
chancesNumber = 5
# we start with no wrong guesses, variable guessNumber represents that user has not guess any wrong number yet.
guessNumber = 0
# variable where we store the boundary length, a number if we exceed, then we are not even close to the right guess and vice versa.
margin = 5
# start taking the guesses one by one from user until he find the right guess or spend all the chances (lose)
while guessNumber < chancesNumber:
    num = input('guess the number between 1 and 20  \n')
    if(int(num) == n):
        # if number entered from user is the right number, we print the result and finish the process / program
        print('you win!')
        exit()
    # we print hint for user to improve the guesses (whether he is too high or too low).
    elif(int(num) > n and int(num) - n > margin):
        print('too high')
    elif(int(num) < n and n - int(num) > margin):
        print('too low')
    else:
        print('close')
    # increase the guesses number, program do not see/excute this line of code unless the user win.
    # represent the lost is being approached and the condition that make loop continue may break
    guessNumber +=1

# we do not see/excute this line of code unless the loop has finished looping and the condition is broken (user has lost)
print('you lose!')
print('the number: ',n)
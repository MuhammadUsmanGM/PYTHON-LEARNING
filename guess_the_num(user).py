def comp_guess(x):
   low=1
   high=100
   import random
   print('Think a number between 1 to 100')
   while True:
    guess=random.randint(low,high)
    user_input=input(f'Is {guess} too high(h),too low(l),or correct(c): ').lower()
    if user_input=='h':
       high=guess-1
    elif user_input=='l':
       low=guess+1
    elif user_input=='c':
       print(f'Computer guessed your number correctly!')
       break
    else:
      print("Invalid input.Please enter 'h','l' or 'c': ")
if __name__=='__main__':
   comp_guess(56)
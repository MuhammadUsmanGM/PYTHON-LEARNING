def rand_num():
  import random
  try:
    number=random.randint(1,100)
    while True:
       guess=int(input('Guess a num between 1 to 100: '))
       if guess<number:
         print('To low,Guess higher')
       elif guess>number:
         print('To high,Guess low')
       elif guess==number:
         break
    print(f'Congrats,You guessed it,the num is {number}')
  except ValueError:
    print('invalid literal for int() with base 10')
  except Exception as e:
    print(f'NO you got an error which is {e}')
if __name__=='__main__':
     rand_num()
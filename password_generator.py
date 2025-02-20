import random
def pwd_generator():
  try:
    print('WElcome to Password Generator')
    Character='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'
    number=input('Enter Number of Password you want to generate: ')
    number=int(number)
    lenght=input('Enter Lenght of your password(s): ')
    lenght=int(lenght)
    print('\nHere is your Password(s)')
    for pwd in range(number):
      passwords=''
      for c in range(lenght):
        passwords += random.choice(Character)
      print(passwords)
    print('Hope You got the Strong ones.😊')
  except Exception as e:
    print(f'You got an error which is {e}')
if __name__=='__main__':
    pwd_generator()
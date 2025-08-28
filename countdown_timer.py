import time
import os
def countdown(t):
  while t:
    mins,secs= divmod(t, 60)
    timer='{:02d}:{:02d}'.format(mins,secs)
    print(f'\r{timer}',end=' ')
    time.sleep(1)
    t -= 1
  print('\rTimer Completed')
if __name__=='__main__':
  while True:
    try:
      t=int(input('Enter time in sec: '))
      break
    except ValueError:
      print('Invalid Input.Please enter a number.')
  countdown(t)
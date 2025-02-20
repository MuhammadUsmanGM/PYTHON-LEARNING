import random
def play():
  user_score=0
  computer_score=0
  while True:
   user=input("Enter 'r' for rock 'p' for paper 's' for sicissor or 'q' to quit: ").lower()
   if user not in ['r','p','s','q']:
    print("Invalid choice. Please enter 'p','r' or 's'.")
   computer=random.choice(['r','p','s'])
   if user=='r' or user=='p' or user=='s':
    print(f'Computer choice:{computer}')
   elif user=='q':
    print('Thanks')
   if user==computer:
     print('Tie')
   elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
     print('You Won!')
     user_score+=1
     print(f'{user.upper()} beats {computer.upper()}')
   elif user=='q':
    print(f'Your score:{user_score}')
    print(f'Computer score:{computer_score}')
    if user_score>computer_score:
      print('You won it')
    elif user_score<computer_score:
      print('Computer won this round')
    print('Hope you enjoyed it. Play Again!')
    break
   elif (computer=='r' and user=='s') or (computer=='s' and user=='p') or (computer=='p' and user=='r'):
       print('You lost!')
       print(f'{computer.upper()} beats {user.upper()}')
       computer_score+=1
if __name__=='__main__':
      play()
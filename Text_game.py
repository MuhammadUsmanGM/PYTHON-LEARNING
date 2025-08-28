import random
def game():
    inventory=[]
    health=100
    while True:
      user_input=input('Enter the location(Forest,river or cave) you wanna go or\n q to quit the game: ')
      if user_input.lower()=='q':
         print(f'Inventory:{inventory}')
         break
      if user_input.lower()=='forest':
         print('You are in the forest right now')
         print('You face a lion in here.You wanna fight with lion.')
         print('If you will fight with lion hope you will get something precious.')
         lion=input("Enter 'y' for yes and 'n' for no: ")
         if lion.lower()=='y':
            print('You are fighting with the lion')
            damage=random.randint(1,100)
            health-=damage
            if health<=0:
               print('You Died')
               print('You lost your Inventory.')
               print('Sometimes taking risk leads you to death')
               break
            print(f'Remaining Health:{health}')
            print('Ooo!As hoped you found something after defeating lion.')
            print("It's a Glowing Crystal.You wanna collect it.")
            crystal=input("Enter 'y' for yes and 'n' for no: ")
            if crystal.lower()=='y':
              inventory.append('Glowing Crystal')
              print('Glowing Crystal added in your inventory')
              continue
            else:
              print('If you want something you have to take risk.')
              print('Hope next time you choose to fight and take risk.')
              pass
      elif user_input.lower()=='river':
         print('You are in a river.Water is a little bit cold.')
         print("There's a crocodile in water.You wanna fight with crocodile.")
         crocodile=input("Enter 'y' for yes and 'n' for no: ")
         print('You are fighting with a crocodile.')
         if crocodile.lower()=='y':
            damage=random.randint(0,100)
            health-=damage
            if health<=0:
              print('You Died')
              print('You lost your Inventory.')
              print('Sometimes taking risk leads you to death')
              break
            print(f'Remaining Health:{health}')
            print("Your foot is on something.Its a valuable pearl.nYou wanna collect the pearl.")
            water=input("Enter 'y' for yes and 'n' for no:")
            if water.lower()=='y':
              inventory.append('Valuable Pearl')
              print('Valuable Pearl added in your inventory.')
            continue
         else:
            print('If you want something you have to take risk.')
            print('Hope next time you choose to fight and take risk.')
            pass
      elif user_input.lower()=='cave':
         print("You are in a cave.There's dark in here.")
         print("There's a bear in the cave.It may be wild.You wanna fight with bear.")
         bear=input("Enter 'y' for yes and 'n' for no:")
         if bear.lower()=='y':
            print('You are having a fight with bear.')
            damage=random.randint(0,100)
            health-=damage
            if health<=0:
              print('You Died')
              print('You lost your Inventory.')
              print('Sometimes taking risk leads you to death')
              break
            print(f'Remaining Health:{health}')
            print("You found something.It's a piece of gold in here.You wanna collect it.")
            gold=input("Enter 'y' for yes and 'n' for no: ")
            if gold.lower()=='y':
              inventory.append('Gold Bar')
            print('Gold Bar added in your inventory.')
            continue
         else:
             print('If you want something you have to take risk.')
             print('Hope next time you choose to fight and take risk.')
             pass
      else:
         print('Invalid Choice.Please select an available location to enter the game.')   
if __name__=="__main__":
     game()
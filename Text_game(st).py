import random
import streamlit as st
def game():
    inventory=[]
    st.write('Your Inventory=[]')
    health=100
    st.write('Your Health=100')
    while True:
      user_input=st.text_input('Enter a location:"Forest" , "River" , "Cave" :',key="location_input")
      if user_input.lower()=='q':
         st.write(f'Inventory:{inventory}')
         break
      elif user_input.lower()=='forest':
         st.write('You are in the forest right now')
         st.write('You face a lion in here.You wanna fight with lion.')
         st.write('If you will fight with lion hope you will get something precious.')
         lion=st.text_input("Enter 'y' for yes and 'n' for no: ",key="lion_input")
         if lion.lower()=='y':
            st.write('You are fighting with the lion')
            damage=random.randint(1,100)
            health-=damage
            if health<=0:
               st.write('You Died')
               st.write('You lost your Inventory.')
               st.write('Sometimes taking risk leads you to death')
               break
            st.write(f'Remaining Health:{health}')
            st.write('Ooo!As hoped you found something after defeating lion.')
            st.write("It's a Glowing Crystal.You wanna collect it.")
            crystal=st.text_input("Enter 'y' for yes and 'n' for no: ",key="crystal_input")
            if crystal.lower()=='y':
              inventory.append('Glowing Crystal')
              st.write('Glowing Crystal added in your inventory')
              continue
            elif lion.lower()==' n':
              st.write('If you want something you have to take risk.')
              st.write('Hope next time you choose to fight and take risk.')
              pass
            else:
               st.write('Invalid Choice')
               pass
      elif user_input.lower()=='river':
         st.write('You are in a river.Water is a little bit cold.')
         st.write("There's a crocodile in water.You wanna fight with crocodile.")
         crocodile=st.text_input("Enter 'y' for yes and 'n' for no: ",key="crocodile_input")
         if crocodile.lower()=='y':
            st.write('You are fighting with a crocodile.')
            damage=random.randint(0,100)
            health-=damage
            if health<=0:
              st.write('You Died')
              st.write('You lost your Inventory.')
              st.write('Sometimes taking risk leads you to death')
              break
            st.write(f'Remaining Health:{health}')
            st.write("Your foot is on something.Its a valuable pearl.nYou wanna collect the pearl.")
            water=st.text_input("Enter 'y' for yes and 'n' for no:",key="water_input")
            if water.lower()=='y':
              inventory.append('Valuable Pearl')
              st.write('Valuable Pearl added in your inventory.')
            continue
         elif crocodile.lower()=='n':
            st.write('If you want something you have to take risk.')
            st.write('Hope next time you choose to fight and take risk.')
            pass
         else:
               st.write('Invalid Choice')
               pass
      elif user_input.lower()=='cave':
         st.write("You are in a cave.There's dark in here.")
         st.write("There's a bear in the cave.It may be wild.You wanna fight with bear.")
         bear=st.text_input("Enter 'y' for yes and 'n' for no:",key="bear_input")
         if bear.lower()=='y':
            st.write('You are having a fight with bear.')
            damage=random.randint(0,100)
            health-=damage
            if health<=0:
              st.write('You Died')
              st.write('You lost your Inventory.')
              st.write('Sometimes taking risk leads you to death')
              break
            st.write(f'Remaining Health:{health}')
            st.write("You found something.It's a piece of gold in here.You wanna collect it.")
            gold=st.text_input("Enter 'y' for yes and 'n' for no: ",key="gold_input")
            if gold.lower()=='y':
              inventory.append('Gold Bar')
            st.write('Gold Bar added in your inventory.')
            continue
         elif bear.lower()=='n':
             st.write('If you want something you have to take risk.')
             st.write('Hope next time you choose to fight and take risk.')
             pass
         else:
               st.write('Invalid Choice')
               pass
      else:
         st.write('Invalid Choice.Please select an available location to enter the game.') 

def new_func():
    st.session_state  
if __name__=="__main__":
     game()
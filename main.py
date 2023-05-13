from rappers_list import rappers
import random
# ask user if they want 8 16 32 bracket
# make randomizer to get x amount of rappers in bracket
# make 'while' function that loops till winner
# print winner is the winner!!!
# ask them pick 1 or 2 for their choice
def main():
  print('Welcome to the Rapper Tournament!\n')
  bracket_size = int(input('How big do you want the bracket: 8, 16, or 32 people? '))
  while bracket_size != 8 and bracket_size != 16 and bracket_size != 32:
    bracket_size = int(input('Sorry, you must pick a size of 8, 16 or 32:  '))
  
  # making each rounds bracket 
  round_32_bracket = []
  round_16_bracket = []
  quarters_bracket = []
  semis_bracket = []
  finals_bracket = []
  winner = []

  # list used for checking which rapper has been added to the bracket already
  nums_used = []
  

  # helper function for randomizing starting bracket
  def get_number(nums_used):
    random1 = str(random.randint(0,31))
    # avoiding duplicate choices by checking which selections have been added already
    while random1 in nums_used:
      random1 = str(random.randint(0,31))
  
    random2 = str(random.randint(0,31))
    while random2 in nums_used or random2 == random1:
      random2 = str(random.randint(0,31))
      
    nums_used.append(random1)
    nums_used.append(random2)
    return int(random1), int(random2)
    
  # looping to make the first bracket 
  for i in range(bracket_size//2):
      
      if bracket_size == 8:
        random1,random2 = (get_number(nums_used))
        quarters_bracket.append(rappers[random1])
        quarters_bracket.append(rappers[random2])
      if bracket_size == 16:
        random1,random2 = (get_number(nums_used))
        round_16_bracket.append(rappers[random1])
        round_16_bracket.append(rappers[random2])
      if bracket_size == 32:
        random1,random2 = (get_number(nums_used))
        round_32_bracket.append(rappers[random1])
        round_32_bracket.append(rappers[random2])
  
  print('Bracket Generated!')

  
  # helper function for similulating each round
  def bracket_advance(bracket_size,round,nextround,bracket,next_bracket):
    for i in range(0,bracket_size,2):
        a = int(input(f'\n{round}: {bracket[i]} vs {bracket[i+1]} \nPress 1 or 2 to pick your choice! '))
        while a != 1 and a!= 2:
          a = int(input('MUST PRESS 1 OR 2 TO PICK: '))
        next_bracket.append(bracket[i + a -1])
    if len(next_bracket) == 1:
      return next_bracket[0]
    print(f'\n{nextround}')
      # returning the next bracket with the previous bracket winners
    return next_bracket


  # main loop that similuates until the winner is picked
  while True:
    if bracket_size == 32:
      round_16_bracket = bracket_advance(32,'Round 32','ROUND OF 16',round_32_bracket,round_16_bracket)
      quarters_bracket = bracket_advance(16,'Round 16','QUARTER FINALS',round_16_bracket,quarters_bracket)
      semis_bracket = bracket_advance(8,'Quarter-Final','SEMI FINALS',quarters_bracket,semis_bracket)
      finals_bracket = bracket_advance(4,'Semis','FINAL ROUND!!!',semis_bracket,finals_bracket)
      winner = bracket_advance(2,'Finals','',finals_bracket,winner)
      
      print(f'\nCongrats! {winner} is the winner of your tournament!')
      break
      
    if bracket_size == 16:
      quarters_bracket = bracket_advance(16,'Round 16','QUARTER FINALS',round_16_bracket,quarters_bracket)
      semis_bracket = bracket_advance(8,'Quarter-Final','SEMI FINALS',quarters_bracket,semis_bracket)
      finals_bracket = bracket_advance(4,'Semis','FINAL ROUND!!!',semis_bracket,finals_bracket)
      winner = bracket_advance(2,'Finals','',finals_bracket,winner)
      
      print(f'\nCongrats! {winner} is the winner of your tournament!')
      break

    if bracket_size == 8:
      semis_bracket = bracket_advance(8,'Quarter-Final','SEMI FINALS',quarters_bracket,semis_bracket)
      finals_bracket = bracket_advance(4,'Semis','FINAL ROUND!!!',semis_bracket,finals_bracket)
      winner = bracket_advance(2,'Finals','',finals_bracket,winner)
      
      print(f'\nCongrats! {winner} is the winner of your tournament!')
      break
  
main()

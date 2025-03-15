import art
import random
import game_data
from replit import clear

score = 0
score1 = 0

def header():
  if score1 == 0:
    hd = f"You're right! Current score: {score}."
    return hd
  elif score1 > 0:
    hd = f"You're wrong! Current score: {score}."
    return hd


decii = "" 
stat = True

while stat:

  winner = ""

  personnality1 = random.choice(game_data.data)
  personnality2 = random.choice(game_data.data)

  clear()

  print(personnality1['follower_count'])
  print(personnality2['follower_count'])

  print(art.logo)

  if score > 0:
   print(header())
  
  print(f"Compare A: {personnality1['name']}, a {personnality1['description']}, from {personnality1['country']}.")
    
  print(art.vs)
    
  print(f"Compare B: {personnality2['name']}, a {personnality2['description']}, from {personnality1['country']}.")
    
  decision = input("Who has more followers? Type 'A' or 'B': ") .lower()
      
  if personnality1['follower_count'] > personnality2['follower_count']:
    winner = "a"
  elif personnality2['follower_count'] > personnality1['follower_count']:
    winner = "b"
        
  if decision == winner:
    score += 1
    score1 += 1
    score1 -= 1
  elif decision != winner:
    score1 += 1
   
  decii += decision
  
  if decision != winner or personnality1['name'] == personnality2['name']:
    stat = False

    clear()

    print(art.logo)
    print(header())
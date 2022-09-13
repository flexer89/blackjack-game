import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
def deal_cards(cards):
  '''Returns randomly picked card'''
  index = random.randint(0,len(cards)-1)
  return cards[index]

def overflow_check(score):
  if score > 21:
    return "You have black"
  elif score == 21:
    return "You have blackjack!"
  else:
    return "underflow"

def print_result(cards,score,who):
  print(f"{who} final hand: {cards}, final score: {score}")

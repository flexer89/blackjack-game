import functions

print(functions.logo)
decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
computer_cards = []
user_cards = []
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_score = 0
computer_score = 0
computer_first_card = 0
continue_playing = "y"
  
user_cards.append(cards[functions.deal_cards(cards)])  
computer_cards.append(cards[functions.deal_cards(cards)])
computer_cards.append(cards[functions.deal_cards(cards)])

while continue_playing=="y":
  user_cards.append(cards[functions.deal_cards(cards)])
  user_score = sum(user_cards)
  computer_score = sum(computer_cards)
  
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
    
  if user_score == 21:
    functions.print_result(user_cards,user_score,"Your")
    functions.print_result(computer_cards,computer_score,"Computer's")
    print("Win! You have blackjack.")
    quit()
  elif computer_score == 21:
    functions.print_result(user_cards,user_score,"Your")
    functions.print_result(computer_cards,computer_score,"Computer's")
    print("You lose! Opponent has blackjack.")
    quit()
  if user_score > 21:
    if 11 in user_cards:
      user_cards[user_cards.index(11)]=1
      if user_score > 21:
        functions.print_result(user_cards,user_score,"Your")
        functions.print_result(computer_cards,computer_score,"Computer's")
        print("You lose!")
        quit()
    else:
      functions.print_result(user_cards,user_score,"Your")
      functions.print_result(computer_cards,computer_score,"Computer's")
      print("You lose!")
      quit()
  continue_playing = input("Type 'y' to get another card, type 'n' to pass:").lower()
while computer_score < 17:
  computer_cards.append(cards[functions.deal_cards(cards)])
  computer_score = sum(computer_cards)
if computer_score > 21:
  functions.print_result(user_cards,user_score,"Your")
  functions.print_result(computer_cards,computer_score,"Computer's")
  print("You win!")
  
else:
  if user_score > computer_score:
    functions.print_result(user_cards,user_score,"Your")
    functions.print_result(computer_cards,computer_score,"Computer's")
    print("You win!")
  elif user_score == computer_score:
    functions.print_result(user_cards,user_score,"Your")
    functions.print_result(computer_cards,computer_score,"Computer's")
    print("Draw")
  else:
    functions.print_result(user_cards,user_score,"Your")
    functions.print_result(computer_cards,computer_score,"Computer's")
    print("Computer wins!")
      
    
  
# Blackjack game

## Description

Blackjack, also known as 21 is one of the most popular casino card games.
In Blackjack, everyone plays against the dealer. Your goal is to draw cards with a value as close to 21 as possible without going over.

### How do you beat the dealer?

- By drawing a hand value that is higher than the dealer’s hand value
- By the dealer drawing a hand value that goes over 21.
- By drawing a hand value of 21 on your first two cards, when the dealer does not.

### How do you lose to the dealer? 

- Your hand value exceeds 21.
- The dealers hand has a greater value than yours at the end of the round


## Example Input

```

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Do you want to play a game of Blackjack? Type 'y' or 'n':y
Your cards: [10, 6], current score: 16
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass:
```

## Example Output

```
Your cards: [10, 6, 5], current score: 21
Computer's first card: 10
Your final hand: [10, 6, 5], final score: 21
Computer's final hand: [10, 10], final score: 20
Win! You have blackjack.
```

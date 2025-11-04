# BlackJack game written in Python
My first project **written by myself**, since the AI became free for everyone to use.

> Note that it's only in hungarian right now, and I don't prioritize translating the game!

It's still a work in progress, yet I'll document everything I did here.

## How to play
I made a minimal choice system in the game, the first thing the user sees is the choice to play, or exit the game.

The map of choices: Play? &rarr; [1] &rarr; Write the bet you want to play with! &darr;

| Action | Command |
|--------|---------|
| Stand  | s       |
| Hit    | h       |

## Project progress
As of now, these are the completed functions, and solved issues:

- **Drawing an ace:** The code sums the players hand, and decides, whether it has to decrease its value to 1, or can keep it at 11.
- **Having all the cards in 2 decks:** The easiest way for me, was using a list of `kartyak = []` (kártyák is cards in hungarian), and multiplying it with 4 *(since in a French deck, we have quadruplets of every value)*, and 2 *(for the double-deck)*, so the code then makes exactly 8 variations of every single card.
- **"Shuffling" the deck:** I used the `random.choice()` function to draw a random card. That is why it's a "pun intended" shuffle.
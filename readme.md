# 🎴 BlackJack Python Game - Complete Documentation

A console-based BlackJack (21) card game implementation in Python with colorful terminal output and a complete betting system.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Game Rules](#game-rules)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)
- [Technical Implementation](#technical-implementation)
- [Getting Started](#getting-started)

---

## 🎯 Overview

This is a fully functional BlackJack game written in Python that runs in the terminal. The game implements classic BlackJack rules with a betting system, dealer AI, and colorful visual feedback using the `colorama` library. Players start with 5000 Ft (Hungarian Forint) and can play rounds by placing bets until they run out of money.

**Languages:** The game interface is currently in Hungarian, but the core gameplay follows standard BlackJack rules.

---

## ✨ Features

### Core Gameplay
- 🃏 **Double Deck System** - Uses 2 standard 52-card decks (104 cards total)
- 💰 **Betting System** - Start with 5000 Ft, minimum bet of 10 Ft (must be divisible by 10)
- 🎨 **Color-Coded Output** - Green for wins, red for losses
- 🤖 **Dealer AI** - Dealer follows standard rules (must draw until 17+)
- 🎲 **Random Card Drawing** - Cards are randomly selected from the deck

### Game Mechanics
- ♠️ **Ace Handling** - Aces automatically adjust between 11 and 1 to prevent busting
- 🎰 **BlackJack Bonus** - Natural BlackJack (Ace + 10-value card) pays 1.5x
- 🤝 **Push Detection** - Ties return the bet to the player
- 💥 **Bust Detection** - Automatically detects when player or dealer exceeds 21

### Player Actions
- **Hit (h)** - Draw another card
- **Stand (s)** - Keep current hand and let dealer play

---

## 📖 Game Rules

### Objective
Get as close to 21 as possible without going over, while beating the dealer's hand.

### Card Values
- **Number cards (2-9)**: Face value
- **Face cards (J, Q, K)**: Worth 10 points
- **Aces (A)**: Worth 11 points, automatically converts to 1 if hand exceeds 21

### Winning Conditions
1. **BlackJack**: Starting hand of Ace + 10-value card (pays 1.5x bet)
2. **Win**: Hand value closer to 21 than dealer without busting
3. **Dealer Bust**: Dealer exceeds 21 (you win your bet)
4. **Push**: Same value as dealer (bet is returned)

### Losing Conditions
1. **Bust**: Your hand exceeds 21 (lose bet)
2. **Dealer Wins**: Dealer's hand is closer to 21 than yours

---

## 🎮 How It Works

### Game Flow

#### 1. **Initial Menu**
```
[1] Játék (Play)
[0] Kilepes (Exit)
```
- Choose option 1 to start playing
- Choose option 0 to exit the game

#### 2. **Placing a Bet**
- You're shown your current balance (starts at 5000 Ft)
- Enter your bet amount (minimum 10 Ft, must be divisible by 10)
- Bet cannot exceed your current balance

#### 3. **Initial Deal**
- You receive 2 cards (both visible)
- Dealer receives 2 cards (only 1 visible)
- Your hand total is calculated and displayed

#### 4. **Player's Turn**
Display shows:
```
Nalad: [cards] (total)
Osztonal: [dealer's first card]
```

Available actions:
- **h (Hit)**: Draw another card
  - If you bust (>21), you lose immediately
  - Can hit multiple times until bust or stand
- **s (Stand)**: End your turn and proceed to dealer's turn

#### 5. **Dealer's Turn** (after you stand)
- Dealer reveals hidden card
- Dealer **must** draw cards until reaching 17 or higher
- Display updates showing each card drawn

#### 6. **Round Resolution**
The game compares hands and determines the outcome:
- **BlackJack**: Win 1.5x bet (only if initial 2 cards = Ace + 10)
- **Win**: Win 1x bet
- **Push**: Bet returned (tie)
- **Lose**: Lose bet amount
- **Dealer Bust**: Win 1x bet

#### 7. **Continue or End**
- Game continues to next round if you have ≥10 Ft
- **Game Over** when balance drops below 10 Ft

---

## 🏗️ Code Structure

### Global Variables

```python
kartyak = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 8  # Double deck (104 cards)
kez = []        # Player's hand
oszto = []      # Dealer's hand
penz = 5000     # Player's money (starting balance)
```

### Key Functions

#### `zoldpr(text)` & `pirospr(text)`
- **Purpose**: Print colored text to terminal
- **zoldpr**: Prints text in green (for wins/gains)
- **pirospr**: Prints text in red (for losses)
- **Uses**: `colorama` library's Fore and Style

#### `huzas()`
- **Purpose**: Draw a random card from the deck
- **Process**:
  1. Randomly selects a card from `kartyak` list
  2. Converts face cards (J, Q, K) to value 10
  3. Converts Ace (A) to value 11
  4. Removes card from deck
  5. Returns the card's numeric value
- **Return**: Integer value of drawn card

#### `ace()`
- **Purpose**: Automatically adjust Ace values to prevent busting
- **Process**:
  1. Checks if player has any Aces (value 11) in hand
  2. If hand total exceeds 21, converts first Ace from 11 to 1
  3. Modifies the `kez` list directly
- **Smart Feature**: Only converts when necessary to avoid bust

#### `check()`
- **Purpose**: Determine round outcome and update player's balance
- **Evaluates**:
  1. Both dealer bust and player bust/21+
  2. Dealer stands (17+) vs player value
  3. BlackJack detection (natural 21)
  4. Push (tie) scenarios
  5. Standard win/loss conditions
- **Updates**: `penz` variable with winnings/losses
- **Display**: Shows final hands and outcome message

---

## 🔧 Technical Implementation

### Deck Management
```python
kartyak = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 8
```
- Single deck: 13 card values × 4 suits = 52 cards
- **Multiplied by 8**: 4 (for suits) × 2 (for double deck) = 8 copies of each value
- Total: 104 cards in play

### Random Card Drawing
- Uses `random.choice()` to select cards
- Selected card is removed from deck using `.pop()`
- Ensures no card duplication within a session

### Ace Logic
The game implements intelligent Ace handling:
```python
if 11 in kez:
    kezertek = sum(kez)
    if kezertek > 21:
        # Convert first Ace from 11 to 1
        for i, x in enumerate(kez):
            if x == 11:
                kez[i] = 1
```
- Aces start at 11 points
- Automatically converts to 1 when player would bust
- Only converts one Ace at a time as needed

### Dealer AI
```python
while osztoertek < 17:
    huzott = huzas()
    oszto.append(huzott)
    osztoertek = sum(oszto)
```
- Follows casino rules: dealer must hit on 16 or less
- Dealer must stand on 17 or higher
- No decision-making, purely rule-based

### User Interface
- Uses `os.system('cls')` to clear screen between actions
- `time.sleep()` adds dramatic pauses for better UX
- Color coding via `colorama`:
  - **Green**: Positive outcomes (wins, gains)
  - **Red**: Negative outcomes (losses, game over)

### Betting System
```python
if tet >= 10 and tet % 10 == 0 and tet <= penz:
    # Process bet
```
Validation checks:
1. Minimum bet: 10 Ft
2. Must be divisible by 10
3. Cannot exceed current balance

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- `colorama` library

### Installation
```bash
# Install colorama
pip install colorama

# Clone the repository
git clone https://github.com/garbaiii/BlackJack-Python.git

# Navigate to directory
cd BlackJack-Python

# Run the game
python main.py
```

### First Game
1. Run `python main.py`
2. Enter `1` to start playing
3. Place your first bet (try `100`)
4. Type `h` to hit, `s` to stand
5. Try to beat the dealer and win money!

---

## 🎓 Learning Highlights

### What Was Implemented

1. **Card Deck System**: Created a realistic double-deck system with proper card distribution
2. **Game Logic**: Implemented all BlackJack rules including bust, stand, and BlackJack detection
3. **Ace Intelligence**: Built automatic Ace value adjustment to optimize player's hand
4. **Dealer AI**: Created a rule-based dealer that follows casino standards
5. **Betting Economics**: Designed a complete betting system with validation
6. **User Experience**: Added color coding and timing for better gameplay feel
7. **Edge Case Handling**: Covered scenarios like dealer bust, push, and natural BlackJack

### Code Techniques Used
- **Lists**: For storing cards and hand values
- **Random Library**: For card shuffling simulation
- **Conditional Logic**: For game rule implementation
- **Loops**: For continuous gameplay and dealer drawing
- **Functions**: For code organization and reusability
- **Global Variables**: For game state management
- **String Formatting**: For displaying game information
- **External Libraries**: colorama for enhanced terminal output

---

## 🎉 Conclusion

This BlackJack implementation demonstrates a complete understanding of:
- Game logic and rule implementation
- User input handling and validation
- State management in a turn-based game
- Visual feedback and user experience
- Python fundamentals (lists, functions, conditionals, loops)

The game is fully playable and includes all essential BlackJack features, making it a solid first project that combines programming concepts with game design!

---

**Note**: Game text is in Hungarian. Future updates may include English localization.

**Game Over Condition**: When balance drops below 10 Ft, the game ends with a "GAME OVER" message.

**Enjoy playing! 🎰**

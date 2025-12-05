# Number Guessing Game 猜數字遊戲

## 🎯 Game Description
Classic number guessing game! The computer picks a random number, and you try to guess it with hints of "higher" or "lower".

## 🎮 How to Play
1. Computer picks a random number (1-100)
2. Enter your guess
3. Get a hint: "Too High!" or "Too Low!"
4. Keep guessing until you find the number
5. Try to guess in as few attempts as possible!

## 💻 Technologies Used
- **HTML** - Page structure
- **CSS** - Clean styling
- **JavaScript** - Game logic

## 📝 Key JavaScript Concepts

### Generate Random Number
```javascript
let secretNumber = Math.floor(Math.random() * 100) + 1;
```

### Comparison Logic
```javascript
if (guess === secretNumber) {
    message = 'Correct! 🎉';
} else if (guess < secretNumber) {
    message = 'Too Low! ⬆️';
} else {
    message = 'Too High! ⬇️';
}
```

### Tracking Attempts
```javascript
let attempts = 0;
attempts++;  // Increment each guess
```

### Reset Game
```javascript
function resetGame() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    input.value = '';
}
```

## 🌟 Learning Objectives
- Random number generation
- Comparison operators (`<`, `>`, `===`)
- Counting with increment (`++`)
- Reset/restart functionality

## 🔧 Customization Ideas
- Change the number range
- Add maximum attempts limit
- Show guess history
- Add difficulty levels

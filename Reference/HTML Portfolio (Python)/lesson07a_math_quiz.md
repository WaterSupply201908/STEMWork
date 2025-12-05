# Math Quiz Game 數學測驗遊戲

## 🎯 Game Description
A fun math quiz game that tests your addition, subtraction, and multiplication skills!

## 🎮 How to Play
1. A math problem appears on screen (e.g., `5 + 3 = ?`)
2. Type your answer in the input box
3. Press Enter or click Submit
4. Get instant feedback - Correct ✓ or Wrong ✗
5. Try to get the highest score!

## 💻 Technologies Used
- **HTML** - Page structure
- **CSS** - Styling and animations
- **JavaScript** - Game logic

## 📝 Key JavaScript Concepts

### Random Number Generation
```javascript
let a = Math.floor(Math.random() * 12) + 1;  // Random 1-12
```

### Operators Array
```javascript
const operators = ['+', '-', '×'];
let operator = operators[Math.floor(Math.random() * 3)];
```

### Calculate Answer
```javascript
if (operator === '+') answer = a + b;
else if (operator === '-') answer = a - b;
else answer = a * b;
```

### Event Listener for Enter Key
```javascript
input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        checkAnswer();
    }
});
```

## 🌟 Learning Objectives
- Generate random numbers with `Math.random()`
- Use arrays to store options
- Handle user input with event listeners
- Update DOM elements dynamically
- Track score with variables

## 🔧 Customization Ideas
- Add division problems
- Increase number range for harder problems
- Add a timer for speed challenge
- Add difficulty levels (Easy/Medium/Hard)

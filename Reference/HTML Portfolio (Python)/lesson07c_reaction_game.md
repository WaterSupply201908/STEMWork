# Reaction Game 反應遊戲

## 🎯 Game Description
Test your reaction speed! Wait for the circle to turn green, then click as fast as you can!

## 🎮 How to Play
1. Click the "START" button
2. Wait for the red circle to appear...
3. When it turns GREEN, click it immediately!
4. Your reaction time is measured in milliseconds
5. Try to beat your best time!

## 💻 Technologies Used
- **HTML** - Page structure
- **CSS** - Circle styling and animations
- **JavaScript** - Timing and measurement

## 📝 Key JavaScript Concepts

### setTimeout for Random Delay
```javascript
setTimeout(() => {
    circle.style.background = '#2ecc71';  // Green
    startTime = Date.now();
}, Math.random() * 3000 + 2000);  // 2-5 seconds
```

### Measuring Time
```javascript
let startTime = Date.now();

// When clicked:
let reactionTime = Date.now() - startTime;
```

### Conditional Messages
```javascript
let message;
if (time < 200) message = 'Amazing! 🏆';
else if (time < 300) message = 'Good! 👍';
else if (time < 500) message = 'Average';
else message = 'Keep trying!';
```

### Click Event on Element
```javascript
circle.onclick = function() {
    // Check if green before counting
    if (circle.style.background === 'rgb(46, 204, 113)') {
        // Calculate time
    }
};
```

## 🌟 Learning Objectives
- Use `Date.now()` for precise timing
- `setTimeout()` for delayed actions
- Random delays with `Math.random()`
- Conditional logic for feedback

## 🔧 Customization Ideas
- Add multiple rounds and average time
- Add a leaderboard
- Make the circle move to random positions
- Add sound effects

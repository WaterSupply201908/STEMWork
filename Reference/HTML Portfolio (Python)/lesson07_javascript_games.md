# Lesson 7: JavaScript Games

## 🎯 Learning Objectives
- Create HTML/JavaScript games from scratch
- Learn JavaScript: variables, functions, events, DOM
- Embed games in Flask using iframes

---

## 📁 Sub-Lessons

| Lesson | Game | Focus |
|--------|------|-------|
| **7a** | 🧮 Math Quiz | Random numbers, user input, score tracking |
| **7b** | ⚡ Reaction Game | setTimeout, Date timing, click events |
| **7c** | 🎨 Color Game | Arrays, timer countdown, color matching |

---

## 📝 Lesson 7a: Math Quiz

### What Students Learn
- Generate random numbers with `Math.random()`
- Get user input from `<input>` fields
- Check answers with `if/else`
- Track score with variables

### Key JavaScript
```javascript
// Random number 1-10
let a = Math.floor(Math.random() * 10) + 1;

// Get user input
let answer = parseInt(document.getElementById('answer').value);

// Check answer
if (answer === correct) {
    score++;
    alert('Correct! 🎉');
}
```

### File: `static/games/math_quiz.html`
### Route: `/play/math-quiz`

---

## 📝 Lesson 7b: Reaction Game

### What Students Learn
- Use `setTimeout()` for delays
- Measure time with `Date.now()`
- Handle click events
- Change element styles dynamically

### Key JavaScript
```javascript
// Random delay 2-5 seconds
setTimeout(() => {
    circle.style.background = '#2ecc71';  // Turn green
    startTime = Date.now();
}, Math.random() * 3000 + 2000);

// Calculate reaction time
circle.onclick = () => {
    const reactionTime = Date.now() - startTime;
    message.textContent = `${reactionTime}ms`;
};
```

### File: `static/games/reaction_game.html`
### Route: `/play/reaction-game`

---

## 📝 Lesson 7c: Color Game

### What Students Learn
- Use arrays to store data
- Create countdown timer with `setInterval()`
- Compare strings (word vs color)
- Game over logic

### Key JavaScript
```javascript
// Color arrays
const colors = ['RED', 'BLUE', 'GREEN', 'YELLOW'];
const colorCodes = {'RED': '#ff0000', 'BLUE': '#0000ff', ...};

// Timer countdown
let timer = setInterval(() => {
    time--;
    if (time === 0) {
        clearInterval(timer);
        alert('Game Over!');
    }
}, 1000);

// Check if word matches color
correct = (word === color);
```

### File: `static/games/color_game.html`
### Route: `/play/color-game`

---

## 🎮 All Games Summary

| Lesson | Game | File | Route |
|--------|------|------|-------|
| 7a | Math Quiz | `math_quiz.html` | `/play/math-quiz` |
| 7b | Reaction Game | `reaction_game.html` | `/play/reaction-game` |
| 7c | Color Game | `color_game.html` | `/play/color-game` |

Plus 4 Vercel games from Lesson 6b:
- Whack-a-Mole, Fireworks, Star Fall, King & Pigs

**Total: 7 playable games!**

---

## 📖 Game Documentation

See `static/games/` folder:
- `math_quiz.md` - Full Math Quiz documentation
- `reaction_game.md` - Full Reaction Game documentation
- `color_game.md` - Full Color Game documentation

---

## ✅ Checklist

### After 7a:
- [ ] `math_quiz.html` created
- [ ] `/play/math-quiz` route works
- [ ] Score updates correctly

### After 7b:
- [ ] `reaction_game.html` created
- [ ] `/play/reaction-game` route works
- [ ] Reaction time displays

### After 7c:
- [ ] `color_game.html` created
- [ ] `/play/color-game` route works
- [ ] Timer counts down
- [ ] All 7 games playable!

---

## 🔗 Next Lesson
**Lesson 8: Parent Dashboard** - Create a page for parents showing skills and statistics

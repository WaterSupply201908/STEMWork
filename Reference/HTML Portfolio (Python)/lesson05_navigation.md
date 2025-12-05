# Lesson 5: Multi-Page Navigation System

## 🎯 Learning Objectives:
- Create 5 Flask routes
- Build consistent navigation
- Link all pages together

## 📝 What Students Build:

### 5 Routes:
```python
@app.route('/')                    # Home
@app.route('/projects')            # Projects
@app.route('/games')               # Games
@app.route('/parent-dashboard')    # Parents
@app.route('/about')               # About
```

### Navigation Bar (on every page):
```html
<nav class="navbar">
    <div class="logo">🎓 我的編程作品集</div>
    <ul class="nav-links">
        <li><a href="/">主頁 Home</a></li>
        <li><a href="/projects">作品 Projects</a></li>
        <li><a href="/games">遊戲 Games</a></li>
        <li><a href="/parent-dashboard">👨‍👩‍👧 家長專區</a></li>
        <li><a href="/about">關於我 About</a></li>
    </ul>
</nav>
```

## ✅ Deliverable:
- 5-page website
- Navigation works on all pages
- Consistent header/footer

## 🔗 Leads to:
Lesson 6 - Games page content

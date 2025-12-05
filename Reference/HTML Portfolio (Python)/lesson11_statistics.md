# Lesson 11: Statistics & Database Queries

## 🎯 Learning Objectives:
- Write COUNT queries
- Calculate statistics from database
- Display in visual cards
- Use statistics in multiple pages

## 📝 What Students Build:

### Database Queries:

**1. Count Total Projects:**
```python
c.execute('SELECT COUNT(*) FROM projects')
total = c.fetchone()[0]
# Result: 15
```

**2. Count Unique Categories:**
```python
c.execute('SELECT COUNT(DISTINCT category) FROM projects')
categories = c.fetchone()[0]
# Result: 4 (Python, Pygame, Tkinter, HTML/CSS)
```

**3. Count by Category:**
```python
c.execute('SELECT category, COUNT(*) FROM projects GROUP BY category')
by_category = c.fetchall()
```

### Display Statistics:

**Visual Cards:**
```html
<div class="game-card">
    <div class="game-header" style="font-size:64px;">15</div>
    <div class="game-content">
        <div class="game-title">完成的專案</div>
        <div class="game-desc">Projects Completed</div>
    </div>
</div>
```

### Used In:

**1. Home Page:**
- Featured statistics at bottom

**2. Parent Dashboard:**
- Detailed statistics section
- Shows 15 projects, 4 technologies, 120+ hours

**3. Projects Page:**
- "Total: 15 projects" display

## ✅ Deliverable:
- Statistics working in 3 pages
- Database queries tested
- Visual cards styled

## 💡 Key Concepts:
- SQL COUNT()
- SQL DISTINCT
- SQL GROUP BY
- Dynamic data display

## 🔗 Leads to:
Lesson 12 - Final integration!

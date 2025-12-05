# ============================================================
# LESSON 12: FINAL INTEGRATION
# ============================================================
# This is the complete portfolio combining all lessons 1-11
# 
# RUN: python lesson12_final_integration.py
# OPEN: http://127.0.0.1:5000
#
# For the full version with all Pygame games, see:
#   html_portfolio/FINAL_STEMWORK_WITH_GAMES_LOCAL.py
# ============================================================

from flask import Flask, render_template_string, send_from_directory
import sqlite3
import os

# ============================================================
# AUTO-TRANSLATION (from Lesson 9)
# ============================================================
try:
    from deep_translator import MyMemoryTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("⚠️  For translation: pip install deep-translator")

def translate(text):
    if not TRANSLATOR_AVAILABLE or not text:
        return text
    try:
        return MyMemoryTranslator(source='en-US', target='zh-TW').translate(text)
    except:
        return text

def t(text):
    return translate(text)

def b(text):
    chinese = translate(text)
    return f"{chinese} {text}" if chinese != text else text

# ============================================================
# FLASK APP SETUP
# ============================================================
app = Flask(__name__)

# Create static/games folder if not exists
os.makedirs('static/games', exist_ok=True)

# ============================================================
# CREATE JAVASCRIPT GAME FILES (from Lesson 7)
# ============================================================

MATH_QUIZ_HTML = """<!DOCTYPE html>
<html><head><title>Math Quiz</title><meta charset="UTF-8">
<style>body{font-family:Arial;text-align:center;padding:50px;background:#f0f0f0}
#game{background:white;padding:40px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.2);max-width:500px;margin:0 auto}
h1{color:#2c5aa0}#question{font-size:36px;margin:30px 0}
input{padding:15px;font-size:24px;width:200px;border:2px solid #2c5aa0;border-radius:8px}
button{padding:15px 40px;font-size:20px;background:#2c5aa0;color:white;border:none;border-radius:8px;cursor:pointer;margin-top:20px}
#score{font-size:24px;margin-top:20px;color:#2c5aa0}</style>
</head><body><div id="game"><h1>🧮 Math Quiz</h1>
<div id="question"></div><input type="number" id="answer" placeholder="Your answer"><br>
<button onclick="checkAnswer()">Submit</button><div id="score">Score: <span id="points">0</span></div></div>
<script>let score=0,a,b,op;
function newQuestion(){a=Math.floor(Math.random()*10)+1;b=Math.floor(Math.random()*10)+1;op=['+','-','×'][Math.floor(Math.random()*3)];document.getElementById('question').textContent=`${a} ${op} ${b} = ?`;document.getElementById('answer').value='';document.getElementById('answer').focus()}
function checkAnswer(){const answer=parseInt(document.getElementById('answer').value);let correct;if(op==='+')correct=a+b;else if(op==='-')correct=a-b;else correct=a*b;if(answer===correct){score++;document.getElementById('points').textContent=score;alert('Correct! 🎉')}else{alert(`Wrong! The answer was ${correct}`)}newQuestion()}
newQuestion()</script></body></html>"""

COLOR_GAME_HTML = """<!DOCTYPE html>
<html><head><title>Color Game</title><meta charset="UTF-8">
<style>body{font-family:Arial;text-align:center;padding:30px;background:#f0f0f0}
#game{background:white;padding:30px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.2);max-width:600px;margin:0 auto}
h1{color:#2c5aa0}#word{font-size:72px;font-weight:bold;margin:30px 0}
.btn{padding:20px 40px;margin:10px;font-size:24px;background:#2c5aa0;color:white;border:none;border-radius:8px;cursor:pointer}
#timer,#score{font-size:24px;margin:10px;color:#2c5aa0}</style>
</head><body><div id="game"><h1>🎨 Color Game</h1>
<div id="timer">Time: <span id="time">30</span>s</div><div id="score">Score: <span id="points">0</span></div>
<div id="word">RED</div><button class="btn" onclick="answer('yes')">Match ✓</button><button class="btn" onclick="answer('no')">No Match ✗</button></div>
<script>const colors=['RED','BLUE','GREEN','YELLOW','ORANGE','PURPLE','PINK'];
const colorCodes={'RED':'#ff0000','BLUE':'#0000ff','GREEN':'#00ff00','YELLOW':'#ffff00','ORANGE':'#ff8800','PURPLE':'#8800ff','PINK':'#ff00ff'};
let score=0,time=30,correct,timer;
function newRound(){const word=colors[Math.floor(Math.random()*colors.length)];const color=colors[Math.floor(Math.random()*colors.length)];correct=word===color;document.getElementById('word').textContent=word;document.getElementById('word').style.color=colorCodes[color]}
function answer(choice){if((choice==='yes'&&correct)||(choice==='no'&&!correct)){score++;document.getElementById('points').textContent=score}newRound()}
timer=setInterval(()=>{time--;document.getElementById('time').textContent=time;if(time===0){clearInterval(timer);alert(`Game Over! Score: ${score}`);location.reload()}},1000);
newRound()</script></body></html>"""

REACTION_GAME_HTML = """<!DOCTYPE html>
<html><head><title>Reaction Game</title><meta charset="UTF-8">
<style>body{font-family:Arial;text-align:center;padding:50px;background:#f0f0f0}
#game{background:white;padding:40px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.2);max-width:500px;margin:0 auto}
h1{color:#2c5aa0}#circle{width:150px;height:150px;border-radius:50%;background:#e74c3c;margin:40px auto;cursor:pointer;display:none}
#message{font-size:24px;margin:20px;color:#2c5aa0}
button{padding:15px 40px;font-size:20px;background:#2c5aa0;color:white;border:none;border-radius:8px;cursor:pointer}</style>
</head><body><div id="game"><h1>⚡ Reaction Game</h1>
<div id="message">Click START to begin!</div><div id="circle"></div><button onclick="start()">START</button></div>
<script>let startTime;
function start(){document.getElementById('message').textContent='Wait for GREEN...';document.getElementById('circle').style.display='none';
setTimeout(()=>{document.getElementById('circle').style.display='block';document.getElementById('circle').style.background='#2ecc71';startTime=Date.now();document.getElementById('message').textContent='CLICK NOW!'},Math.random()*3000+2000)}
document.getElementById('circle').onclick=()=>{if(document.getElementById('circle').style.background==='rgb(46, 204, 113)'){const time=Date.now()-startTime;document.getElementById('message').textContent=`${time}ms - ${time<200?'Amazing!':time<300?'Good!':'Keep trying!'}`;document.getElementById('circle').style.display='none'}}</script></body></html>"""

# Create game files if they don't exist
for filename, content in [('math_quiz.html', MATH_QUIZ_HTML), ('color_game.html', COLOR_GAME_HTML), ('reaction_game.html', REACTION_GAME_HTML)]:
    filepath = f'static/games/{filename}'
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filepath}")

# ============================================================
# DATABASE SETUP (from Lesson 3)
# ============================================================

def init_database():
    """Create database with sample projects"""
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT
    )''')
    
    # Check if data exists
    c.execute('SELECT COUNT(*) FROM projects')
    if c.fetchone()[0] == 0:
        # Insert sample projects
        projects = [
            (1, 'Number Guessing Game', 'A simple game where you guess a random number', 'Python'),
            (2, 'Calculator App', 'Basic calculator with +, -, *, / operations', 'Python'),
            (3, 'To-Do List', 'Manage your tasks with this simple app', 'Python'),
            (4, 'Personal Portfolio', 'This website you are viewing now', 'Web'),
            (5, 'Math Quiz Game', 'Test your math skills with random questions', 'Game'),
            (6, 'Color Matching Game', 'Match colors as fast as you can', 'Game'),
            (7, 'Reaction Speed Test', 'Test your reaction time', 'Game'),
            (8, 'Weather App', 'Check the weather in any city', 'Web'),
            (9, 'Snake Game', 'Classic snake game built with Python', 'Game'),
            (10, 'Chat Application', 'Simple chat app using Flask', 'Web'),
            (11, 'Expense Tracker', 'Track your daily expenses', 'Desktop'),
            (12, 'Password Generator', 'Generate secure random passwords', 'Python'),
            (13, 'Hangman Game', 'Classic word guessing game', 'Game'),
            (14, 'File Organizer', 'Automatically organize your files', 'Desktop'),
            (15, 'Quiz Application', 'Create and take custom quizzes', 'Web'),
        ]
        c.executemany('INSERT INTO projects VALUES (?,?,?,?)', projects)
        print("✅ Database initialized with 15 projects")
    
    conn.commit()
    conn.close()

init_database()

# ============================================================
# CSS STYLES (STEM WORK Theme)
# ============================================================

CLEAN_CSS = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, 'Microsoft JhengHei', sans-serif; background: #f8f9fa; }
    
    .navbar { background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
    .nav-container { max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 24px; font-weight: bold; color: #2c5aa0; }
    .nav-links { display: flex; gap: 25px; list-style: none; }
    .nav-links a { text-decoration: none; color: #333; font-weight: 500; }
    .nav-links a:hover { color: #2c5aa0; }
    .nav-links a.active { color: #2c5aa0; border-bottom: 2px solid #2c5aa0; }
    
    .hero { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; text-align: center; padding: 60px 20px; }
    .hero h1 { font-size: 42px; margin-bottom: 10px; }
    .hero p { font-size: 18px; opacity: 0.9; }
    .hero-btn { background: white; color: #2c5aa0; padding: 12px 30px; border-radius: 5px; text-decoration: none; font-weight: bold; margin: 10px; display: inline-block; }
    
    .container { max-width: 1200px; margin: 40px auto; padding: 20px; }
    .section { background: white; padding: 40px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .section h2 { color: #2c5aa0; font-size: 28px; margin-bottom: 20px; }
    
    .game-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; margin-top: 20px; }
    .game-card { background: #f8f9fa; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); transition: transform 0.3s; }
    .game-card:hover { transform: translateY(-5px); }
    .game-header { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; padding: 30px; text-align: center; font-size: 48px; }
    .game-content { padding: 20px; }
    .game-title { font-size: 20px; font-weight: bold; color: #333; margin-bottom: 10px; }
    .game-desc { color: #666; font-size: 14px; margin-bottom: 15px; }
    .game-type { display: inline-block; background: #2c5aa0; color: white; padding: 5px 15px; border-radius: 20px; font-size: 12px; margin-bottom: 15px; }
    .play-btn { width: 100%; padding: 12px; background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; text-decoration: none; display: block; text-align: center; }
    
    .game-frame { width: 100%; height: 650px; border: none; border-radius: 10px; }
    
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
    .stat-card { background: #f8f9fa; border-radius: 10px; padding: 30px; text-align: center; }
    .stat-number { font-size: 48px; font-weight: bold; color: #2c5aa0; }
    .stat-label { font-size: 16px; color: #666; margin-top: 10px; }
    
    .checklist { list-style: none; padding: 0; }
    .checklist li { padding: 15px 0; border-bottom: 1px solid #e9ecef; padding-left: 35px; position: relative; }
    .checklist li::before { content: '✓'; position: absolute; left: 0; color: #2c5aa0; font-weight: bold; }
    
    .timeline-item { padding: 20px; margin-bottom: 20px; background: #f8f9fa; border-left: 4px solid #2c5aa0; border-radius: 8px; }
    .skill-badges { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }
    .skill-badge { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; padding: 8px 16px; border-radius: 20px; font-size: 14px; }
    
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

# ============================================================
# NAVIGATION (from Lesson 5)
# ============================================================

def get_nav(active_page):
    return f"""
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">🎓 {t("My Coding Portfolio")}</div>
            <ul class="nav-links">
                <li><a href="/" class="{'active' if active_page == 'home' else ''}">{b("Home")}</a></li>
                <li><a href="/projects" class="{'active' if active_page == 'projects' else ''}">{b("Projects")}</a></li>
                <li><a href="/games" class="{'active' if active_page == 'games' else ''}">{b("Games")}</a></li>
                <li><a href="/parent-dashboard" class="{'active' if active_page == 'parents' else ''}">👨‍👩‍👧 {b("For Parents")}</a></li>
                <li><a href="/about" class="{'active' if active_page == 'about' else ''}">{b("About")}</a></li>
            </ul>
        </div>
    </nav>
    """

# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def home():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{t("My Coding Portfolio")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('home')}
        <div class="hero">
            <h1>{t("Welcome to My Coding World")}</h1>
            <h1>Welcome to My Coding Portfolio</h1>
            <p>{t("Showcasing my work from STEM WORK")}</p>
            <a href="/projects" class="hero-btn">{b("View Projects")}</a>
            <a href="/games" class="hero-btn">{b("Play Games")}</a>
        </div>
        <div class="container">
            <div class="section">
                <h2>🎮 {t("Featured Games")}</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">{b("Math Quiz")}</div>
                            <div class="game-desc">{t("Test your math skills!")}</div>
                            <a href="/play/math-quiz" class="play-btn">▶ Play</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">{b("Color Game")}</div>
                            <div class="game-desc">{t("Match colors fast!")}</div>
                            <a href="/play/color-game" class="play-btn">▶ Play</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">{b("Reaction Game")}</div>
                            <div class="game-desc">{t("Test your speed!")}</div>
                            <a href="/play/reaction-game" class="play-btn">▶ Play</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM projects')
    all_projects = c.fetchall()
    c.execute('SELECT COUNT(*) FROM projects')
    total = c.fetchone()[0]
    c.execute('SELECT COUNT(DISTINCT category) FROM projects')
    categories = c.fetchone()[0]
    conn.close()

    icons = {'Python': '🐍', 'Web': '🌐', 'Game': '🎮', 'Desktop': '🖥️'}
    cards = ''
    for proj in all_projects:
        icon = icons.get(proj[3], '🐍')
        cards += f'<div class="game-card"><div class="game-header">{icon}</div><div class="game-content"><div class="game-title">{proj[1]}</div><div class="game-desc">{proj[2][:50]}...</div><span class="game-type">{proj[3]}</span></div></div>'

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("Projects")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('projects')}
        <div class="hero"><h1>{t("My Projects")}</h1><h1>My Projects</h1><p>{total} {t("projects")} | {categories} {t("categories")}</p></div>
        <div class="container">
            <div class="section"><h2>🎯 {b("All Projects")}</h2><div class="game-grid">{cards}</div></div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/games')
def games():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("Games")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🎮 {t("My Games")}</h1><h1>My Games Portfolio</h1><p>7 {t("playable games")}</p></div>
        <div class="container">
            <div class="section">
                <h2>🎯 {t("JavaScript Games")}</h2>
                <div class="game-grid">
                    <div class="game-card"><div class="game-header">🧮</div><div class="game-content"><div class="game-title">{b("Math Quiz")}</div><span class="game-type">JavaScript</span><a href="/play/math-quiz" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">🎨</div><div class="game-content"><div class="game-title">{b("Color Game")}</div><span class="game-type">JavaScript</span><a href="/play/color-game" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">⚡</div><div class="game-content"><div class="game-title">{b("Reaction Game")}</div><span class="game-type">JavaScript</span><a href="/play/reaction-game" class="play-btn">▶ Play</a></div></div>
                </div>
            </div>
            <div class="section">
                <h2>🌐 {t("Vercel Games")}</h2>
                <div class="game-grid">
                    <div class="game-card"><div class="game-header">🐰</div><div class="game-content"><div class="game-title">{b("Whack-a-Mole")}</div><span class="game-type">Vercel</span><a href="/play/mole-game" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">🎆</div><div class="game-content"><div class="game-title">{b("Fireworks")}</div><span class="game-type">Vercel</span><a href="/play/fireworks" class="play-btn">▶ View</a></div></div>
                    <div class="game-card"><div class="game-header">⭐</div><div class="game-content"><div class="game-title">{b("Star Fall")}</div><span class="game-type">Vercel</span><a href="/play/starfall" class="play-btn">▶ View</a></div></div>
                    <div class="game-card"><div class="game-header">👑</div><div class="game-content"><div class="game-title">{b("King and Pigs")}</div><span class="game-type">Vercel</span><a href="/play/kingpigs" class="play-btn">▶ Play</a></div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/parent-dashboard')
def parent_dashboard():
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM projects')
    total = c.fetchone()[0]
    c.execute('SELECT COUNT(DISTINCT category) FROM projects')
    categories = c.fetchone()[0]
    conn.close()
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("For Parents")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('parents')}
        <div class="hero"><h1>👨‍👩‍👧 {t("For My Parents")}</h1><h1>For My Parents</h1><p>{t("Here is what I learned!")}</p></div>
        <div class="container">
            <div class="section">
                <h2>🎉 {t("What I Built")}</h2>
                <p style="font-size: 20px;">{t("I completed")} <strong style="color: #2c5aa0;">{total}</strong> {t("projects")}!</p>
            </div>
            <div class="section">
                <h2>💪 {t("Skills I Learned")}</h2>
                <ul class="checklist">
                    <li>{t("Build websites from scratch")}</li>
                    <li>{t("Create interactive games")}</li>
                    <li>{t("Use databases to store data")}</li>
                    <li>{t("Solve coding problems")}</li>
                </ul>
            </div>
            <div class="section">
                <h2>📈 {b("Statistics")}</h2>
                <div class="stats-grid">
                    <div class="stat-card"><div class="stat-number">{total}</div><div class="stat-label">{b("Projects")}</div></div>
                    <div class="stat-card"><div class="stat-number">{categories}</div><div class="stat-label">{b("Technologies")}</div></div>
                    <div class="stat-card"><div class="stat-number">7</div><div class="stat-label">{b("Games")}</div></div>
                    <div class="stat-card"><div class="stat-number">120+</div><div class="stat-label">{b("Hours")}</div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/about')
def about():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("About")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('about')}
        <div class="hero"><h1>{t("About Me")}</h1><h1>About Me</h1><p>{t("My Coding Journey")}</p></div>
        <div class="container">
            <div class="section">
                <h2>👋 {t("Introduction")}</h2>
                <p style="line-height:2;font-size:17px;">{t("Hello! I am a coding student at STEM WORK. I learned to build websites and games from scratch!")}</p>
            </div>
            <div class="section">
                <h2>🌱 {t("Learning Timeline")}</h2>
                <div class="timeline-item"><strong>2024 Jan</strong> - {t("Started learning Flask and HTML")}</div>
                <div class="timeline-item"><strong>2024 Mar</strong> - {t("Completed first Python project")}</div>
                <div class="timeline-item"><strong>2024 Jun</strong> - {t("Mastered SQLite database")}</div>
                <div class="timeline-item"><strong>2024 Sep</strong> - {t("Built this portfolio website")}</div>
            </div>
            <div class="section">
                <h2>💪 {t("My Skills")}</h2>
                <div class="skill-badges">
                    <span class="skill-badge">🐍 Python</span>
                    <span class="skill-badge">🌐 HTML/CSS</span>
                    <span class="skill-badge">⚡ JavaScript</span>
                    <span class="skill-badge">🔥 Flask</span>
                    <span class="skill-badge">🗄️ SQLite</span>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

# ============================================================
# GAME ROUTES
# ============================================================

@app.route('/play/math-quiz')
def play_math_quiz():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Math Quiz</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🧮 {b("Math Quiz")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/math_quiz.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/color-game')
def play_color_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Color Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎨 {b("Color Game")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/color_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/reaction-game')
def play_reaction_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Reaction Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⚡ {b("Reaction Game")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/reaction_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/mole-game')
def play_mole():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Whack-a-Mole</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🐰 {b("Whack-a-Mole")}</h1></div><div class="container"><div class="section"><iframe src="https://mole-game-psi.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/fireworks')
def play_fireworks():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Fireworks</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎆 {b("Fireworks")}</h1></div><div class="container"><div class="section"><iframe src="https://firework-self.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/starfall')
def play_starfall():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Star Fall</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⭐ {b("Star Fall")}</h1></div><div class="container"><div class="section"><iframe src="https://star-falling.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/kingpigs')
def play_kingpigs():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>King & Pigs</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>👑 {b("King and Pigs")}</h1></div><div class="container"><div class="section"><iframe src="https://king-and-pigs-test.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/games/<path:filename>')
def serve_game(filename):
    return send_from_directory('static/games', filename)


if __name__ == '__main__':
    print("=" * 60)
    print("🎓 LESSON 12: FINAL INTEGRATION")
    print("=" * 60)
    print()
    print("This is the complete portfolio combining all lessons!")
    print()
    print("📄 5 Pages: Home, Projects, Games, Parents, About")
    print("🎮 7 Games: 3 JavaScript + 4 Vercel")
    print("🗄️ Database: 15 projects")
    print("🌐 Bilingual: Auto-translated")
    print()
    print("📖 See lesson12_guide.md for documentation")
    print()
    print("Server: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)

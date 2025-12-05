# Lesson 7: Create Your Own JavaScript Games
# Focus: Build 3 HTML/JS games and embed them using iframe
#
# BUILDS ON LESSON 6b:
# - Same navigation with active page highlighting
# - Same CSS with game card and iframe styles
# - /projects reads from database
# - /games page with 7 game cards
# - 4 Vercel game routes work
#
# NEW IN THIS LESSON:
# - Create static/games/math_quiz.html
# - Create static/games/color_game.html
# - Create static/games/reaction_game.html
# - /play/math-quiz, /play/color-game, /play/reaction-game routes
# - ALL 7 game buttons now work!

from flask import Flask, render_template_string
import sqlite3
import os

app = Flask(__name__)

# ============================================================
# CREATE GAME FILES - Auto-create all 3 JS games
# ============================================================
os.makedirs('static/games', exist_ok=True)

# Game 1: Math Quiz
MATH_QUIZ_HTML = """<!DOCTYPE html>
<html><head><title>Math Quiz</title><meta charset="UTF-8">
<style>body{font-family:Arial;text-align:center;padding:50px;background:#f0f0f0}
#game{background:white;padding:40px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.2);max-width:500px;margin:0 auto}
h1{color:#2c5aa0}#question{font-size:36px;margin:30px 0}
input{padding:15px;font-size:24px;width:200px;border:2px solid #2c5aa0;border-radius:8px}
button{padding:15px 40px;font-size:20px;background:#2c5aa0;color:white;border:none;border-radius:8px;cursor:pointer;margin-top:20px}
button:hover{background:#1e4070}#score{font-size:24px;margin-top:20px;color:#2c5aa0}</style>
</head><body><div id="game"><h1>🧮 Math Quiz</h1><div id="question"></div>
<input type="number" id="answer" placeholder="Your answer"><br>
<button onclick="checkAnswer()">Submit</button><div id="score">Score: <span id="points">0</span></div></div>
<script>let score=0,a,b,op;
function newQuestion(){a=Math.floor(Math.random()*10)+1;b=Math.floor(Math.random()*10)+1;op=['+','-','×'][Math.floor(Math.random()*3)];document.getElementById('question').textContent=`${a} ${op} ${b} = ?`;document.getElementById('answer').value='';document.getElementById('answer').focus()}
function checkAnswer(){const answer=parseInt(document.getElementById('answer').value);let correct;if(op==='+')correct=a+b;else if(op==='-')correct=a-b;else correct=a*b;if(answer===correct){score++;document.getElementById('points').textContent=score;alert('Correct! 🎉')}else{alert(`Wrong! The answer was ${correct}`)}newQuestion()}
newQuestion()</script></body></html>"""

# Game 2: Color Game
COLOR_GAME_HTML = """<!DOCTYPE html>
<html><head><title>Color Game</title><meta charset="UTF-8">
<style>body{font-family:Arial;text-align:center;padding:30px;background:#f0f0f0}
#game{background:white;padding:30px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.2);max-width:600px;margin:0 auto}
h1{color:#2c5aa0}#word{font-size:72px;font-weight:bold;margin:30px 0}
.btn{padding:20px 40px;margin:10px;font-size:24px;background:#2c5aa0;color:white;border:none;border-radius:8px;cursor:pointer}
.btn:hover{background:#1e4070}#timer,#score{font-size:24px;margin:10px;color:#2c5aa0}</style>
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

# Game 3: Reaction Game
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

# Create all game files
for filename, content in [('math_quiz.html', MATH_QUIZ_HTML), ('color_game.html', COLOR_GAME_HTML), ('reaction_game.html', REACTION_GAME_HTML)]:
    filepath = f'static/games/{filename}'
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filepath}")

# ============================================================
# CSS - Same as Lesson 6b
# ============================================================
CLEAN_CSS = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, 'Microsoft JhengHei', sans-serif; background: #f8f9fa; }
    
    .navbar { background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
    .nav-container { max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 24px; font-weight: bold; color: #2c5aa0; }
    .nav-links { display: flex; gap: 25px; list-style: none; }
    .nav-links a { text-decoration: none; color: #333; font-weight: 500; transition: color 0.3s; }
    .nav-links a:hover { color: #2c5aa0; }
    .nav-links a.active { color: #2c5aa0; border-bottom: 2px solid #2c5aa0; }
    
    .hero { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; text-align: center; padding: 60px 20px; }
    .hero h1 { font-size: 42px; margin-bottom: 10px; }
    .hero p { font-size: 18px; opacity: 0.9; }
    
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
    .play-btn:hover { transform: scale(1.05); }
    
    .game-frame { width: 100%; height: 650px; border: none; border-radius: 10px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); background: white; }
    
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

def get_nav(active_page):
    return f"""
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">My Portfolio</div>
            <ul class="nav-links">
                <li><a href="/" class="{'active' if active_page == 'home' else ''}">Home</a></li>
                <li><a href="/projects" class="{'active' if active_page == 'projects' else ''}">Projects</a></li>
                <li><a href="/games" class="{'active' if active_page == 'games' else ''}">Games</a></li>
                <li><a href="/parent-dashboard" class="{'active' if active_page == 'parents' else ''}">For Parents</a></li>
                <li><a href="/about" class="{'active' if active_page == 'about' else ''}">About</a></li>
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
    <head><title>Home - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('home')}
        <div class="hero">
            <h1>Welcome to My Coding Portfolio</h1>
            <p>Built with Flask at STEM WORK</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>🎉 Lesson 7: JavaScript Games</h2>
                <p style="line-height: 2;">In Lesson 6b, we embedded Vercel games using iframes.</p>
                <p style="line-height: 2;">In Lesson 7, we <strong>create our own HTML/JS games</strong>:</p>
                <ul style="margin: 15px 0 15px 30px; line-height: 2;">
                    <li>🧮 Math Quiz - Test your math skills</li>
                    <li>🎨 Color Game - Match colors in 30 seconds</li>
                    <li>⚡ Reaction Game - Test your speed</li>
                </ul>
                <p style="line-height: 2;">All 7 games are now playable! Click <a href="/games" style="color: #2c5aa0; font-weight: bold;">Games</a> to try them.</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM projects')
        all_projects = c.fetchall()
    except Exception:
        all_projects = []
    conn.close()

    cards = ''
    icons = {'Python': '🐍', 'Web': '🌐', 'Game': '🎮', 'Desktop': '🖥️'}
    for proj in all_projects:
        icon = icons.get(proj[3], '🐍')
        cards += f'''
        <div class="game-card">
            <div class="game-header">{icon}</div>
            <div class="game-content">
                <div class="game-title">{proj[1]}</div>
                <div class="game-desc">{proj[2][:60]}...</div>
                <span class="game-type">{proj[3]}</span>
            </div>
        </div>'''

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Projects - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('projects')}
        <div class="hero"><h1>All My Projects</h1><p>15 projects from the database</p></div>
        <div class="container">
            <div class="section">
                <h2>Projects Gallery</h2>
                <div class="game-grid">{cards}</div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/games')
def games():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Games - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero">
            <h1>My Games Portfolio</h1>
            <p>🎉 All 7 games are now playable!</p>
        </div>
        <div class="container">
            <!-- JavaScript Games - ALL NOW WORK -->
            <div class="section">
                <h2>My JavaScript Games</h2>
                <p>3 games I built myself! (Lesson 7)</p>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">Math Quiz</div>
                            <div class="game-desc">Math quiz game - test your skills</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/math-quiz" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">Color Game</div>
                            <div class="game-desc">Color matching - 30 second challenge</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/color-game" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">Reaction Game</div>
                            <div class="game-desc">Test your reaction speed</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/reaction-game" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Vercel Games - Same as 6b -->
            <div class="section">
                <h2>Professional Vercel Games</h2>
                <p>Games embedded from Vercel!</p>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🐰</div>
                        <div class="game-content">
                            <div class="game-title">Whack-a-Mole</div>
                            <div class="game-desc">Whack-a-Mole on Vercel</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/mole-game" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎆</div>
                        <div class="game-content">
                            <div class="game-title">Fireworks</div>
                            <div class="game-desc">Fireworks animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/fireworks" class="play-btn">▶ View Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⭐</div>
                        <div class="game-content">
                            <div class="game-title">Star Fall</div>
                            <div class="game-desc">Falling stars animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/starfall" class="play-btn">▶ View Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">👑</div>
                        <div class="game-content">
                            <div class="game-title">King & Pigs</div>
                            <div class="game-desc">Adventure platform game</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/kingpigs" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

# ============================================================
# JavaScript Game Routes (3 total) - NEW in Lesson 7
# ============================================================

@app.route('/play/math-quiz')
def play_math_quiz():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Math Quiz - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🧮 Math Quiz</h1><p>A game I built myself!</p></div>
        <div class="container"><div class="section">
            <iframe src="/static/games/math_quiz.html" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/play/color-game')
def play_color_game():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Color Game - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🎨 Color Game</h1><p>Match the word with its color!</p></div>
        <div class="container"><div class="section">
            <iframe src="/static/games/color_game.html" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/play/reaction-game')
def play_reaction_game():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Reaction Game - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>⚡ Reaction Game</h1><p>Test your reaction speed!</p></div>
        <div class="container"><div class="section">
            <iframe src="/static/games/reaction_game.html" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

# ============================================================
# Vercel Game Routes - Same as Lesson 6b
# ============================================================

@app.route('/play/mole-game')
def play_mole():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Whack-a-Mole</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🐰 Whack-a-Mole</h1><p>Embedded from Vercel</p></div>
        <div class="container"><div class="section">
            <iframe src="https://mole-game-psi.vercel.app/" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/play/fireworks')
def play_fireworks():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Fireworks</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🎆 Fireworks</h1><p>Embedded from Vercel</p></div>
        <div class="container"><div class="section">
            <iframe src="https://firework-self.vercel.app/" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/play/starfall')
def play_starfall():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Star Fall</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>⭐ Star Fall</h1><p>Embedded from Vercel</p></div>
        <div class="container"><div class="section">
            <iframe src="https://star-falling.vercel.app/" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/play/kingpigs')
def play_kingpigs():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>King & Pigs</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>👑 King & Pigs</h1><p>Embedded from Vercel</p></div>
        <div class="container"><div class="section">
            <iframe src="https://king-and-pigs-test.vercel.app/" class="game-frame"></iframe>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

# ============================================================
# Placeholder routes - Will be expanded in later lessons
# ============================================================

@app.route('/parent-dashboard')
def parent_dashboard():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>For Parents</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('parents')}
        <div class="hero"><h1>👨‍👩‍👧 For Parents</h1><p>Information for parents</p></div>
        <div class="container"><div class="section">
            <h2>Parent Dashboard (Coming in Lesson 8)</h2>
            <p style="line-height: 2;">This page will show parents what skills I learned.</p>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/about')
def about():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>About</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('about')}
        <div class="hero"><h1>About Me</h1><p>My coding journey</p></div>
        <div class="container"><div class="section">
            <h2>About Page (Coming in Lesson 10)</h2>
            <p style="line-height: 2;">This page will contain my learning timeline.</p>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)


if __name__ == '__main__':
    print("=" * 60)
    print("LESSON 7: Create Your Own JavaScript Games")
    print("=" * 60)
    print()
    print("BUILDS ON Lesson 6b:")
    print("  ✓ Navigation with active page highlighting")
    print("  ✓ /projects reads from database")
    print("  ✓ 4 Vercel game routes")
    print()
    print("NEW in this lesson:")
    print("  ✓ Created static/games/math_quiz.html")
    print("  ✓ Created static/games/color_game.html")
    print("  ✓ Created static/games/reaction_game.html")
    print("  ✓ /play/math-quiz route")
    print("  ✓ /play/color-game route")
    print("  ✓ /play/reaction-game route")
    print()
    print("🎮 ALL 7 GAMES NOW WORK:")
    print("   JavaScript: Math Quiz, Color Game, Reaction Game")
    print("   Vercel: Mole, Fireworks, Star Fall, King & Pigs")
    print()
    print("Server: http://127.0.0.1:5000")
    print("Visit /games to play all 7 games!")
    print("=" * 60)
    app.run(debug=True, port=5000)

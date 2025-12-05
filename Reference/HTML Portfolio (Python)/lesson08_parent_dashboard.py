# Lesson 8: Parent Dashboard with Database Statistics
# Focus: Create a page for parents showing achievements in simple language
#
# BUILDS ON LESSON 7:
# - Same navigation with active page highlighting
# - Same CSS with game card and iframe styles
# - /projects reads from database
# - /games page with all 7 game cards (all work)
# - All 7 game routes work (3 JS + 4 Vercel)
#
# NEW IN THIS LESSON:
# - Full /parent-dashboard page with real content
# - Database statistics (COUNT, DISTINCT)
# - Simple, non-jargon language for parents
# - Skills checklist and value explanation

from flask import Flask, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Ensure game files exist (from Lesson 7)
os.makedirs('static/games', exist_ok=True)

# ============================================================
# CSS - Same as Lesson 7 + checklist styles for parent dashboard
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
    
    /* NEW: Checklist style for parent dashboard */
    .checklist { list-style: none; padding: 0; }
    .checklist li { padding: 15px 0; border-bottom: 1px solid #e9ecef; padding-left: 35px; position: relative; }
    .checklist li::before { content: '✓'; position: absolute; left: 0; color: #2c5aa0; font-weight: bold; font-size: 20px; }
    
    /* NEW: Value box for highlighting benefits */
    .value-box { background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; border-left: 5px solid #4caf50; margin: 30px 0; }
    
    /* Stats grid for numbers */
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
    .stat-card { background: #f8f9fa; border-radius: 10px; padding: 30px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .stat-number { font-size: 48px; font-weight: bold; color: #2c5aa0; }
    .stat-label { font-size: 16px; color: #666; margin-top: 10px; }
    
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
                <h2>What's New in Lesson 8</h2>
                <p style="line-height: 2;">In Lesson 7, we completed all 7 games.</p>
                <p style="line-height: 2;">In Lesson 8, we create the <strong>Parent Dashboard</strong> with database statistics!</p>
                <p style="line-height: 2; margin-top: 15px;">Click <a href="/parent-dashboard" style="color: #2c5aa0; font-weight: bold;">For Parents</a> to see the new page.</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    """Projects page - Same as Lesson 7"""
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
    """Games page - Same as Lesson 7, all 7 games work"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Games - My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero">
            <h1>My Games Portfolio</h1>
            <p>All 7 games are playable!</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>My JavaScript Games</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">Math Quiz</div>
                            <div class="game-desc">Math quiz game</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/math-quiz" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">Color Game</div>
                            <div class="game-desc">Color matching game</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/color-game" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">Reaction Game</div>
                            <div class="game-desc">Reaction speed test</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/reaction-game" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section">
                <h2>Professional Vercel Games</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🐰</div>
                        <div class="game-content">
                            <div class="game-title">Whack-a-Mole</div>
                            <div class="game-desc">Whack-a-Mole</div>
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
                            <div class="game-desc">Falling stars</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/starfall" class="play-btn">▶ View Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">👑</div>
                        <div class="game-content">
                            <div class="game-title">King & Pigs</div>
                            <div class="game-desc">Platform game</div>
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
# NEW IN LESSON 8: Full Parent Dashboard
# ============================================================

@app.route('/parent-dashboard')
def parent_dashboard():
    """Parent Dashboard with database statistics and simple language"""
    # Get statistics from database
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    try:
        c.execute('SELECT COUNT(*) FROM projects')
        total_projects = c.fetchone()[0]
        c.execute('SELECT COUNT(DISTINCT category) FROM projects')
        total_categories = c.fetchone()[0]
    except Exception:
        total_projects = 15
        total_categories = 4
    conn.close()
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>For Parents - My Portfolio</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        {get_nav('parents')}
        
        <div class="hero">
            <h1>👨‍👩‍👧 For My Parents</h1>
            <p>Here's What I Learned at STEM WORK!</p>
        </div>
        
        <div class="container">
            <div class="section">
                <h2>🎉 Dad & Mom, Look What I Built!</h2>
                <p style="line-height: 2; font-size: 18px;">
                    <strong style="color: #2c5aa0;">I completed {total_projects} projects!</strong>
                </p>
                <p style="margin-top: 20px; font-size: 17px; line-height: 2;">
                    From knowing nothing about coding to creating my own websites and games - 
                    this is what I achieved at STEM WORK!
                </p>
            </div>
            
            <div class="section">
                <h2>💪 I Can Now Do These Things!</h2>
                <ul class="checklist">
                    <li>Build complete websites from scratch, like this portfolio!</li>
                    <li>Create interactive games - check out the Games page!</li>
                    <li>Design beautiful web pages with professional styling</li>
                    <li>Use databases to store and manage information</li>
                    <li>Solve coding problems independently</li>
                    <li>Understand how websites and apps work</li>
                    <li>Use logical thinking to break down complex problems</li>
                </ul>
            </div>
            
            <div class="value-box">
                <h3 style="color: #2e7d32; margin-bottom: 15px;">🌟 Why These Skills Are Valuable</h3>
                <p style="line-height: 2; font-size: 16px;"><strong>Dad, Mom - these skills will be useful in my future:</strong></p>
                <ul style="margin-left: 20px; line-height: 2; margin-top: 15px;">
                    <li>🎓 <strong>College Applications:</strong> I can showcase my projects when applying to universities</li>
                    <li>💼 <strong>Future Career:</strong> I can become a programmer or web developer</li>
                    <li>🧠 <strong>Thinking Skills:</strong> I learned how to solve problems and think logically</li>
                    <li>🚀 <strong>Creativity:</strong> I can turn my ideas into real websites and apps</li>
                    <li>🌐 <strong>Digital Age:</strong> These skills are essential in today's world</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>📈 Learning Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">{total_projects}</div>
                        <div class="stat-label">Projects Completed</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{total_categories}</div>
                        <div class="stat-label">Technologies Learned</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">7</div>
                        <div class="stat-label">Games Created</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">120+</div>
                        <div class="stat-label">Learning Hours</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>💬 Message to My Parents</h2>
                <div style="margin-top: 20px;">
                    <p style="font-weight: bold; color: #2c5aa0; margin-top: 20px;">💻 What did I learn?</p>
                    <p style="margin-left: 20px; line-height: 1.8;">
                        I learned web development basics, including Python programming, web design (HTML/CSS), 
                        database usage, and game development!
                    </p>
                    
                    <p style="font-weight: bold; color: #2c5aa0; margin-top: 20px;">✨ What can I show you?</p>
                    <p style="margin-left: 20px; line-height: 1.8;">
                        I built this entire website myself! Click "Projects" to see my {total_projects} completed projects, 
                        click "Games" to play the games I made!
                    </p>
                    
                    <p style="font-weight: bold; color: #2c5aa0; margin-top: 20px;">🚀 What can I do in the future?</p>
                    <p style="margin-left: 20px; line-height: 1.8;">
                        I can now create my own websites, design games, and build apps for family and friends. 
                        In the future, I want to learn more and maybe even take on small projects!
                    </p>
                </div>
            </div>
        </div>
        
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

# ============================================================
# Game Routes - Same as Lesson 7
# ============================================================

@app.route('/play/math-quiz')
def play_math_quiz():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Math Quiz</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🧮 Math Quiz</h1></div><div class="container"><div class="section"><iframe src="/static/games/math_quiz.html" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/color-game')
def play_color_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Color Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎨 Color Game</h1></div><div class="container"><div class="section"><iframe src="/static/games/color_game.html" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/reaction-game')
def play_reaction_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Reaction Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⚡ Reaction Game</h1></div><div class="container"><div class="section"><iframe src="/static/games/reaction_game.html" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/mole-game')
def play_mole():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Whack-a-Mole</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🐰 Whack-a-Mole</h1></div><div class="container"><div class="section"><iframe src="https://mole-game-psi.vercel.app/" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/fireworks')
def play_fireworks():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Fireworks</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎆 Fireworks</h1></div><div class="container"><div class="section"><iframe src="https://firework-self.vercel.app/" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/starfall')
def play_starfall():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Star Fall</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⭐ Star Fall</h1></div><div class="container"><div class="section"><iframe src="https://star-falling.vercel.app/" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

@app.route('/play/kingpigs')
def play_kingpigs():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>King & Pigs</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>👑 King & Pigs</h1></div><div class="container"><div class="section"><iframe src="https://king-and-pigs-test.vercel.app/" class="game-frame"></iframe></div></div><div class="footer"><p>© 2024</p></div></body></html>""")

# About page placeholder
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
            <p style="line-height: 2;">This page will contain my learning timeline and personal story.</p>
        </div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)


if __name__ == '__main__':
    print("=" * 60)
    print("LESSON 8: Parent Dashboard with Database Statistics")
    print("=" * 60)
    print()
    print("KEEPS from Lesson 7:")
    print("  ✓ Navigation with active page highlighting")
    print("  ✓ /projects reads from database")
    print("  ✓ /games page with all 7 game cards")
    print("  ✓ All 7 game routes work")
    print()
    print("NEW in this lesson:")
    print("  ✓ Full /parent-dashboard page")
    print("  ✓ Database statistics (COUNT, DISTINCT)")
    print("  ✓ Skills checklist")
    print("  ✓ Value explanation for parents")
    print("  ✓ Stats cards showing achievements")
    print()
    print("Server: http://127.0.0.1:5000")
    print("Visit /parent-dashboard to see the new page!")
    print("=" * 60)
    app.run(debug=True, port=5000)

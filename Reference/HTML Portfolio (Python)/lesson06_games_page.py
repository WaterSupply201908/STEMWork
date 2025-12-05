# Lesson 6: Games Page & Game Embedding
# Add games showcase page to the website

from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

CLEAN_CSS = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, 'Microsoft JhengHei', sans-serif; background: #f8f9fa; }
    .navbar { background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; }
    .nav-container { max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 24px; font-weight: bold; color: #2c5aa0; }
    .nav-links { display: flex; gap: 25px; list-style: none; }
    .nav-links a { text-decoration: none; color: #333; font-weight: 500; }
    .nav-links a:hover { color: #2c5aa0; }
    .hero { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; text-align: center; padding: 60px 20px; }
    .hero h1 { font-size: 42px; margin-bottom: 10px; }
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
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

NAV_HTML = """
<nav class="navbar">
    <div class="nav-container">
        <div class="logo">My Portfolio</div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/projects">Projects</a></li>
            <li><a href="/games">Games</a></li>
            <li><a href="/parent-dashboard">For Parents</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </div>
</nav>
"""

@app.route('/')
def home():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><title>Home</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {NAV_HTML}
        <div class="hero"><h1>Welcome to My Coding Portfolio</h1></div>
        <div class="container"><div class="section"><h2>Home Page</h2><p>Click "Games" to see the new games page!</p></div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body></html>
    """)

@app.route('/projects')
def projects():
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM projects')
    all_projects = c.fetchall()
    conn.close()
    
    cards = ''
    for proj in all_projects:
        cards += f'<div class="game-card"><div class="game-header">🐍</div><div class="game-content"><div class="game-title">{proj[1]}</div><div class="game-desc">{proj[2][:60]}...</div></div></div>'
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><title>Projects</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {NAV_HTML}
        <div class="hero"><h1>All My Projects</h1></div>
        <div class="container"><div class="section"><div class="game-grid">{cards}</div></div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body></html>
    """)

@app.route('/games')
def games():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><title>Games</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {NAV_HTML}
        <div class="hero"><h1>My Games Portfolio</h1><p>JavaScript Games + Vercel Games</p></div>
        <div class="container">
            <div class="section">
                <h2>My JavaScript Games</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">Math Quiz</div>
                            <div class="game-desc">Math quiz game - test your skills</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">Color Game</div>
                            <div class="game-desc">Color matching game - 30 second challenge</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">Reaction Game</div>
                            <div class="game-desc">Reaction speed test game</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now</a>
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
                            <div class="game-desc">Whack-a-Mole on Vercel</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎆</div>
                        <div class="game-content">
                            <div class="game-title">Fireworks</div>
                            <div class="game-desc">Fireworks animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ View Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⭐</div>
                        <div class="game-content">
                            <div class="game-title">Star Fall</div>
                            <div class="game-desc">Falling stars animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ View Now</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">👑</div>
                        <div class="game-content">
                            <div class="game-title">King & Pigs</div>
                            <div class="game-desc">Adventure platform game</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ Play Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body></html>
    """)

@app.route('/parent-dashboard')
def parent_dashboard():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><title>For Parents</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {NAV_HTML}
        <div class="hero"><h1>👨‍👩‍👧 For Parents</h1></div>
        <div class="container"><div class="section"><h2>Parent Dashboard (Coming in Lesson 8)</h2></div></div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body></html>
    """)

@app.route('/about')
def about():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><title>About</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {NAV_HTML}
        <div class="hero"><h1>About Me</h1></div>
        <div class="container"><div class="section"><h2>About Page (Coming in Lesson 10)</h2></div></div>
        <div class="footer"><p> 2024 | Learning at STEM WORK</p></div>
    </body></html>
    """)

if __name__ == '__main__':
    print("LESSON 6: Games Page & Game Embedding")
    print("Server: http://127.0.0.1:5000")
    print("Visit /games to see 7 games showcase")
    print("")
    app.run(debug=True, port=5000)

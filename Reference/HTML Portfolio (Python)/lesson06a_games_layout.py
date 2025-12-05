# Lesson 6a: Games Page Layout (No Playable Games Yet)
# Focus: design the /games page with cards and sections.
# 
# BUILDS ON LESSON 5:
# - Same navigation structure (Home, Projects, Games, For Parents, About)
# - Same STEM WORK blue theme (#2c5aa0)
# - Keeps the database reading for /projects from Lesson 4
#
# NEW IN THIS LESSON:
# - /games page layout with game cards
# - Card design pattern (header with emoji, content, button)
# - Game sections: "My JavaScript Games" + "Professional Vercel Games"

from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# ============================================================
# CSS - Extended from Lesson 5 with game-specific styles
# ============================================================
CLEAN_CSS = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, 'Microsoft JhengHei', sans-serif; background: #f8f9fa; }
    
    /* Navigation - Same as Lesson 5 */
    .navbar { background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
    .nav-container { max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 24px; font-weight: bold; color: #2c5aa0; }
    .nav-links { display: flex; gap: 25px; list-style: none; }
    .nav-links a { text-decoration: none; color: #333; font-weight: 500; transition: color 0.3s; }
    .nav-links a:hover { color: #2c5aa0; }
    .nav-links a.active { color: #2c5aa0; border-bottom: 2px solid #2c5aa0; }
    
    /* Hero Section - Same as Lesson 5 */
    .hero { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; text-align: center; padding: 60px 20px; }
    .hero h1 { font-size: 42px; margin-bottom: 10px; }
    .hero p { font-size: 18px; opacity: 0.9; }
    
    /* Container & Sections - Same as Lesson 5 */
    .container { max-width: 1200px; margin: 40px auto; padding: 20px; }
    .section { background: white; padding: 40px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .section h2 { color: #2c5aa0; font-size: 28px; margin-bottom: 20px; }
    
    /* NEW: Game Grid & Cards - Added in Lesson 6a */
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
    
    /* Footer - Same as Lesson 5 */
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

# ============================================================
# Helper function to generate navigation with active highlighting
# (Carried over from Lesson 5)
# ============================================================
def get_nav(active_page):
    """Generate navigation bar with active page highlighting (from Lesson 5)"""
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
# ROUTES - Building on Lesson 5, adding Games page layout
# ============================================================

@app.route('/')
def home():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home - My Portfolio</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        {get_nav('home')}
        <div class="hero">
            <h1>Welcome to My Coding Portfolio</h1>
            <p>Built with Flask at STEM WORK</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>What's New in Lesson 6a</h2>
                <p style="line-height: 2;">In Lesson 5, we learned about navigation and multi-page layouts.</p>
                <p style="line-height: 2;">In Lesson 6a, we add a <strong>Games page layout</strong> with card design.</p>
                <p style="line-height: 2; margin-top: 15px;">Click <a href="/games" style="color: #2c5aa0; font-weight: bold;">Games</a> in the navigation to see the new layout!</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    """Projects page - Same as Lesson 4/5, reads from database"""
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM projects')
        all_projects = c.fetchall()
    except Exception:
        all_projects = []
    conn.close()

    # Build project cards (using the new card style from this lesson)
    cards = ''
    icons = {'Python': '🐍', 'Web': '🌐', 'Game': '🎮', 'Desktop': '🖥️'}
    for proj in all_projects:
        icon = icons.get(proj[3], '🐍')  # proj[3] is category
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
    <head>
        <title>Projects - My Portfolio</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        {get_nav('projects')}
        <div class="hero">
            <h1>All My Projects</h1>
            <p>15 projects from the database (Lesson 3-4)</p>
        </div>
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
    """NEW IN LESSON 6a: Games page with card layout"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Games - My Portfolio</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        {get_nav('games')}
        <div class="hero">
            <h1>My Games Portfolio</h1>
            <p>Layout only – buttons will work in later lessons (6b, 6c, 7).</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>My JavaScript Games</h2>
                <p>In future lessons we will build these games ourselves.</p>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">Math Quiz</div>
                            <div class="game-desc">Math quiz game - test your skills</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now (coming soon)</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">Color Game</div>
                            <div class="game-desc">Color matching game - 30 second challenge</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now (coming soon)</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">Reaction Game</div>
                            <div class="game-desc">Reaction speed test game</div>
                            <span class="game-type">JavaScript</span>
                            <a href="#" class="play-btn">▶ Play Now (coming soon)</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>Professional Vercel Games</h2>
                <p>In a later lesson we will embed games from other websites here.</p>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🐰</div>
                        <div class="game-content">
                            <div class="game-title">Whack-a-Mole</div>
                            <div class="game-desc">Whack-a-Mole on Vercel</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ Play Now (coming soon)</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎆</div>
                        <div class="game-content">
                            <div class="game-title">Fireworks</div>
                            <div class="game-desc">Fireworks animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ View Now (coming soon)</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⭐</div>
                        <div class="game-content">
                            <div class="game-title">Star Fall</div>
                            <div class="game-desc">Falling stars animation</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ View Now (coming soon)</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">👑</div>
                        <div class="game-content">
                            <div class="game-title">King & Pigs</div>
                            <div class="game-desc">Adventure platform game</div>
                            <span class="game-type">Vercel</span>
                            <a href="#" class="play-btn">▶ Play Now (coming soon)</a>
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
    """Placeholder - will be expanded in Lesson 8"""
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
            <h1>👨‍👩‍👧 For Parents</h1>
            <p>Information for parents about what I learned</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>Parent Dashboard (Coming in Lesson 8)</h2>
                <p style="line-height: 2;">This page will show parents what skills I learned and my achievements.</p>
                <p style="line-height: 2;">It will use statistics from the database (Lesson 11).</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)

@app.route('/about')
def about():
    """Placeholder - will be expanded in Lesson 10"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About - My Portfolio</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        {get_nav('about')}
        <div class="hero">
            <h1>About Me</h1>
            <p>My coding journey and personal story</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>About Page (Coming in Lesson 10)</h2>
                <p style="line-height: 2;">This page will contain my learning timeline and personal introduction.</p>
                <p style="line-height: 2;">It will showcase my skills and favorite projects.</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | Learning at STEM WORK</p></div>
    </body>
    </html>
    """)


if __name__ == '__main__':
    print("=" * 60)
    print("LESSON 6a: Games Page Layout")
    print("=" * 60)
    print()
    print("BUILDS ON Lesson 5:")
    print("  ✓ Same navigation with active page highlighting")
    print("  ✓ Same STEM WORK blue theme (#2c5aa0)")
    print("  ✓ /projects still reads from database")
    print()
    print("NEW in this lesson:")
    print("  ✓ /games page with card layout design")
    print("  ✓ Game card pattern (emoji header, content, button)")
    print("  ✓ Two sections: 'My JS Games' + 'Vercel Games'")
    print()
    print("Server: http://127.0.0.1:5000")
    print("Visit /games to see the new layout!")
    print("=" * 60)
    app.run(debug=True, port=5000)

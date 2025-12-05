# Lesson 9: Automatic Translation with deep-translator
# Focus: Use Google Translate API to auto-translate English to Traditional Chinese
#
# BUILDS ON LESSON 8:
# - Same navigation with active page highlighting
# - /projects reads from database
# - /games with all 7 games working
# - Full parent dashboard with statistics
#
# NEW IN THIS LESSON:
# - Install: pip install deep-translator
# - t(text) function - translate English to Chinese
# - b(text) function - bilingual output (Chinese + English)
# - No manual Chinese typing needed!

from flask import Flask, render_template_string
import sqlite3
import os

# ============================================================
# NEW: Import deep-translator for auto-translation
# Install first: pip install deep-translator
# Using MyMemoryTranslator for better quality (no API key needed)
# ============================================================
try:
    from deep_translator import MyMemoryTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("⚠️  deep-translator not installed!")
    print("   Run: pip install deep-translator")

app = Flask(__name__)

os.makedirs('static/games', exist_ok=True)

# ============================================================
# Translation Helper Functions - Using MyMemoryTranslator
# MyMemoryTranslator often provides better quality translations
# ============================================================

def translate(text):
    """Translate English to Traditional Chinese using MyMemory"""
    if not TRANSLATOR_AVAILABLE:
        return text
    if not text or not text.strip():
        return text
    try:
        translator = MyMemoryTranslator(source='en-US', target='zh-TW')
        result = translator.translate(text)
        return result if result else text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def t(text):
    """Translate to Chinese only"""
    return translate(text)

def b(text):
    """Bilingual output (Chinese + English)"""
    chinese = translate(text)
    if chinese == text:  # Translation failed or same
        return text
    return f"{chinese} {text}"

# ============================================================
# CSS - Same as Lesson 8
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
    
    .checklist { list-style: none; padding: 0; }
    .checklist li { padding: 15px 0; border-bottom: 1px solid #e9ecef; padding-left: 35px; position: relative; }
    .checklist li::before { content: '✓'; position: absolute; left: 0; color: #2c5aa0; font-weight: bold; font-size: 20px; }
    
    .value-box { background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; border-left: 5px solid #4caf50; margin: 30px 0; }
    
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
    .stat-card { background: #f8f9fa; border-radius: 10px; padding: 30px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .stat-number { font-size: 48px; font-weight: bold; color: #2c5aa0; }
    .stat-label { font-size: 16px; color: #666; margin-top: 10px; }
    
    .code-box { background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 10px; font-family: monospace; margin: 20px 0; }
    
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

# ============================================================
# NEW: Bilingual navigation using b() function
# ============================================================
def get_nav(active_page):
    """Navigation with auto-translated bilingual links"""
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
# ROUTES - Using auto-translation
# ============================================================

@app.route('/')
def home():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("My Portfolio")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('home')}
        <div class="hero">
            <h1>{t("Welcome to My Coding World")}</h1>
            <h1>Welcome to My Coding Portfolio</h1>
            <p>{t("Showcasing my work from STEM WORK")}</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>Lesson 9: {t("Auto Translation")}</h2>
                <p style="line-height: 2;">{t("In this lesson, we use deep-translator to auto-translate English to Traditional Chinese!")}</p>
                
                <div class="code-box">
                    <code>pip install deep-translator</code><br><br>
                    <code>from deep_translator import MyMemoryTranslator</code><br><br>
                    <code>def t(text):</code><br>
                    <code>&nbsp;&nbsp;&nbsp;&nbsp;return MyMemoryTranslator(source='en-US', target='zh-TW').translate(text)</code><br><br>
                    <code>def b(text):</code><br>
                    <code>&nbsp;&nbsp;&nbsp;&nbsp;return f"{{t(text)}} {{text}}"</code>
                </div>
                
                <h3 style="margin-top: 20px;">{t("Examples")}:</h3>
                <ul style="margin-left: 20px; line-height: 2;">
                    <li><code>t("Hello")</code> → {t("Hello")}</li>
                    <li><code>t("My Projects")</code> → {t("My Projects")}</li>
                    <li><code>b("Home")</code> → {b("Home")}</li>
                    <li><code>b("Games")</code> → {b("Games")}</li>
                </ul>
            </div>
        </div>
        <div class="footer">
            <p>© 2024 | {t("Learning at STEM WORK")}</p>
        </div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    """Projects page with auto-translated content"""
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
    <head><title>{b("Projects")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('projects')}
        <div class="hero">
            <h1>{t("My Projects")}</h1>
            <h1>My Projects</h1>
            <p>{t("15 projects from the database")}</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>🎯 {b("Project Gallery")}</h2>
                <div class="game-grid">{cards}</div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/games')
def games():
    """Games page with auto-translated content"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("Games")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero">
            <h1>🎮 {t("My Games Portfolio")}</h1>
            <h1>My Games Portfolio</h1>
            <p>{t("JavaScript Games + Professional Vercel Games")}</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>🎯 {t("My JavaScript Games")}</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🧮</div>
                        <div class="game-content">
                            <div class="game-title">{b("Math Quiz")}</div>
                            <div class="game-desc">{t("Test your math skills!")}</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/math-quiz" class="play-btn">▶ {t("Play Now")}</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎨</div>
                        <div class="game-content">
                            <div class="game-title">{b("Color Game")}</div>
                            <div class="game-desc">{t("Test your reaction speed!")}</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/color-game" class="play-btn">▶ {t("Play Now")}</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⚡</div>
                        <div class="game-content">
                            <div class="game-title">{b("Reaction Game")}</div>
                            <div class="game-desc">{t("Click to test your speed!")}</div>
                            <span class="game-type">JavaScript</span>
                            <a href="/play/reaction-game" class="play-btn">▶ {t("Play Now")}</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section">
                <h2>🌐 {t("Professional Vercel Games")}</h2>
                <div class="game-grid">
                    <div class="game-card">
                        <div class="game-header">🐰</div>
                        <div class="game-content">
                            <div class="game-title">{b("Whack-a-Mole")}</div>
                            <div class="game-desc">{t("Classic arcade game")}</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/mole-game" class="play-btn">▶ {t("Play Now")}</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">🎆</div>
                        <div class="game-content">
                            <div class="game-title">{b("Fireworks")}</div>
                            <div class="game-desc">{t("Beautiful fireworks animation")}</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/fireworks" class="play-btn">▶ {t("View Now")}</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">⭐</div>
                        <div class="game-content">
                            <div class="game-title">{b("Star Fall")}</div>
                            <div class="game-desc">{t("Falling stars animation")}</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/starfall" class="play-btn">▶ {t("View Now")}</a>
                        </div>
                    </div>
                    <div class="game-card">
                        <div class="game-header">👑</div>
                        <div class="game-content">
                            <div class="game-title">{b("King and Pigs")}</div>
                            <div class="game-desc">{t("Adventure platform game")}</div>
                            <span class="game-type">Vercel</span>
                            <a href="/play/kingpigs" class="play-btn">▶ {t("Play Now")}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/parent-dashboard')
def parent_dashboard():
    """Parent Dashboard with auto-translated content"""
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    try:
        c.execute('SELECT COUNT(*) FROM projects')
        total = c.fetchone()[0]
        c.execute('SELECT COUNT(DISTINCT category) FROM projects')
        categories = c.fetchone()[0]
    except:
        total, categories = 15, 4
    conn.close()
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("For Parents")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('parents')}
        <div class="hero">
            <h1>👨‍👩‍👧 {t("For My Parents")}</h1>
            <h1>For My Parents</h1>
            <p>{t("Here is what I learned at STEM WORK!")}</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>🎉 {t("Dad and Mom, Look What I Built!")}</h2>
                <p style="font-size: 18px; line-height: 2;">
                    <strong style="color: #2c5aa0;">{t("I completed")} {total} {t("projects")}!</strong>
                </p>
            </div>
            <div class="section">
                <h2>💪 {t("I Can Now Do These Things!")}</h2>
                <ul class="checklist">
                    <li>{t("Build websites from scratch")}</li>
                    <li>{t("Create interactive games")}</li>
                    <li>{t("Use databases to store data")}</li>
                    <li>{t("Solve coding problems independently")}</li>
                </ul>
            </div>
            <div class="section">
                <h2>📈 {b("Learning Statistics")}</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">{total}</div>
                        <div class="stat-label">{b("Projects")}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{categories}</div>
                        <div class="stat-label">{b("Technologies")}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">7</div>
                        <div class="stat-label">{b("Games")}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

@app.route('/about')
def about():
    """About page placeholder - will be expanded in Lesson 10"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{b("About")}</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('about')}
        <div class="hero">
            <h1>{t("About Me")}</h1>
            <h1>About Me</h1>
            <p>{t("My Coding Journey")}</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>{b("About Page")} ({t("Coming in Lesson 10")})</h2>
                <p style="line-height: 2;">{t("This page will contain my learning timeline and personal story.")}</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | {t("Learning at STEM WORK")}</p></div>
    </body>
    </html>
    """)

# Game routes - Same as Lesson 8
@app.route('/play/math-quiz')
def play_math_quiz():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Math Quiz")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🧮 {b("Math Quiz")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/math_quiz.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/color-game')
def play_color_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Color Game")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎨 {b("Color Game")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/color_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/reaction-game')
def play_reaction_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Reaction Game")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⚡ {b("Reaction Game")}</h1></div><div class="container"><div class="section"><iframe src="/static/games/reaction_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/mole-game')
def play_mole():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Whack-a-Mole")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🐰 {b("Whack-a-Mole")}</h1></div><div class="container"><div class="section"><iframe src="https://mole-game-psi.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/fireworks')
def play_fireworks():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Fireworks")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎆 {b("Fireworks")}</h1></div><div class="container"><div class="section"><iframe src="https://firework-self.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/starfall')
def play_starfall():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("Star Fall")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⭐ {b("Star Fall")}</h1></div><div class="container"><div class="section"><iframe src="https://star-falling.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/kingpigs')
def play_kingpigs():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>{b("King and Pigs")}</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>👑 {b("King and Pigs")}</h1></div><div class="container"><div class="section"><iframe src="https://king-and-pigs-test.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")


if __name__ == '__main__':
    print("=" * 60)
    print("LESSON 9: Automatic Translation with deep-translator")
    print("=" * 60)
    print()
    if not TRANSLATOR_AVAILABLE:
        print("⚠️  IMPORTANT: Install deep-translator first!")
        print("   Run: pip install deep-translator")
        print()
    print("KEEPS from Lesson 8:")
    print("  ✓ All 7 game routes work")
    print("  ✓ /projects reads from database")
    print("  ✓ Parent dashboard with statistics")
    print()
    print("NEW in this lesson:")
    print("  ✓ t(text) - translate English to Traditional Chinese")
    print("  ✓ b(text) - bilingual output (Chinese + English)")
    print("  ✓ Auto-translation throughout the site")
    print("  ✓ No manual Chinese typing needed!")
    print()
    print("Language: zh-TW (Traditional Chinese 繁體中文)")
    print()
    print("Server: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)

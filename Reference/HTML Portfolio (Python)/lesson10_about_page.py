# Lesson 10: Full About Page with Timeline and Skills
# Focus: Create the complete About Me page with personal story
#
# BUILDS ON LESSON 9:
# - Auto-translation with deep-translator
# - t(text) and b(text) functions
# - /projects reads from database
# - /games with all 7 games working
# - Parent dashboard with statistics
#
# NEW IN THIS LESSON:
# - Full /about page with:
#   - Introduction (auto-translated)
#   - Learning timeline (4 milestones)
#   - Skills with badges
#   - Favorite projects
#   - Future goals

from flask import Flask, render_template_string
import sqlite3
import os

# ============================================================
# Import auto-translation from Lesson 9
# ============================================================
try:
    from deep_translator import MyMemoryTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("⚠️  Run: pip install deep-translator")

def translate(text):
    """Translate using MyMemoryTranslator (same as Lesson 9)"""
    if not TRANSLATOR_AVAILABLE:
        return text
    if not text or not text.strip():
        return text
    try:
        translator = MyMemoryTranslator(source='en-US', target='zh-TW')
        result = translator.translate(text)
        return result if result else text
    except:
        return text

def t(text):
    """Translate to Chinese"""
    return translate(text)

def b(text):
    """Bilingual: Chinese + English"""
    chinese = translate(text)
    return f"{chinese} {text}" if chinese != text else text

app = Flask(__name__)

os.makedirs('static/games', exist_ok=True)

# CSS - Same as Lesson 9 + timeline and skill badge styles
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
    
    .game-frame { width: 100%; height: 650px; border: none; border-radius: 10px; }
    
    .checklist { list-style: none; padding: 0; }
    .checklist li { padding: 15px 0; border-bottom: 1px solid #e9ecef; padding-left: 35px; position: relative; }
    .checklist li::before { content: '✓'; position: absolute; left: 0; color: #2c5aa0; font-weight: bold; font-size: 20px; }
    
    .value-box { background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; border-left: 5px solid #4caf50; margin: 30px 0; }
    
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
    .stat-card { background: #f8f9fa; border-radius: 10px; padding: 30px; text-align: center; }
    .stat-number { font-size: 48px; font-weight: bold; color: #2c5aa0; }
    .stat-label { font-size: 16px; color: #666; margin-top: 10px; }
    
    /* NEW: Timeline styles for About page */
    .timeline { position: relative; padding: 20px 0; }
    .timeline-item { padding: 20px; margin-bottom: 20px; background: #f8f9fa; border-left: 4px solid #2c5aa0; border-radius: 8px; }
    .timeline-date { color: #2c5aa0; font-weight: bold; margin-bottom: 10px; }
    
    /* NEW: Skill badges */
    .skill-badges { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }
    .skill-badge { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; padding: 8px 16px; border-radius: 20px; font-size: 14px; }
    
    /* NEW: Highlight box */
    .highlight-box { background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3; margin: 20px 0; }
    
    .footer { background: #2c5aa0; color: white; text-align: center; padding: 20px; margin-top: 40px; }
</style>
"""

def get_nav(active_page):
    return f"""
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">🎓 我的編程作品集</div>
            <ul class="nav-links">
                <li><a href="/" class="{'active' if active_page == 'home' else ''}">主頁 Home</a></li>
                <li><a href="/projects" class="{'active' if active_page == 'projects' else ''}">作品 Projects</a></li>
                <li><a href="/games" class="{'active' if active_page == 'games' else ''}">遊戲 Games</a></li>
                <li><a href="/parent-dashboard" class="{'active' if active_page == 'parents' else ''}">👨‍👩‍👧 家長專區</a></li>
                <li><a href="/about" class="{'active' if active_page == 'about' else ''}">關於我 About</a></li>
            </ul>
        </div>
    </nav>
    """

@app.route('/')
def home():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>我的編程作品集 My Portfolio</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('home')}
        <div class="hero">
            <h1>歡迎來到我的編程世界</h1>
            <h1>Welcome to My Coding Portfolio</h1>
            <p>在 STEM WORK 學習編程的成果展示</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>Lesson 10: About Page 關於我頁面</h2>
                <p style="line-height: 2;">In Lesson 9, we added bilingual content.</p>
                <p style="line-height: 2;">In Lesson 10, we create the <strong>full About page</strong> with timeline and skills!</p>
                <p style="line-height: 2; margin-top: 15px;">Click <a href="/about" style="color: #2c5aa0; font-weight: bold;">關於我 About</a> to see the new page.</p>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
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
    except:
        all_projects = []
    conn.close()

    cards = ''
    icons = {'Python': '🐍', 'Web': '🌐', 'Game': '🎮', 'Desktop': '🖥️'}
    for proj in all_projects:
        icon = icons.get(proj[3], '🐍')
        cards += f'<div class="game-card"><div class="game-header">{icon}</div><div class="game-content"><div class="game-title">{proj[1]}</div><div class="game-desc">{proj[2][:60]}...</div><span class="game-type">{proj[3]}</span></div></div>'

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>作品 Projects</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('projects')}
        <div class="hero"><h1>我的作品集</h1><h1>My Projects</h1></div>
        <div class="container"><div class="section"><h2>🎯 專案展示 Project Gallery</h2><div class="game-grid">{cards}</div></div></div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

@app.route('/games')
def games():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>遊戲 Games</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('games')}
        <div class="hero"><h1>🎮 遊戲作品集</h1><h1>My Games Portfolio</h1></div>
        <div class="container">
            <div class="section">
                <h2>🎯 我的 JavaScript 遊戲</h2>
                <div class="game-grid">
                    <div class="game-card"><div class="game-header">🧮</div><div class="game-content"><div class="game-title">Math Quiz 數學測驗</div><a href="/play/math-quiz" class="play-btn">▶ Play Now</a></div></div>
                    <div class="game-card"><div class="game-header">🎨</div><div class="game-content"><div class="game-title">Color Game 顏色遊戲</div><a href="/play/color-game" class="play-btn">▶ Play Now</a></div></div>
                    <div class="game-card"><div class="game-header">⚡</div><div class="game-content"><div class="game-title">Reaction Game 反應遊戲</div><a href="/play/reaction-game" class="play-btn">▶ Play Now</a></div></div>
                </div>
            </div>
            <div class="section">
                <h2>🌐 Vercel 專業遊戲</h2>
                <div class="game-grid">
                    <div class="game-card"><div class="game-header">🐰</div><div class="game-content"><div class="game-title">Whack-a-Mole 打地鼠</div><a href="/play/mole-game" class="play-btn">▶ Play Now</a></div></div>
                    <div class="game-card"><div class="game-header">🎆</div><div class="game-content"><div class="game-title">Fireworks 煙火</div><a href="/play/fireworks" class="play-btn">▶ View Now</a></div></div>
                    <div class="game-card"><div class="game-header">⭐</div><div class="game-content"><div class="game-title">Star Fall 星星墜落</div><a href="/play/starfall" class="play-btn">▶ View Now</a></div></div>
                    <div class="game-card"><div class="game-header">👑</div><div class="game-content"><div class="game-title">King & Pigs 國王與豬</div><a href="/play/kingpigs" class="play-btn">▶ Play Now</a></div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

@app.route('/parent-dashboard')
def parent_dashboard():
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
    <head><title>家長專區 For Parents</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('parents')}
        <div class="hero"><h1>👨‍👩‍👧 給爸爸媽媽看</h1><h1>For My Parents</h1></div>
        <div class="container">
            <div class="section">
                <h2>🎉 我完成了 {total} 個專案！</h2>
                <p style="font-size: 18px;">I completed {total} projects at STEM WORK!</p>
            </div>
            <div class="section">
                <h2>📈 學習統計 Learning Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card"><div class="stat-number">{total}</div><div class="stat-label">專案 Projects</div></div>
                    <div class="stat-card"><div class="stat-number">{categories}</div><div class="stat-label">技術 Technologies</div></div>
                    <div class="stat-card"><div class="stat-number">7</div><div class="stat-label">遊戲 Games</div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

# ============================================================
# NEW IN LESSON 10: Full About Page
# ============================================================

@app.route('/about')
def about():
    """Full About page with timeline, skills, and personal story"""
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>關於我 About</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('about')}
        
        <div class="hero">
            <h1>關於我</h1>
            <h1>About Me</h1>
            <p>我的編程學習之旅 | My Coding Journey</p>
        </div>
        
        <div class="container">
            <div class="section">
                <h2>👋 自我介紹 Introduction</h2>
                <p style="line-height:2;font-size:17px;">
                    你好！我是一名在 STEM WORK 學習編程的學生。從 2024 年開始，我從完全不懂程式碼，到現在能夠獨立創建網站和遊戲。
                </p>
                <p style="line-height:2;font-size:17px;margin-top:10px;">
                    Hello! I'm a coding student at STEM WORK. Since 2024, I went from knowing nothing about code to creating websites and games independently.
                </p>
            </div>
            
            <div class="section">
                <h2>🌱 學習時間軸 Learning Timeline</h2>
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-date">📅 2024年1月 | January 2024</div>
                        <strong>開始學習 | Started Learning</strong>
                        <p style="margin-top:10px;">在 STEM WORK 開始我的編程之旅，學習 Flask 和 HTML 基礎。</p>
                        <p>Started my coding journey at STEM WORK, learning Flask and HTML basics.</p>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-date">📅 2024年3月 | March 2024</div>
                        <strong>第一個專案 | First Project</strong>
                        <p style="margin-top:10px;">完成了我的第一個 Python 專案！</p>
                        <p>Completed my first Python project!</p>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-date">📅 2024年6月 | June 2024</div>
                        <strong>掌握資料庫 | Mastered Database</strong>
                        <p style="margin-top:10px;">學會了使用 SQLite 資料庫！</p>
                        <p>Learned to use SQLite database!</p>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-date">📅 2024年9月 | September 2024</div>
                        <strong>完成作品集 | Completed Portfolio</strong>
                        <p style="margin-top:10px;">建立了這個完整的作品集網站！</p>
                        <p>Built this complete portfolio website!</p>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>💪 我學會的技能 Skills I Learned</h2>
                <div style="margin-bottom:20px;">
                    <h3 style="color:#2c5aa0;margin-bottom:10px;">編程語言 | Programming Languages</h3>
                    <div class="skill-badges">
                        <span class="skill-badge">🐍 Python</span>
                        <span class="skill-badge">🌐 HTML</span>
                        <span class="skill-badge">🎨 CSS</span>
                        <span class="skill-badge">⚡ JavaScript</span>
                    </div>
                </div>
                <div style="margin-bottom:20px;">
                    <h3 style="color:#2c5aa0;margin-bottom:10px;">框架與工具 | Frameworks & Tools</h3>
                    <div class="skill-badges">
                        <span class="skill-badge">🔥 Flask</span>
                        <span class="skill-badge">🗄️ SQLite</span>
                        <span class="skill-badge">🎮 Pygame</span>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>⭐ 我最喜歡的專案 My Favorite Projects</h2>
                <div class="highlight-box">
                    <h3 style="color:#1976d2;">🎮 互動遊戲合集 | Interactive Games</h3>
                    <p style="margin-top:10px;">我創建了 3 個 JavaScript 遊戲：數學測驗、顏色遊戲和反應速度測試。</p>
                    <p>I created 3 JavaScript games: Math Quiz, Color Game, and Reaction Speed Test.</p>
                </div>
                <div class="highlight-box">
                    <h3 style="color:#1976d2;">📊 這個作品集網站 | This Portfolio Website</h3>
                    <p style="margin-top:10px;">這是我最自豪的專案！包含資料庫、多頁面導航、遊戲整合。</p>
                    <p>This is my proudest project! Includes database, multi-page navigation, game integration.</p>
                </div>
            </div>
            
            <div class="section">
                <h2>🎯 未來目標 Future Goals</h2>
                <ul style="margin-left:20px;line-height:2;">
                    <li>學習更多 JavaScript 框架 (Learn more JS frameworks like React)</li>
                    <li>創建手機應用程式 (Create mobile applications)</li>
                    <li>參加編程比賽 (Participate in coding competitions)</li>
                    <li>成為全端開發者 (Become a full-stack developer)</li>
                </ul>
            </div>
        </div>
        
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

# Game routes - Same as Lesson 9
@app.route('/play/math-quiz')
def play_math_quiz():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Math Quiz</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🧮 Math Quiz</h1></div><div class="container"><div class="section"><iframe src="/static/games/math_quiz.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/color-game')
def play_color_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Color Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎨 Color Game</h1></div><div class="container"><div class="section"><iframe src="/static/games/color_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/reaction-game')
def play_reaction_game():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Reaction Game</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⚡ Reaction Game</h1></div><div class="container"><div class="section"><iframe src="/static/games/reaction_game.html" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/mole-game')
def play_mole():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Whack-a-Mole</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🐰 Whack-a-Mole</h1></div><div class="container"><div class="section"><iframe src="https://mole-game-psi.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/fireworks')
def play_fireworks():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Fireworks</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>🎆 Fireworks</h1></div><div class="container"><div class="section"><iframe src="https://firework-self.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/starfall')
def play_starfall():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>Star Fall</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>⭐ Star Fall</h1></div><div class="container"><div class="section"><iframe src="https://star-falling.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")

@app.route('/play/kingpigs')
def play_kingpigs():
    return render_template_string(f"""<!DOCTYPE html><html><head><title>King & Pigs</title><meta charset="UTF-8">{CLEAN_CSS}</head><body>{get_nav('games')}<div class="hero"><h1>👑 King & Pigs</h1></div><div class="container"><div class="section"><iframe src="https://king-and-pigs-test.vercel.app/" class="game-frame"></iframe></div></div></body></html>""")


if __name__ == '__main__':
    print("=" * 60)
    print("LESSON 10: Full About Page with Timeline and Skills")
    print("=" * 60)
    print()
    print("KEEPS from Lesson 9:")
    print("  ✓ Bilingual navigation and content")
    print("  ✓ All 7 game routes")
    print("  ✓ Parent dashboard with statistics")
    print()
    print("NEW in this lesson:")
    print("  ✓ Full /about page with:")
    print("      - Introduction (bilingual)")
    print("      - Learning timeline (4 milestones)")
    print("      - Skills with badges")
    print("      - Favorite projects")
    print("      - Future goals")
    print()
    print("Server: http://127.0.0.1:5000")
    print("Visit /about to see the full page!")
    print("=" * 60)
    app.run(debug=True, port=5000)

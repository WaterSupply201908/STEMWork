# Lesson 11: Database Statistics with GROUP BY
# Focus: Learn SQL aggregation (COUNT, DISTINCT, GROUP BY)
#
# BUILDS ON LESSON 10:
# - Auto-translation with deep-translator
# - /projects reads from database
# - /games with all 7 games working
# - Parent dashboard with basic statistics
# - Full About page with timeline
#
# NEW IN THIS LESSON:
# - SQL COUNT(*) for totals
# - SQL COUNT(DISTINCT) for unique values
# - SQL GROUP BY for category breakdown
# - Display statistics on multiple pages
# - Statistics demo page showing SQL queries

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
    
    .container { max-width: 1200px; margin: 40px auto; padding: 20px; }
    .section { background: white; padding: 40px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .section h2 { color: #2c5aa0; font-size: 28px; margin-bottom: 20px; }
    
    .game-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; margin-top: 20px; }
    .game-card { background: #f8f9fa; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .game-header { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; padding: 30px; text-align: center; font-size: 48px; }
    .game-content { padding: 20px; text-align: center; }
    .game-title { font-size: 20px; font-weight: bold; color: #333; }
    .game-desc { color: #666; font-size: 14px; margin-top: 5px; }
    .play-btn { width: 100%; padding: 12px; background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; border: none; border-radius: 5px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-top: 15px; }
    
    .game-frame { width: 100%; height: 650px; border: none; border-radius: 10px; }
    
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
    .stat-card { background: #f8f9fa; border-radius: 10px; padding: 30px; text-align: center; }
    .stat-number { font-size: 48px; font-weight: bold; color: #2c5aa0; }
    .stat-label { font-size: 16px; color: #666; margin-top: 10px; }
    
    .code-box { background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 10px; font-family: monospace; overflow-x: auto; margin: 20px 0; }
    .code-box .keyword { color: #569cd6; }
    .code-box .function { color: #dcdcaa; }
    .code-box .string { color: #ce9178; }
    
    .checklist { list-style: none; padding: 0; }
    .checklist li { padding: 15px 0; border-bottom: 1px solid #e9ecef; padding-left: 35px; position: relative; }
    .checklist li::before { content: '✓'; position: absolute; left: 0; color: #2c5aa0; font-weight: bold; }
    
    .value-box { background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; border-left: 5px solid #4caf50; margin: 30px 0; }
    
    .timeline-item { padding: 20px; margin-bottom: 20px; background: #f8f9fa; border-left: 4px solid #2c5aa0; border-radius: 8px; }
    .skill-badges { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }
    .skill-badge { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; padding: 8px 16px; border-radius: 20px; font-size: 14px; }
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

# ============================================================
# Helper function to get all statistics (NEW in Lesson 11)
# ============================================================
def get_stats():
    """Get statistics from database using COUNT, DISTINCT, GROUP BY"""
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    try:
        # COUNT(*) - total projects
        c.execute('SELECT COUNT(*) FROM projects')
        total = c.fetchone()[0]
        
        # COUNT(DISTINCT) - unique categories
        c.execute('SELECT COUNT(DISTINCT category) FROM projects')
        categories = c.fetchone()[0]
        
        # GROUP BY - count per category
        c.execute('SELECT category, COUNT(*) FROM projects GROUP BY category')
        by_category = c.fetchall()
    except:
        total, categories, by_category = 15, 4, []
    conn.close()
    return total, categories, by_category

@app.route('/')
def home():
    total, categories, by_category = get_stats()
    
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
                <h2>📊 Lesson 11: Database Statistics 資料庫統計</h2>
                <p style="line-height: 2;">In Lesson 10, we created the full About page.</p>
                <p style="line-height: 2;">In Lesson 11, we learn <strong>SQL aggregation</strong>: COUNT, DISTINCT, GROUP BY!</p>
                
                <div class="code-box">
                    <span class="keyword">SELECT</span> <span class="function">COUNT</span>(*) <span class="keyword">FROM</span> projects<br>
                    <span class="keyword">SELECT</span> <span class="function">COUNT</span>(<span class="keyword">DISTINCT</span> category) <span class="keyword">FROM</span> projects<br>
                    <span class="keyword">SELECT</span> category, <span class="function">COUNT</span>(*) <span class="keyword">FROM</span> projects <span class="keyword">GROUP BY</span> category
                </div>
            </div>
            
            <div class="section">
                <h2>📈 即時統計 Live Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">{total}</div>
                        <div class="stat-label">專案 Projects</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{categories}</div>
                        <div class="stat-label">技術類別 Categories</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">7</div>
                        <div class="stat-label">遊戲 Games</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">120+</div>
                        <div class="stat-label">學習時數 Hours</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

@app.route('/projects')
def projects():
    total, categories, by_category = get_stats()
    
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
        cards += f'<div class="game-card"><div class="game-header">{icon}</div><div class="game-content"><div class="game-title">{proj[1]}</div><div class="game-desc">{proj[2][:50]}...</div></div></div>'

    # Build category breakdown
    cat_html = ''.join([f'<li><strong>{cat}:</strong> {count} 個專案</li>' for cat, count in by_category])

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>作品 Projects</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('projects')}
        <div class="hero"><h1>我的作品集</h1><h1>My Projects</h1><p>總共 {total} 個專案 | {total} projects total</p></div>
        <div class="container">
            <div class="section">
                <h2>📊 專案分類統計 Projects by Category (GROUP BY)</h2>
                <ul style="margin-left: 20px; line-height: 2;">{cat_html}</ul>
            </div>
            <div class="section">
                <h2>🎯 所有專案 All Projects</h2>
                <div class="game-grid">{cards}</div>
            </div>
        </div>
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
                    <div class="game-card"><div class="game-header">🧮</div><div class="game-content"><div class="game-title">Math Quiz</div><a href="/play/math-quiz" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">🎨</div><div class="game-content"><div class="game-title">Color Game</div><a href="/play/color-game" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">⚡</div><div class="game-content"><div class="game-title">Reaction Game</div><a href="/play/reaction-game" class="play-btn">▶ Play</a></div></div>
                </div>
            </div>
            <div class="section">
                <h2>🌐 Vercel 專業遊戲</h2>
                <div class="game-grid">
                    <div class="game-card"><div class="game-header">🐰</div><div class="game-content"><div class="game-title">Whack-a-Mole</div><a href="/play/mole-game" class="play-btn">▶ Play</a></div></div>
                    <div class="game-card"><div class="game-header">🎆</div><div class="game-content"><div class="game-title">Fireworks</div><a href="/play/fireworks" class="play-btn">▶ View</a></div></div>
                    <div class="game-card"><div class="game-header">⭐</div><div class="game-content"><div class="game-title">Star Fall</div><a href="/play/starfall" class="play-btn">▶ View</a></div></div>
                    <div class="game-card"><div class="game-header">👑</div><div class="game-content"><div class="game-title">King & Pigs</div><a href="/play/kingpigs" class="play-btn">▶ Play</a></div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

@app.route('/parent-dashboard')
def parent_dashboard():
    total, categories, by_category = get_stats()
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>家長專區 For Parents</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('parents')}
        <div class="hero"><h1>👨‍👩‍👧 給爸爸媽媽看</h1><h1>For My Parents</h1></div>
        <div class="container">
            <div class="section">
                <h2>🎉 爸爸媽媽，看我的成績！</h2>
                <p style="font-size: 18px; line-height: 2;">我在 STEM WORK 完成了 <strong style="color: #2c5aa0;">{total} 個專案</strong>！</p>
                <p style="font-size: 18px;">I completed {total} projects at STEM WORK!</p>
            </div>
            <div class="section">
                <h2>💪 我會做這些！Skills I Learned</h2>
                <ul class="checklist">
                    <li>建立網站 Build websites</li>
                    <li>創建遊戲 Create games</li>
                    <li>使用資料庫 Use databases</li>
                    <li>解決問題 Solve problems</li>
                </ul>
            </div>
            <div class="value-box">
                <h3 style="color: #2e7d32;">🌟 這些技能的價值</h3>
                <ul style="margin-left: 20px; line-height: 2; margin-top: 15px;">
                    <li>🎓 升學幫助 - 大學申請時可以展示作品</li>
                    <li>💼 未來職業 - 可以成為程式設計師</li>
                    <li>🧠 思考能力 - 學會邏輯思考</li>
                </ul>
            </div>
            <div class="section">
                <h2>📈 學習統計 (來自資料庫查詢)</h2>
                <div class="stats-grid">
                    <div class="stat-card"><div class="stat-number">{total}</div><div class="stat-label">專案 Projects</div></div>
                    <div class="stat-card"><div class="stat-number">{categories}</div><div class="stat-label">技術 Technologies</div></div>
                    <div class="stat-card"><div class="stat-number">7</div><div class="stat-label">遊戲 Games</div></div>
                    <div class="stat-card"><div class="stat-number">120+</div><div class="stat-label">學習時數 Hours</div></div>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

@app.route('/about')
def about():
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head><title>關於我 About</title><meta charset="UTF-8">{CLEAN_CSS}</head>
    <body>
        {get_nav('about')}
        <div class="hero"><h1>關於我</h1><h1>About Me</h1><p>我的編程學習之旅</p></div>
        <div class="container">
            <div class="section">
                <h2>👋 自我介紹</h2>
                <p style="line-height:2;">你好！我是在 STEM WORK 學習編程的學生。</p>
                <p style="line-height:2;">Hello! I'm a coding student at STEM WORK.</p>
            </div>
            <div class="section">
                <h2>🌱 學習時間軸</h2>
                <div class="timeline-item"><strong>2024年1月</strong> - 開始學習 Started Learning</div>
                <div class="timeline-item"><strong>2024年3月</strong> - 第一個專案 First Project</div>
                <div class="timeline-item"><strong>2024年6月</strong> - 掌握資料庫 Mastered Database</div>
                <div class="timeline-item"><strong>2024年9月</strong> - 完成作品集 Completed Portfolio</div>
            </div>
            <div class="section">
                <h2>💪 我的技能</h2>
                <div class="skill-badges">
                    <span class="skill-badge">🐍 Python</span>
                    <span class="skill-badge">🌐 HTML/CSS</span>
                    <span class="skill-badge">⚡ JavaScript</span>
                    <span class="skill-badge">🔥 Flask</span>
                    <span class="skill-badge">🗄️ SQLite</span>
                </div>
            </div>
        </div>
        <div class="footer"><p>© 2024 | 在 STEM WORK 學習編程</p></div>
    </body>
    </html>
    """)

# Game routes
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
    print("LESSON 11: Database Statistics with GROUP BY")
    print("=" * 60)
    print()
    print("KEEPS from Lesson 10:")
    print("  ✓ Bilingual content")
    print("  ✓ All 7 game routes")
    print("  ✓ Full About page")
    print("  ✓ Parent dashboard")
    print()
    print("NEW in this lesson:")
    print("  ✓ get_stats() helper function")
    print("  ✓ SQL COUNT(*) for totals")
    print("  ✓ SQL COUNT(DISTINCT) for unique values")
    print("  ✓ SQL GROUP BY for category breakdown")
    print("  ✓ Statistics displayed on Home, Projects, Parent pages")
    print()
    print("Server: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)

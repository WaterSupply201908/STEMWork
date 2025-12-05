# Lesson 5: Multi-Page Navigation System (Refactored for Architecture)
# New Concept: Jinja2 Template Inheritance (The "Professional" Way)
# Instead of copying code 5 times, we use one BASE template.

from flask import Flask, render_template_string
from jinja2 import DictLoader

app = Flask(__name__)

# 1. THE BASE LAYOUT (Master Template)
# Contains the <head>, CSS, Navbar, and Footer that EVERY page shares.
BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
    <meta charset="UTF-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #333; }
        
        /* Navigation */
        .navbar { background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        .nav-container { max-width: 1000px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; height: 60px; align-items: center; }
        .logo { font-size: 20px; font-weight: bold; color: #2c5aa0; }
        .nav-links { display: flex; gap: 20px; }
        .nav-links a { text-decoration: none; color: #666; font-weight: 500; transition: color 0.3s; }
        .nav-links a:hover { color: #2c5aa0; }
        
        /* Active Link Highlighting */
        .nav-links a.active { color: #2c5aa0; border-bottom: 2px solid #2c5aa0; }

        /* Hero Section */
        .hero { background: linear-gradient(135deg, #2c5aa0, #0b3d91); color: white; text-align: center; padding: 50px 20px; margin-bottom: 30px; }
        .hero h1 { font-size: 36px; margin-bottom: 10px; }

        /* Main Content */
        .container { max-width: 1000px; margin: 0 auto; padding: 20px; min-height: 400px; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        
        /* Footer */
        footer { text-align: center; padding: 20px; color: #888; font-size: 14px; margin-top: 40px; border-top: 1px solid #ddd; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">My First Website</div>
            <div class="nav-links">
                <!-- Jinja2 logic to highlight active page (same sections as the final portfolio) -->
                <a href="/" class="{{ 'active' if active_page == 'home' else '' }}">Home</a>
                <a href="/projects" class="{{ 'active' if active_page == 'projects' else '' }}">Projects</a>
                <a href="/games" class="{{ 'active' if active_page == 'games' else '' }}">Games</a>
                <a href="/parent-dashboard" class="{{ 'active' if active_page == 'parents' else '' }}">For Parents</a>
                <a href="/about" class="{{ 'active' if active_page == 'about' else '' }}">About</a>
            </div>
        </div>
    </nav>

    <div class="hero">
        <h1>{% block header %}Welcome{% endblock %}</h1>
    </div>

    <div class="container">
        <div class="card">
            {% block content %}{% endblock %}
        </div>
    </div>

    <footer>
        <p>&copy; 2024 | Built with Flask & Jinja2</p>
    </footer>
</body>
</html>
"""

# Configure Flask to look for templates in this dictionary, not in files
app.jinja_loader = DictLoader({
    'base': BASE_TEMPLATE
})

# 2. CHILD TEMPLATES (Extend the Base)
HOME_HTML = """
{% extends "base" %}
{% block title %}Home - My First Website{% endblock %}
{% block header %}My First Website with Navigation{% endblock %}
{% block content %}
    <h2>Welcome back to the Lesson 4 project!</h2>
    <p>In Lesson 4, we built a homepage, a database page, and a projects gallery.</p>
    <p>In Lesson 5, we refactor the same <strong>idea</strong> into a layout that looks more like the final portfolio.</p>
    <ul>
        <li><strong>Home</strong> – main introduction and links to other pages</li>
        <li><strong>Projects</strong> – will show database projects in a grid (from Lesson 4)</li>
        <li><strong>Games</strong> – will list browser games (used in the final file)</li>
        <li><strong>For Parents</strong> – future parent dashboard using database statistics</li>
        <li><strong>About</strong> – explains the learning journey</li>
    </ul>
    <p>The navigation bar and footer now live in a single <code>base</code> template, similar to the final portfolio file.</p>
{% endblock %}
"""

PARENTS_HTML = """
{% extends "base" %}
{% block title %}For Parents{% endblock %}
{% block header %}Parent Dashboard (Preview){% endblock %}
{% block content %}
    <h2>Parent Dashboard Preview</h2>
    <p>In the final portfolio, there will be a full <strong>Parent Dashboard</strong> page.</p>
    <ul>
        <li>It will use the same navigation bar and layout as this lesson.</li>
        <li>It will read data from the <code>gaming_portfolio.db</code> database (created in Lessons 3 &amp; 4).</li>
        <li>It will show statistics like total projects and technologies learned.</li>
    </ul>
    <p>For Lesson 5, this page is a <strong>layout placeholder</strong> so students can practice multi-page navigation.</p>
{% endblock %}
"""

PROJECTS_HTML = """
{% extends "base" %}
{% block title %}Projects{% endblock %}
{% block header %}Projects Gallery{% endblock %}
{% block content %}
    <h2>Projects Gallery Page</h2>
    <p>In Lesson 4, this page displayed all 15 projects in a responsive CSS Grid.</p>
    <p>In Lesson 5, we simply show how this page fits into the shared navigation system.</p>
    <p>Later lessons can plug the real card HTML here using the same base template.</p>
{% endblock %}
"""

GAMES_HTML = """
{% extends "base" %}
{% block title %}Games{% endblock %}
{% block header %}Games (Coming Soon){% endblock %}
{% block content %}
    <h2>Games Page</h2>
    <p>In later lessons, this page will show JavaScript and Pygame web games.</p>
    <p>For now, it is a simple placeholder in our 5-page navigation system.</p>
{% endblock %}
"""

ABOUT_HTML = """
{% extends "base" %}
{% block title %}About{% endblock %}
{% block header %}About Me{% endblock %}
{% block content %}
    <h2>My Learning Journey</h2>
    <p>I started with "Hello World", then added a database (Lesson 3), a projects gallery (Lesson 4),</p>
    <p>and now a professional navigation system with template inheritance (Lesson 5).</p>
{% endblock %}
"""

# 3. ROUTES (Simple & Clean)
@app.route('/')
def home():
    # We pass the template string AND the 'base' template
    # In a real app, these would be files in a /templates folder
    return render_template_string(HOME_HTML, base=BASE_TEMPLATE, active_page='home')

@app.route('/projects')
def projects():
    return render_template_string(PROJECTS_HTML, base=BASE_TEMPLATE, active_page='projects')

@app.route('/games')
def games():
    return render_template_string(GAMES_HTML, base=BASE_TEMPLATE, active_page='games')

@app.route('/parent-dashboard')
def parent_dashboard():
    # Placeholder that represents the future Parent Dashboard page in the final portfolio
    return render_template_string(PARENTS_HTML, base=BASE_TEMPLATE, active_page='parents')

@app.route('/about')
def about():
    return render_template_string(ABOUT_HTML, base=BASE_TEMPLATE, active_page='about')

if __name__ == '__main__':
    print("LESSON 5: Architecture & Inheritance")
    print("Notice how the code is cleaner and we have 'Active' link highlighting!")
    print("Server: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

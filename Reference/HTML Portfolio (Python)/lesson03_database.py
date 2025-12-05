# Lesson 3: Database Integration
# NEW CONCEPT: Connecting a Database (SQLite) to Flask
# In Lesson 2, we just had static HTML/CSS.
# In Lesson 3, we learn how to store and retrieve data!

from flask import Flask
import sqlite3  # NEW: Library for database
import datetime
import csv      # NEW: Library for reading CSV files
import os       # NEW: Library for file paths

app = Flask(__name__)

# Function to create database
def create_database():
    # NEW: Connect to a file-based database
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    
    # Create projects table
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT,
        tech_stack TEXT,
        difficulty TEXT,
        screenshot TEXT,
        thumbnail TEXT,
        source_code TEXT,
        playable BOOLEAN,
        url TEXT,
        date_created TEXT,
        featured BOOLEAN
    )''')
    
    # Delete old data
    c.execute('DELETE FROM projects')
    
    # NEW: Read data from an external CSV file instead of hardcoding it
    # This makes it easier to edit project data without touching Python code
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'projects_data.csv')

    projects_data = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            projects_data.append((
                int(row['id']),
                row['title'],
                row['description'],
                row['category'],
                row['tech_stack'],
                row['difficulty'],
                row['screenshot'],
                row['thumbnail'],
                row['source_code'],
                int(row['playable']),
                row['url'],
                row['date_created'],
                int(row['featured'])
            ))

    # NEW: Insert multiple rows at once using SQL
    c.executemany('INSERT INTO projects VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', projects_data)
    conn.commit()
    conn.close()
    print("Database created: gaming_portfolio.db from projects_data.csv")

# Create database on startup
create_database()

# CSS Styling (from Lesson 2 + database styles)
CLEAN_CSS = """
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Arial, sans-serif; background: #f8f9fa; color: #333; line-height: 1.6; }

header { background: linear-gradient(135deg, #2c5aa0, #4a90e2); color: white; text-align: center; padding: 60px 20px; }
header h1 { font-size: 48px; margin-bottom: 10px; }
header p { font-size: 20px; }

nav { background: white; padding: 15px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
nav a { color: #2c5aa0; text-decoration: none; padding: 10px 15px; font-weight: 500; }
nav a:hover { background: #2c5aa0; color: white; border-radius: 5px; }

main { max-width: 1000px; margin: 40px auto; padding: 20px; }
section { background: white; padding: 30px; margin-bottom: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
section h2 { color: #2c5aa0; margin-bottom: 15px; }
section h3 { color: #2c5aa0; margin-top: 20px; margin-bottom: 10px; }
section ul, section ol { margin-left: 20px; margin-top: 10px; }
section li { margin-bottom: 8px; }

form { margin-top: 20px; }
form label { color: #333; font-weight: 500; }
form input[type="text"], form textarea { width: 100%; padding: 10px; margin-top: 5px; border: 2px solid #2c5aa0; border-radius: 5px; font-family: Arial, sans-serif; }
form input[type="radio"] { margin-right: 8px; margin-top: 10px; }
form button { background: #2c5aa0; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 10px; }
form button:hover { background: #1e4070; }

.container { max-width: 1200px; margin: 40px auto; padding: 20px; }
.content { background: white; padding: 30px; border-radius: 10px; 
box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 30px; }
.content table { width: 100%; border-collapse: collapse; margin-top: 15px; }
.content th, .content td { padding: 12px; text-align: left; border-bottom: 1px solid #e0e0e0; }
.content th { background: #f8f9fa; color: #2c5aa0; font-weight: bold; }
.content .stats { display: grid; grid-template-columns: 
repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }
.content .stat-box { background: #f8f9fa; padding: 20px; 
border-radius: 8px; text-align: center; border-left: 4px solid #2c5aa0; }
.content .stat-box h2 { color: #2c5aa0; font-size: 36px; margin-bottom: 5px; }
.content .stat-box p { color: #666; font-size: 14px; }

footer { background: #2c5aa0; color: white; text-align: center; padding: 30px 20px; margin-top: 60px; }
footer hr { border: none; border-top: 1px solid rgba(255,255,255,0.3); margin-bottom: 15px; }
</style>
"""

# Route 1: Homepage (from Lesson 2 + database link)
@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_year = datetime.datetime.now().year
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Website</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {CLEAN_CSS}
    </head>
    <body>
        <header>
            <h1>Hello World!</h1>
            <p>My first Flask webpage with database integration.</p>
        </header>

        <nav>
            <a href="#about">About</a> |
            <a href="#learning">Learning</a> |
            <a href="#skills">Skills</a> |
            <a href="#feedback">Feedback</a> |
            <a href="/database">Database</a>
        </nav>

        <main>
            <section id="about">
                <h2>About Me</h2>
                <p>I am learning web development at STEM WORK.</p>
                <p><strong>Current server time:</strong> {current_time}</p>
                <p>Need to search something? <a href="https://google.com" target="_blank">Visit Google</a></p>
            </section>

            <section id="learning">
                <h2>What This Page Shows</h2>
                <ul>
                    <li>Basic HTML structure</li>
                    <li>Headings and paragraphs</li>
                    <li>Lists and links</li>
                    <li>Form inputs (text, radio, textarea, button)</li>
                    <li>Dynamic time from Python</li>
                    <li>CSS styling with STEM WORK colors</li>
                    <li><strong>SQLite database integration!</strong></li>
                </ul>
            </section>

            <section id="skills">
                <h2>My Learning Steps</h2>
                <ol>
                    <li>Install Python and Flask</li>
                    <li>Create a Flask app</li>
                    <li>Return HTML from a route</li>
                    <li>Open the page in a browser</li>
                    <li>Add CSS to make it beautiful</li>
                    <li>Create a database with SQLite!</li>
                </ol>
                <h3>Starter Skill Set</h3>
                <ul>
                    <li>Python + Flask basics</li>
                    <li>HTML page layout</li>
                    <li>CSS styling (colors, spacing, shadows)</li>
                    <li>SQLite database (CREATE TABLE, INSERT, SELECT)</li>
                    <li>Reading server messages</li>
                </ul>
            </section>

            <section id="feedback">
                <h2>Feedback Form</h2>
                <form>
                    <label for="name">Your Name:</label><br>
                    <input type="text" id="name" name="name" placeholder="Enter your name"><br><br>
                    
                    <label>How do you like this page?</label><br>
                    <input type="radio" id="great" name="rating" value="great">
                    <label for="great">Great!</label><br>
                    <input type="radio" id="good" name="rating" value="good">
                    <label for="good">Good</label><br>
                    <input type="radio" id="okay" name="rating" value="okay">
                    <label for="okay">Okay</label><br><br>
                    
                    <label for="comments">Comments:</label><br>
                    <textarea id="comments" name="comments" rows="4" placeholder="Your feedback..."></textarea><br><br>
                    
                    <button type="submit">Submit Feedback</button>
                </form>
            </section>

            <section id="database-link">
                <h2>Check Out My Database!</h2>
                <p>I created a database with 15 projects. <a href="/database" style="color: #2c5aa0; 
                font-weight: bold;">Click here to view database →</a></p>
            </section>
        </main>

        <footer>
            <hr>
            <p>&copy; {current_year} | Learning at STEM WORK</p>
        </footer>
    </body>
    </html>
    """

# Route 2: Database Page (NEW!)
@app.route('/database')
def database():
    # NEW: Connect to database and get all projects
    conn = sqlite3.connect('gaming_portfolio.db')
    c = conn.cursor()
    
    # NEW: Execute SQL query to get ALL data
    c.execute('SELECT * FROM projects')
    all_projects = c.fetchall()
    
    # NEW: Execute SQL query with aggregation (GROUP BY)
    c.execute('SELECT category, COUNT(*) FROM projects GROUP BY category')
    by_category = c.fetchall()
    
    # NEW: Execute SQL query to count unique items
    c.execute('SELECT COUNT(DISTINCT category) FROM projects')
    unique_categories = c.fetchone()[0]
    
    conn.close()
    
    # Generate statistics boxes
    stats_html = f"""
    <div class="stats">
        <div class="stat-box">
            <h2>{len(all_projects)}</h2>
            <p>Total Projects</p>
        </div>
        <div class="stat-box">
            <h2>{unique_categories}</h2>category
            <p>Categories</p>
        </div>
    </div>
    """
    
    # Generate category breakdown
    category_html = "<h3>Projects by Category:</h3><ul>"
    for cat, count in by_category:
        category_html += f"<li><strong>{cat}:</strong> {count} projects</li>"
    category_html += "</ul>"
    
    # Generate projects table
    table_html = "<h3>All Projects:</h3><table><tr><th>ID</th><th>Title</th><th>Category</th><th>Difficulty</th></tr>"
    for proj in all_projects:
        table_html += f"<tr><td>{proj[0]}</td><td>{proj[1]}</td><td>{proj[3]}</td><td>{proj[5]}</td></tr>"
    table_html += "</table>"
    
    current_year = datetime.datetime.now().year
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Database</title>
        <meta charset="UTF-8">
        {CLEAN_CSS}
    </head>
    <body>
        <header>
            <h1>Database Information</h1>
            <p>15 Projects Stored in SQLite Database</p>
        </header>

        <nav>
            <a href="/">Home</a> |
            <a href="/database">Database</a>
        </nav>
        
        <main>
            <div class="content">
                {stats_html}
            </div>
            
            <div class="content">
                {category_html}
            </div>
            
            <div class="content">
                {table_html}
            </div>
        </main>
        
        <footer>
            <hr>
            <p>&copy; {current_year} | Learning at STEM WORK</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("LESSON 3: Database Integration")
    print("Server: http://127.0.0.1:5000")
    print("Visit /database to see database info")
    print("")
    app.run(debug=True, port=5000)

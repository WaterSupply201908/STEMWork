# Lesson 1: Flask Introduction & Hello World
# Duration: 1 hour
# Objective: Create your first webpage with Flask

"""
LEARNING OBJECTIVES:
- Understand what Flask is and how it works
- Set up Flask environment
- Create a simple homepage
- Learn basic HTML structure
- Run a local web server
"""

from flask import Flask
import datetime

app = Flask(__name__)

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
    </head>
    <body>
        <header>
            <h1>Hello World!</h1>
            <p>My first Flask webpage.</p>
        </header>

        <nav>
            <a href="#about">About</a> |
            <a href="#learning">Learning</a> |
            <a href="#skills">Skills</a> |
            <a href="#feedback">Feedback</a> |
            <a href="#next">Next Step</a>
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
                </ul>
            </section>

            <section id="skills">
                <h2>My Learning Steps</h2>
                <ol>
                    <li>Install Python and Flask</li>
                    <li>Create a Flask app</li>
                    <li>Return HTML from a route</li>
                    <li>Open the page in a browser</li>
                </ol>
                <h3>Starter Skill Set</h3>
                <ul>
                    <li>Python + Flask basics</li>
                    <li>HTML page layout</li>
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
                    <textarea id="comments" name="comments" rows="4" cols="40" placeholder="Your feedback..."></textarea><br><br>
                    
                    <button type="submit">Submit Feedback</button>
                </form>
            </section>

            <section id="next">
                <h2>Next Step</h2>
                <p>In Lesson 2 we will add CSS to make this page look professional.</p>
            </section>
        </main>

        <footer>
            <hr>
            <p>&copy; {current_year} | Learning at STEM WORK</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("LESSON 1: Flask Basics & Hello World")
    print("Server: http://127.0.0.1:5000")
    print("")
    app.run(debug=True, port=5000)

"""
WHAT STUDENTS LEARN IN LESSON 1:

Flask Basics:
- Import Flask and create app
- Define a route with @app.route('/')
- Return HTML content from a function
- Run development server with app.run()

HTML Basics:
- Page structure (DOCTYPE, html, head, body)
- Headings (h1, h2, h3)
- Paragraphs (p)
- Lists (ul for unordered, ol for ordered, li for items)
- Horizontal rule (hr)
- Bold text (strong)

Dynamic Content:
- Using Python datetime to show current time
- Using f-strings to insert dynamic data into HTML

LESSON 2: We'll add CSS styling to make this homepage look professional with 
the STEM WORK color scheme, navigation bar, hero section, and clean design.
"""

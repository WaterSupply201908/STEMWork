from flask import Flask
import datetime

app = Flask(__name__)

# STEM WORK Style CSS
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

footer { background: #2c5aa0; color: white; text-align: center; padding: 30px 20px; margin-top: 60px; }
footer hr { border: none; border-top: 1px solid rgba(255,255,255,0.3); margin-bottom: 15px; }
</style>
"""

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
            <p>My first Flask webpage with CSS styling.</p>
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
                    <li><strong>CSS styling with STEM WORK colors!</strong></li>
                </ul>
            </section>

            <section id="skills">
                <h2>My Learning Steps</h2>
                <ol>
                    <li>Install Python and Flask</li>
                    <li>Create a Flask app</li>
                    <li>Return HTML from a route</li>
                    <li>Open the page in a browser</li>
                    <li>Add CSS to make it beautiful!</li>
                </ol>
                <h3>Starter Skill Set</h3>
                <ul>
                    <li>Python + Flask basics</li>
                    <li>HTML page layout</li>
                    <li>CSS styling (colors, spacing, shadows)</li>
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

            <section id="next">
                <h2>Next Step</h2>
                <p>In Lesson 3 we will add a database to store project information.</p>
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
    print("LESSON 2: CSS Styling & STEM WORK Design")
    print("Server: http://127.0.0.1:5000")
    print("")
    app.run(debug=True, port=5000)

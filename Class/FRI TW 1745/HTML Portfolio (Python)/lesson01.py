from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home() :
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_year = datetime.datetime.now().year

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Webiste</title>
        <meta charset="utf-8">
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
                <p><strong>Current server time : </strong>{current_time}</p>
                <p>Need to search something? <a href="https://google.com" target="_blank">Visit Google</a></p>
            </section>
            <section id="learning">
            </section>
            <section id="skills">
            </section>
            <section id="feedback">
            </section>
            <section id="next">
            </section>
        </main>

        <footer>
            <hr>
            <p>&copy; {current_year} | Learning at STEM WORK</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__' :
    print("Lesson 1 : Flask Basics & Hello World")
    print("Server : http://127.0.0.1:5000")
    print("")

    app.run(debug=True, port=5000)

from flask import Flask, render_template, redirect
import subprocess
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/end')
def end_ai():
    # Start the AI app (ap.py) as a background process
    subprocess.Popen(['python', 'ap.py'])

    # Optionally, redirect to a new page or notify the user
    return "AI Drawing App Started!", 200
@app.route('/start')
def start_ai():
    # Start the Streamlit app using subprocess
    subprocess.Popen(['streamlit', 'run', 'ai.py'])

    # Automatically open the Streamlit app in the default web browser
    webbrowser.open('http://localhost:8501')

    # Redirect to the Streamlit app
    return redirect('http://localhost:8501')

if __name__ == "__main__":
    app.run(debug=True)
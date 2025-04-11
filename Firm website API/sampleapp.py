from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask Website!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# To run the sample Flask application, use the command:    
# python3 sampleapp.py
# Output:
# Running on http://127.0.0.1:5000
# Press CTRL+C to quit
##########################################################################
# Make sure to install Flask using pip if you haven't already:
# pip install Flask
# This code creates a simple Flask web application that displays "Hello, Flask Website!" when accessed at the root URL.
# The app runs in debug mode, which is useful for development as it provides detailed error messages and auto-reloads the server when code changes are made.


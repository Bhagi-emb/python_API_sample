from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)

# To run the sample Flask application, use the command:    
# python3 app.py
# Output:
# Running on http://127.0.0.1:5000
# Press CTRL+C to quit
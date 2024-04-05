from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

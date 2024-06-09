from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        # You can process the data here (e.g., save to a database)

        return f"<h2>Registration Successful</h2><p>Name: {name}</p><p>Email: {email}</p><p>Phone: {phone}</p>"
    return "Invalid request method."

if __name__ == '__main__':
    app.run(debug=True)


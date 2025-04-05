from flask import Flask, render_template, request, jsonify
import re
from validation import validate_username, validate_email, validate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registrationform.html')

@app.route('/validate-password', methods=['POST'])
def validate_password_route():
    data = request.get_json()
    password = data.get('password', '')
    errors = validate_password(password)
    return jsonify({'errors': errors})

@app.route('/validate-username', methods=['POST'])
def validate_username_route():
    data = request.get_json()
    username = data.get('username', '')
    errors = validate_username(username)
    return jsonify({'errors': errors})

@app.route('/validate-email', methods=['POST'])
def validate_email_route():
    data = request.get_json()
    email = data.get('email', '')
    errors = validate_email(email)
    return jsonify({'errors': errors})

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    errors = validate_password(password)
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        errors.append("Passwords do not match")
    if errors:
        return render_template('registrationform.html', server_error="<br>".join(errors))
    return f"User {username} registered successfully!"

if __name__ == '__main__':
    app.run(debug=True)
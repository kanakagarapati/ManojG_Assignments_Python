from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def validate_username(username):
    errors = []
    if len(username) < 5:
        errors.append("At least 5 characters")
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        errors.append("User Name allows only alphanumeric characters and underscores")
    return errors

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("At least one digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("At least one special character")
    return errors

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
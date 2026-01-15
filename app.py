from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password_logic(length, use_upper, use_lower, use_numbers, use_special):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return None

    return "".join(random.choice(char_pool) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    try:
        length = int(data.get('length', 12))
        use_upper = data.get('upper', True)
        use_lower = data.get('lower', True)
        use_numbers = data.get('numbers', True)
        use_special = data.get('special', True)

        if length <= 0 or length > 128:
            return jsonify({"error": "Length must be between 1 and 128"}), 400

        result = generate_password_logic(length, use_upper, use_lower, use_numbers, use_special)
        
        if result is None:
            return jsonify({"error": "Select at least one character type"}), 400

        return jsonify({"password": result})
    except ValueError:
        return jsonify({"error": "Invalid length"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

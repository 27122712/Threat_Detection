from flask import Flask, request, jsonify

app = Flask(__name__)

# Default homepage route
@app.route('/')
def home():
    return "Flask server is running!"

# API route for testing
@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()
    return jsonify({"message": "URL checked successfully", "data": data})

if __name__ == '__main__':
    app.run(debug=True)

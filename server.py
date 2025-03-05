from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])  # Allow POST requests
def detect_threat():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    url = data['url']
    
    # Dummy response (Replace this with your threat detection logic)
    if "malicious" in url:
        return jsonify({"threat": True, "message": "This URL is potentially malicious."})
    else:
        return jsonify({"threat": False, "message": "This URL seems safe."})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
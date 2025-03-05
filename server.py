from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Change port to 10000 or use Render's default port
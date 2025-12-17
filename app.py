from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from ECS CI/CD Pipeline — Version 2 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



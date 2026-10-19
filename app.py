from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando en Render - Version 3 - Rafael"

if __name__ == "__main__":
    app.run()



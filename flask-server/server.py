from flask import Flask

app = Flask(__name__)

# API ROUTES HERE

if __name__ == "__main__":
    app.run(debug=True)
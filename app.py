from flask import Flask
from routes import queue_bp

app = Flask(__name__)
app.register_blueprint(queue_bp)

if __name__ == '__main__':
    app.run(debug=True)

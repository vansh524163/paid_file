from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Vansh-Yadav'

if __name__ == "__main__":
    # Get the port from the environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Run the app on the specified port and make it accessible externally
    app.run(host='0.0.0.0', port=port)

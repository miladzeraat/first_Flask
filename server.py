from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/no_content')
def no_content():
    # Returning a tuple with a custom HTTP status code (204) and a JSON message
    return jsonify({"message": "No content found"}), 204

if __name__ == '__main__':
    app.run(debug=True)



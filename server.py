from flask import Flask, make_response

app = Flask(__name__)

@app.route('/exp')
def index_explicit():
    # Creating a custom response with make_response()
    response = make_response("Custom response with status 200", 200)

    return response

if __name__ == '__main__':
    app.run(debug=True)


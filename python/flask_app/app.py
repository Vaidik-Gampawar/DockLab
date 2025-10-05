from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route
@app.route('/api/status')
def status():
    return jsonify({"message": "Server is up and running"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


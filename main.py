from flask import Flask, request, jsonify, send_file, send_file
from film_time import calculate_film_development_time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')



@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    uses = data.get('uses', 0)
    
    try:
        uses = int(uses)
        if uses < 1 or uses > 24:
            return jsonify({'error': "Please enter an integer between 1 and 24."}), 400
    except ValueError:
        return jsonify({'error': "Invalid input. Please enter an integer."}), 400
    
    result = calculate_film_development_time(uses)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


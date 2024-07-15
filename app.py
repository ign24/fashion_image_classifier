from flask import Flask, request, jsonify, render_template
from model import process_image

app = Flask(__name__)

@app.route('/')

def upload_file():

    return render_template('upload.html')

@app.route('/predict', methods=['POST'])


def predict():

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400


    predictions = process_image(file)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
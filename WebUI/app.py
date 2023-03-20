from ultralytics import YOLO
from flask import Flask, render_template, request, jsonify
import os
from PIL import Image

template = {0:"Hamburguesa", 1:"Pollo frito", 2:"Donut", 3: "Patatas fritas", 4: "Perrito caliente", 5:"Pizza", 6:"Sandwich", 7:"Patatas rellenas"}

model = YOLO("best.pt")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file found'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file found'})
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            img = Image.open(filename)
            classification = model(img)
            prediction = classification[0].probs.argmax().item()
            prediction = template[prediction]
            return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

from ultralytics import YOLO
from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image

template = {0:"Hamburguesa", 1:"Pollo frito", 2:"Donut", 3: "Patatas fritas", 4: "Perrito caliente", 5:"Pizza", 6:"Sandwich", 7:"Patatas rellenas"}

model = YOLO("best.pt")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#         if file:
#             filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filename)
#             img = Image.open(filename)
#             clasification = model(img)
#             prediction = clasification[0].probs.argmax().item()
#             return f"Clase predicha: {prediction}"

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            img = Image.open(filename)
            clasification = model(img)
            prediction = clasification[0].probs.argmax().item()
            prediction = template[prediction]
            return f'''
                <h1>Tu imagen contiene: {prediction}</h1>
                <a href="/" class="back-button">Volver</a>
            '''

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
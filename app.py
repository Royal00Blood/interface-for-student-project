import os
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route("/")
def index():
    uploaded = os.listdir(UPLOAD_FOLDER)

    labels = ["A", "B", "C", "D", "E", "F", "G"]
    data1 = [10, 8, 15, 9, 14, 7, 20]
    data2 = [7, 12, 6, 11, 8, 13, 5]
    data3 = [15, 10, 12, 7, 18, 9, 11]

    result_img = None
    img_path = os.path.join(RESULTS_FOLDER, "output.png")
    if os.path.exists(img_path):
        result_img = "output.png"

    return render_template(
        "index.html",
        uploaded_files=uploaded,
        chart_labels=labels,
        chart_data1=data1,
        chart_data2=data2,
        chart_data3=data3,
        result_img=result_img
    )

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file and file.filename != "":
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
    return redirect("/")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/read/<filename>")
def read_file(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except:
        content = "Cannot read file"
    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
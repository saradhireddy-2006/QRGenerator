from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)
qr_folder = "static/qr"
os.makedirs(qr_folder, exist_ok = True)

@app.route("/", methods = ["GET", "POST"])
def home():
    qr_image = None
    data = ""
    if request.method == "POST":
        data = request.form.get("text")
        if data.strip():
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="blue", back_color="white")
            filename = "qr_code.png"
            filepath = os.path.join(qr_folder, filename)
            img.save(filepath)
            qr_image = "qr/" +filename
    return render_template("index.html", qr_image = qr_image, text = data)
if __name__ == "__main__":
    app.run(debug = True)

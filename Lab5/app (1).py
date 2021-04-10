from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        text2 = request.form.get('textbox2')
        text3 = request.form.get('textbox3')
        text4 = request.form.get('textbox4')
        return render_template("index.html",
        output = backend.meters_feet(float(text),float(text2),float(text3),float(text4)),
        user_text = text,user_text2=text2,user_text3=text3,user_text4=text4)

if __name__ == "__main__":
    app.run()
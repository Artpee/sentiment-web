from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# หน้าแรก
@app.route("/")
def home():
    return render_template("index.html")

# หน้าแนะนำโครงงาน
@app.route("/about")
def about():
    return render_template("about.html")

# หน้า dashboard
@app.route("/dashboard")
def dashboard(
     total_reviews = f"{10000:,}"
):
    return render_template("dashboard.html", total_reviews=total_reviews)


# หน้าสินค้า
import pandas as pd

@app.route("/product")
def product():
     
    return render_template("product.html")

# หน้า creator
@app.route("/creator")
def creator():
    return render_template("creator.html")

# API ทดสอบ
@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]

    if "good" in text or "great" in text:
        result = "Positive"
    elif "bad" in text or "cheap" in text:
        result = "Negative"
    else:
        result = "Neutral"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
from flask import Flask
from flask import render_template, request

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/gad-form", methods=["GET", "POST"])
def gad_form():
    if request.method == "POST":
        print(request.form)
        data = dict((key, request.form.getlist(key)) for key in request.form.keys())
        print("Dict--->", data)
        total = 0
        for k in data:
            value = int(data[k][0])
            total += value
        result = calculate_gad_result(total=total)
        return render_template("submit.html", test_output=result)
    return render_template("gad.html")


@app.route("/products", methods=["GET"])
def product():
    return render_template("products.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


def calculate_gad_result(total):
    if total < 5:
        result = "No Anxiety"
    elif total >= 5 and total < 10:
        result = "Mild Anxiety"
    elif total >= 10 and total < 15:
        result = "Moderate Anxiety"
    else:
        result = "Severe Anxiety"
    return result


# run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

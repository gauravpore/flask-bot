from flask import Flask
from flask import render_template, request

# creates a Flask application, named app
app = Flask(__name__, static_url_path="/static")

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():
    return render_template("home.html")


# @app.route("/form", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         # getting input with name = fname in HTML form
#         print(request.form)
#         data = data = dict(
#             (key, request.form.getlist(key)) for key in request.form.keys()
#         )
#         first_name = data.get("name")
#         age = data.get("age")
#         print(data)
#         # getting input with name = lname in HTML form
#         # last_name = request.form.get("lname")
#         return (
#             "Your name is " + first_name[0] + " and you are " + age[0] + " years old."
#         )
#     return render_template("test2.html")


@app.route("/gad-form", methods=["GET", "POST"])
def gad_form():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        print(request.form)
        data = data = dict(
            (key, request.form.getlist(key)) for key in request.form.keys()
        )
        first_name = data.get("name")
        age = data.get("age")
        print(data)
        # getting input with name = lname in HTML form
        # last_name = request.form.get("lname")\
        # result = process_test_results()
        result = "Anxiety Disorder"
        return render_template("submit.html", test_output=result)
    return render_template("gad.html")


@app.route("/products", methods=["GET"])
def product():
    return render_template("products.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


# run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

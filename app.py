from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    myName = "Anshuman"
    return render_template("index.html", name=myName)

@app.route("/about")
def hello_about():
    names = list(["apple", "mango", "orange", "rose"])
    return render_template("about.html", names=names)

@app.route("/form", methods=["POST"])
def hello_form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    return render_template("subscribe.html", first=first_name, last=last_name, email=email)

# static(for static collection of the data), templates(for serving tht html files)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="") for changing the hostname
    # app.run(debug=True, port=8000) for changing the port
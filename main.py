from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/risco")
def risco():
    return render_template("risco.html")

@app.route("/fauna-flora")
def fauna():
    return render_template("fauna-flora.html")

@app.route("/incendio")
def relatar():
    return render_template("incendio.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
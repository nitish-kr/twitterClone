from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "SECRET"


from controllers import user as userController

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/loginSubmit", methods=["POST"])
def loginSubmit():
    isLoginSuccessful, message = userController.login(request.form["username"], request.form["password"])
    print isLoginSuccessful
    print message
    if isLoginSuccessful:
        return redirect(url_for("home"))
    else:
        flash(message)
        return redirect(url_for("login"))


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/registrationSubmit", methods=["POST"])
def registrationSubmit():
    userController.register(request.form["username"], request.form["password"], request.form["fullName"])
    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    userController.logout()
    return redirect(url_for("login"))


@app.route("/home")
def home():
    return "Logged in user id is: {}".format(session.get("loggedInUserId", "NA"))


if __name__ == "__main__":
    app.run(debug=True)

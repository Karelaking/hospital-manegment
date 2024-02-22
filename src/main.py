import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users-profile")
def usersProfile():
    return render_template('users-profile.html')

@app.route("/pages-faq")
def pagesFaq():
    return render_template('pages-faq.html')

@app.route("/pages-contact")
def pagesContact():
    return render_template('pages-contact.html')

@app.route("/pages-register")
def pagesRegister():
    return render_template("pages-register.html")

# @app.route("/pages-register")
# def pagesRegister():
#     return render_template('pages-register.html')

@app.route("/pages-blank")
def pagesBlank():
    return render_template('pages-blank.html')

@app.route("/pages-login")
def pagesLogin():
    return render_template('pages-login.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()

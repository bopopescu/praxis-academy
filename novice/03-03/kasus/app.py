from flask import Flask, render_template, url_for, redirect, request, session
import mysql.connector as mariadb

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKeyKu2020"

@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('sukses_req'))
    
    #jika tombol button di klik -> request POST
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("email : ", email)
        print("pass : ", password)
        # jika email dan password benar
        if email == 'danayoga@gmail.com' and password == 'mastur420':
            session['email'] = email

            return redirect(url_for('sukses_req'))

        #jika email atau password salah
        else:
            #harus login dulu
            return redirect(url_for('index'))


    return render_template("index.html")

@app.route("/sukses")
def sukses_req():
    conn=mariadb.connect(host="192.168.1.91", user="danayoga", passwd="mastur", database="kasus0205")
    cur=conn.cursor()
    cur.execute("select * from movie")
    ls=cur.fetchall()
    return render_template("sukses.html", ls=ls)


@app.route("/about")
def about():
    if "email" in session:
        return render_template("about.html")
    else:
        return redirect(url_for('index'))


@app.route("/contact")
def contact():
    if "email" in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout_akun():
    if "email" in session:
        session.pop("email")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for('about'))

@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True)
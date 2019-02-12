import re
from db.base import DbManager
from db.models import User
from flask import request, flash, redirect, session, jsonify

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')


def create_user(email, name, password, telp):
    db = DbManager()
    user = User()
    user.name = name
    user.email = email
    user.telp = telp
    user.password = password
    return db.save(user)

def edit_user(user_id, name, password):
    db = DbManager()
    user = db.open().query(User).filter(User.id == user_id).one()
    user.name = name
    user.password = password
    return db.update(user)

def check_login(email, password):
    db = DbManager()
    return db.open().query(User).filter(User.email == email, User.password == password).one()

def get_user_by_id(user_id):
    db = DbManager()
    return db.open().query(User).filter(User.id == user_id).one()


def verifikasi_then_create_or_edit_user(tipe):
    name = request.form.get("name")
    email = request.form.get("email")
    telp = request.form.get("telp")
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    if password == confirm:
        if password is not None and len(password)>7 and re.search('[0-9]',password) is not None and re.search('[a-z]',password) is not None:
            if EMAIL_REGEX.match(email):
                try:
                    if tipe == "create":
                        user = create_user(email, name, password, telp)
                        session['user_id'] = user.id
                        return user
                    else:
                        edit_user(session['user_id'], name, password)
                        flash('Edit user Berhasil')
                    return redirect('/')
                except:
                    flash("Email already registered")
                    return redirect('/register') 
            else:
                flash("Please input correct email")
                return redirect('/register') 
        else:
            flash("password minimum 8 char, have number and letter on it")
            return redirect('/editprofile') 
    else:
        flash("password must be same with confirm")
        return redirect('/register') 







##################### API #########################


''' 
jika mengakses api menggunakan postman, pastikan untuk post datanya
 berupa FORM DATA dibagian BODY dan isikan key dan valuenya
 '''
def api_verifikasi_then_create_or_edit_user(tipe):
    name = request.form.get("name")
    email = request.form.get("email")
    telp = request.form.get("telp")
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    if password == confirm:
        if password is not None and len(password)>7 and re.search('[0-9]',password) is not None and re.search('[a-z]',password) is not None:
            if EMAIL_REGEX.match(email):
                try:
                    if tipe == "create":
                        user = create_user(email, name, password, telp)
                        return jsonify(
                            username=user.name,
                            email=user.email,
                            id=user.id
                        )
                    else:
                        user_id = request.form.get("id")
                        edit_user(user_id, name, password)
                        return jsonify(pesan="edit user berhasil")
                except:
                    return jsonify(pesan="Email already registered")
            else:
                return jsonify(pesan="Please input correct email")
        else:
            return jsonify(pesan="Password minimal 8 digit campur angka dan huruf!")
    else:
        return jsonify(pesan="Confirm password tidak sama")

from flask import Flask, session, request, redirect, render_template, flash, url_for, jsonify, json
from db.data_layer import get_user_by_id, create_user, check_login, verifikasi_then_create_or_edit_user, api_verifikasi_then_create_or_edit_user

app = Flask(__name__)
app.secret_key = 'secretuntukgigelid'



@app.route('/')
def index():
    if 'user_id' in session:
        user = get_user_by_id(session['user_id'])
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')

@app.route('/editprofile', methods=["GET", "POST"])
def editprofile():
    if request.method == 'GET':
        user = get_user_by_id(session['user_id'])
        return render_template('myprofile.html', user=user)
    else:
        verifikasi_then_create_or_edit_user('edit')
        return redirect('/') 
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if 'user_id' not in session: #check if user not yet login
        if request.method == 'POST':
            verifikasi_then_create_or_edit_user('create')
        else:
            return render_template('page_register.html')


    return redirect('/') #redirect if already login


@app.route('/login', methods=["GET", "POST"])
def login():
    if 'user_id' not in session: #check if user not yet login
        if request.method == 'POST':
            email = request.form.get("email")
            password = request.form.get("password")
            try:
                user = check_login(email, password)
                session['user_id'] = user.id
                return redirect('/')
            except:
                flash("email or password not found")
                return redirect('/login') 
                
        else:
            return render_template('page_login.html')

    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))






########################## untuk API ##########################

#untuk editprofil
@app.route('/api/editprofile', methods=["POST"])
def api_editprofile():
    return api_verifikasi_then_create_or_edit_user('edit')
    

#api untuk register
@app.route('/api/register', methods=["POST"])
def api_register():
    return api_verifikasi_then_create_or_edit_user('create')


#api untuk login
@app.route('/api/login', methods=["POST"])
def api_login():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = check_login(email, password)
        return jsonify(pesan="berhasil login")
    except:
        return jsonify(pesan="Email atau password salah")
                



if __name__ == "__main__":
    app.debug(True)
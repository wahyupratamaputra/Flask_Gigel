
### Installation

Download versi python terbaru [disini](https://www.python.org/downloads/)
jika sudah memiliki python, kemudian install Flask dengan ketik code ini di terminal
```sh
$ pip install Flask
```

clone git diatas dengan cara jalankan perintah ini di terminal
```sh
$ git clone https://github.com/wahyupratamaputra/Flask_Gigel.git
```

kemudian masuk ke directory yang telah di clone dan langsung jalankan aplikasinya dengan cara perintah dibawah:
```sh
$ cd Flask_RESTapi
$ flask run
```

kemudian akses [http://localhost:5000](http://localhost:5000)


### API Endpoint

disini semua REST API Menggunakan POST Method, jadi perlu menggunakan aplikasi pihak ke-3 seperti [Postman](https://www.getpostman.com/)

Berikut endpointnya:

| Url | Method | FormData | fungsi |
| ------ | ------ | ------ | ------ |
| /api/register | POST |name, email, telp, password, confirm | untuk daftar user
| /api/login | POST |email, password | untuk login user
| /api/editprofile | POST |id, name, password, confirm | untuk edit user


# CATATAN
*Database yang digunakan adalah sqlite dan tersimpan pada folder **db** dan jika ingin mengecek langsung databasenya bisa menggunakan [DB Browser for SQLite](https://sqlitebrowser.org/)

*aplikasi ini selain rest api, bisa diakses menggunakan browser juga dengan mengakses [http://localhost:5000](http://localhost:5000)


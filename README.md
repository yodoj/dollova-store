Tautan aplikasi pws: http://nadira-aliya-dollovastore.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Membuat sebuah proyek Django baru**
Sebelum membuat proyek Django baru, saya menyiapkan direktori baru, yaitu dollova-store. Kemudian saya mengaktifkan *virtual environment* agar *package* dan *dependencies* dari aplikasi tidak bertabrakan dengan file-file yang ada di laptop. Lalu saya membuat file requirements.txt dan menambahkan beberapa *dependencies*. Kemudian saya *install dependencies* tersebut. Untuk membuat proyek django, saya menjalankan perintah 
django-admin startproject mental_health_tracker .
Pada file settings.py, saya menambahkan "localhost", "127.0.0.1" pada bagian ALLOWED_HOSTS. Setelah selesai, saya menjalankan django dengan perintah python manage.py runserver pada cmd. Kemudian, saya membuka *link* http://localhost:8000 untuk memastikan apakah Django berhasil dibuat. Selanjutnya saya menekan ctrl + c untuk menghentikan server. Setelah itu, saya menonaktifkan *virtual environment*.

**Membuat aplikasi dengan nama main pada proyek tersebut**
Pertama, saya menjalankan perintah 
```python manage.py startapp main``` untuk membuat aplikasi. Di dalam direktori main, terdapat struktur awal aplikasi Django. Selanjutnya, saya menambahkan kode 'main' pada variabel INSTALLED_APPS di settings.py. Fungsinya untuk mendaftarkan aplikasi main di proyek.

**Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
Saya mengofigurasi *routing* URL proyek dengan menambahkan *include* dari django.urls pada urls.py di direktori dollova_store. Kemudian saya menambahkan  path('', include('main.urls')) pada variabel urlpatterns untuk mengarahkan tampilan main.

**Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib**
Model bertanggung jawab dalam mengelola data aplikasi. Berikut kode tambahan pada models.py yang saya berikan.

```
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
```

- Product adalah nama model yang didefinisikan
- *name, price, description*, dan *stock* merupakan atribut model. Tipe data yang digunakan secara berurutan adalah *CharField, IntegerField,  TextField*, dan *IntegerField*.

**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
Berikut adalah kode yang saya tambahkan pada views.py.
```
def show_main(request):
    context = {   
        'app_name':"Dollova Store", 
        'name':"Nadira Aliya Nashwa", 
        'class':'PBP C'
        }
    return render(request, "main.html", context)
```

- Fungsi show_main mengatur *request* dan mengembalikan pada tampilan yang sesuai. 
- *app_name, name*, dan *class* pada views.py adalah data-data yang disimpan pada *dictionary "context"*. 
- Terdapat return yang berfungsi untuk melakukan *render* tampilan main.html.
Kemudian saya mengubah main.html dengan kode

```html
<h1>{{app_name}}</h1>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

Sintaks kurung kurawal tersebut digunakan untuk menampilkan variabel yang telah dideklarasikan di *context*. Variabel ini disebut juga *template variables*.

**Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
Fungsi melakukan *routing* supaya aplikasi dapat diakses dari web. Pertama, saya  melakukan konfigurasi *routing* URL aplikasi main. Saya membuat file urls.py pada direktori main yang berguna mengatur rute URL. saya menambahkan kode beritkut:

```
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Fungsinya:
- impor path: mendefinisikan pola URL
- show main dan modul main.views : tampilan URL
- app_name: nama unik pola URL

**Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
Pertama, saya melakukan login pada akun PWS. Setelah menambahkan *project*, saya mendapatkan 2 informasi mengenai *Project Credentials* dan *Project Command*. Kemudian pada settings.py, saya menambahkan nadira-aliya-dollovastore.pbp.cs.ui.ac.id pada ALLOWED_HOSTS. Ini berguna agar proyek dapat diakses melalui URL PWS. Setelah melakukan git add, commit, dan push, saya menjalankan perintah dari *Project Command*. Untuk mengubah *branch* menjadi main, saya gunakan perintah git branch -M main. Pada situs PWS, kita dapat melihat status *deployment*. apabila statusnya *running*, maka proyek sudah dapat diakses.

**Membuat sebuah README.md**
Pertama saya membuat README.md pada *repository* github, tapi karena saya ingin mengerjakan README.md di VScode, saya melakukan git pull pada cmd untuk memperbarui perubahan pada github di direktori file laptop.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

*Link* bagan *request client*: ristek.link/BaganRequestClientNadira
Pertama, *client* akan melakukan *request* berupa *link* HTTP. Kalau ada *request* ke server Django, urls.py yang akan menentukan tautan tersebut akan dikirim ke mana. Misal akan dikirim ke *project*, *contact*, atau *profile*. Selanjutnya diarahkan ke views.py untuk mengelola tampilan *user*. Kemudian terdapat aktivitas membaca *read/write* data pada models.py dan views.py. Models.py berguna untuk mengurus data. *Database* berfungsi sebagai tempat penyimpanan data. Akan tetapi, untuk menambahkan, menghapus, dan mengedit data menggunakan models.py. Selanjutnya terdapat berkas html yang terhubung pada views.py. Berkas ini berfungsi untuk merancang tampilan yang nantinya akan berisi data dari models.py melalui views.py. Setelah proses berjalan dengan baik, *output* yang dihasilkan berupa *HTTP response*.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git merupakan sistem kontrol yang membantu dalam melacak perubahan pada kode dalam sebuah proyek. Adanya git membuat kita dapat melacak revisi yang telah dilakukan pada proyek. Git sangat penting dalam perangkat lunak karena memungkinkan pengguna untuk melacak perubahan kode, menyimpan versi, dan berkolaborasi tim pada sebuah proyek secara efisien.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan 
pembelajaran pengembangan perangkat lunak?

- *Open source*, artinya dapat digunakan oleh siapa saja tanpa harus mengeluarkan biaya.
- Sangat cepat, artinya Django dapat membantu *developer* dalam membuat aplikasi dalam waktu singkat.
- Fitur siap pakai, artinya Django ramah terhadap pemula.
- Fleksibel, artinya Django dapat digunakan untuk berbagai jenis aplikasi.
- Keamanan kuat, artinya Django memiliki keamanan dalam proteksi aplikasi.

5. Mengapa model pada Django disebut sebagai ORM?

Karena Django mengirimkan data sebagai ORM (*Object Relational Mapping*) agar dapat berkomunikasi secara mudah dengan basis data. Pada Django, models.py berguna sebagai penyedia data dari basis data.
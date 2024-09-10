Tautan aplikasi pws: http://nadira-aliya-dollovastore.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Membuat sebuah proyek Django baru**
Sebelum membuat proyek Django baru, saya menyiapkan direktori baru, yaitu dollova-store. Kemudian saya mengaktifkan *virtual environment* agar *package* dan *dependencies* dari aplikasi tidak bertabrakan dengan file-file yang ada di laptop. Lalu saya membuat file requirements.txt dan menambahkan beberapa *dependencies*. Kemudian saya *install dependencies* tersebut. Untuk membuat proyek django, saya menjalankan perintah 
django-admin startproject mental_health_tracker .
Pada file settings.py, saya menambahkan "localhost", "127.0.0.1" pada bagian ALLOWED_HOSTS. Setelah selesai, saya menjalankan django dengan perintah python manage.py runserver pada cmd. Kemudian, saya membuka *link* http://localhost:8000 untuk memastikan apakah Django berhasil dibuat. Selanjutnya saya menekan ctrl + c untuk menghentikan server dan menonaktifkan *virtual environment*.

**Membuat aplikasi dengan nama main pada proyek tersebut**
Pertama, saya menjalankan perintah python manage.py startapp main untuk membuat aplikasi. Di dalam direktori main, terdapat struktur awal aplikasi Django.Selanjutnya, saya menambahkan kode 'main' pada variabel INSTALLED_APPS di settings.py. Fungsinya untuk mendaftarkan aplikasi main di proyek.

**Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
Fungsi melakukan *routing* agar aplikasi dapat diakses dari web. Pertama, saya  melakukan konfigurasi *routing* URL aplikasi main. Saya membuat file urls.py pada direktori main yang berguna mengatur rute URL. saya menambahkan kode beritkut:

'''from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]'''

Fungsinya:
- impor path: mendefinisikan pola URL
- show main dan modul main.views : tampilan URL
- app_name: nama unik pola URL

Langkah selanjutnya saya mengofigurasi *routing* URL proyek dengan menambahkan *include* dari django.urls pada urls.py di direktori dollova_store. Kemudian saya menambahkan  path('', include('main.urls')) pada variabel urlpatterns untuk mengarahkan tampilan main.

**Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib**
Model bertanggung jawab dalam mengelola data aplikasi. Berikut kode tambahan pada models.py yang saya berikan.

'''class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()'''

- Product adalah nama model yang didefinisikan
- *name, price, description*, dan *stock* merupakan atribut model. Tipe data yang digunakan secara berurutan adalah *CharField, IntegerField,  TextField*, dan *IntegerField*.

**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
Berikut adalah kode yang saya tambahkan pada views.py.
'''def show_main(request):
    context = {   
        'app_name':"Dollova Store", 
        'name':"Nadira Aliya Nashwa", 
        'class':'PBP C'
        }
    return render(request, "main.html", context)'''

- Fungsi show_main mengatur *request* dan mengembalikan pada tampilan yang sesuai. 
- *app_name, name*, dan *class* pada views.py adalah data-data yang disimpan pada *dictionary "context"*. 
- Terdapat return yang berfungsi untuk melakukan *render* tampilan main.html.
Kemudian saya mengubah main.html dengan kode

'''<h1>{{app_name}}</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>'''

Sintaks kurung kurawal tersebut digunakan akan menampilkan variabel yang telah dideklarasikan di *context*. Variabel ini disebut juga *template variables*.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

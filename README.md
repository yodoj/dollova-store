Tautan aplikasi pws: http://nadira-aliya-dollovastore.pbp.cs.ui.ac.id/

**Essay Tugas 2**

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
    
    

**Essay Tugas 3**

1.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

*Data delivery* dibutuhkan dalam pengimplementasian suatu platform karena platform membutuhkan pertukaran data yang efisien sehingga data-data tersebut perlu dikirim dari satu *stack* ke *stack* lain agar platform dapat berfungsi secara optimal.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, keduanya memiliki keunggulan masing-masing. XML lebih cocok untuk menyimpan tipe data yang bervariasi karena XML lebih unggul dalam penyimpanan data yang efektif dan mudah dibaca mesin. XML sangat cocok digunakan pada data yang kompleks karena XML dapat memeriksa data secara efisien. Sedangkan JSON memiliki memiliki transmisi data yang cepat dan ukuran data lebih kecil dari XML sehingga JSON cocok digunakan untuk aplikasi seluler, API dan penyimpanan data. JSON menyediakan format pertukaran data yang lebih sederhana dan lebih cepat dalam komunikasi. JSON lebih populer dibandingkan XML karena JSON memiliki format yang lebih *readable* oleh manusia ataupun mesin. Selain itu, JSON merupakan *output* API umum dalam berbagai aplikasi dan bersifat independen dari semua bahasa pemrograman.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

*Method* ```is_valid``` berfungsi sebagai validasi input data dari suatu *form*. *Method* ini dibutuhkan agar semua data yang diinput *user* sesuai aturan yang telah ditentukan, misalnya tipe data atau batasan lain. Hal ini untuk memastikan bahwa data yang diproses aman dan sesuai dengan kebutuhan aplikasi.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

```csrf_token``` berfungsi sebagai *security* yang dibuat secara otomatis oleh Django untuk melindungi keamanan data. Bila tidak ada ```csrf_token```, penyerang dapat memanfaatkan kelemahan ini seolah-olah *user* meminta **request* pada suatu *website* dan mengekseskusi permintaan tersebut. Setelah *user* login, biasanya penyerang melakukan *phishing* dalam memasang kode serangan CSRF dalam bentuk *link website* atau gambar yang dapat diklik. Setelah *link* ditekan *user*, terdapat perintah seperti mengganti *password*, perintah transfer, dan lain sebagainya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya membuat *skeleton* sebagai kerangka *views* dengan membuat base.html pada direktori templates. Agar berkas terdaftar sebagai *template*, saya menambahkan beberapa kode pada variabel TEMPLATES di settings.py. Selanjutnya, saya menambahkan UUID pada berkas models.py agar aplikasi berjalan dengan aman. Setelah itu melakukan migrasi model.

Untuk membuat *input form*, saya membuat berkas forms.py pada direktori main dan melakukan *import* pada views.py untuk membuat dan menampilkan *form*. Kemudian membuat fungsi create_product_entry dan *entries* pada show_main supaya terlihat jika ada *request*. Agar fungsi dapat diakses, saya menambahkan *path* URL ke variabel *urlpattern* pada urls.py. Kemudian membuat create_product_entry.html dan menambahkan kode pada main.html untuk menampilkan *form* di web. 

Pada views.py, saya menambahkan fungsi show_xml show_json, show_xml_by_id, dan show_json_by_id yang memiliki *return function* berupa HttpResponse untuk mengembalikan data dalam bentuk XML dan JSON serta mengembalikan data berdasarkan ID. Selanjutnya saya melaku *routing* URL dengan menambahkan *path* URL dari masing-masing fungsi ke *urlpatterns* di urls.py. Tujuannya agar fungsi-fungsi tersebut dapat terakses.

Dalam mengakses URL dari masing-masing fungsi tersebut pada Postman, saya memastikan bahwa program sedang berjalan di *localhost*. Kemudian saya membuka aplikasi Postman dan membuat *request* baru dengan *method* GET. Lalu saya memasukkan dan mengirim URL masing-masing fungsi tersebut. Tujuannya untuk memastikan apakah data terkirim dengan baik. Misalnya http://localhost:8000/xml/ untuk semua data pada XML atau http://localhost:8000/json/[id] untuk data berdasarkan ID pada JSON. 

***Screenshot***
![alt text](<Screenshot (327).png>)

![alt text](<Screenshot (328).png>)

![alt text](<Screenshot (329).png>)

![alt text](<Screenshot (330).png>)


Sumber:

JSON vs XML - difference between data representations - AWS. aws. (n.d.). https://aws.amazon.com/compare/the-difference-between-json-xml/ 

Team. (2023, November 19). CSRF adalah: Pengertian, jenis dan cara mencegahnya. Coding Studio. https://codingstudio.id/blog/csrf-adalah/#Cara_Kerja_Serangan_CSRF 



**Essay Tugas 4**

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

Perbedaannya terletak pada argumennya. Pada HttpResponseRedirect(), argumennya hanya dapat berupa URL. Sedangkan redirect() dapat menerima argumen berupa model, *view*, atau URL. Redirect() juga dapat mengembalikan HttpResponseRedirect() sehingga redirect() lebih fleksibel.

2.  Jelaskan cara kerja penghubungan model Product dengan User!

Kita dapat menggunakan ForeignKey sebagai penghubung suatu model dan *user* melalui *relationship* antara *products* yang pasti terasosiasikan dengan seorang *user*. Kemudian mengisi *field user* dengan objek dari *request user* yang sedang terotorisasi. Selanjutnya kita dapat menyaring seluruh objek dengan hanya mengambil *products* dimana *field user* terisi dengan objek *user* yang sama dengan pengguna login pada waktu yang sama. Dengan demikian, hanya produk yang dimiliki oleh pengguna yang sedang login yang akan diambil.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

*Authentication* merupakan proses verifikasi identitas *user* saat login. Sedangkan *authorization* merupakan proses verifikasi halaman yang dapat diakses *user*. Pada Django, fungsi *authenticate* adalah fungsi bawaan Django yang dapat digunakan untuk melakukan *authentication* dan *authorization*. Saat pengguna login, sistem akan melakukan validasi pengguna yang berhak login terlebih dahulu. Saat pengguna berhasil login, sistem akan menentukan hak aksesnya.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login di *browser* melalui *session ID* yang disimpan sebagai *cookies*. Pada setiap login, *browser* mengirimkan suatu *session ID* ke server. Dengan begitu, setiap pengguna melakukan login, server akan mengingatnya. Kemudian server akan mencari informasi *state* di memori server atau *database* berdasarkan *session ID* yang didapat. Kegunaan dari *cookies* adalah sebagai memberikan konten yang lebih personal, mempermudah login, menampilkan iklan yang relevan, dan menyimpan pengaturan *website*. *Cookies* aman digunakan karena data yang disimpan tidak berubah dan tidak memperngaruhi perangkat. Namun, kita tetap harus berhati-hati tidak mengunjungi *website* yang mencurigakan karena *cookies* menyimpan data-data informasi login. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Sebelumnya saya mengimport *form* untuk mensubmit data pengguna. Kemudian saya membuat fungsi register pada views.py dan membuat berkas register.html pada direktori templates. Lalu melakukan *routing* URL di urlpatterns pada urls.py yang ada di subdirektori main. Untuk membuat halaman login, saya mengimport *authenticate*, login, dan *AuthenticationForm* untuk melakukan autentikasi serta menambahkan fungsi login_user pada views.py. Kemudian membuat berkas login.html pada direktori templates serta melakukan *routing* URL. Saya menambahkan *import* login_required agar pengguna mengakses halaman login terlebih dahulu dan potongan kode `@login_required(login_url='/login')` agar halaman main hanya dapat diakses pengguna yang sudah login di views.py. Sama seperti fungsi-fungsi sebelumnya, untuk membuat fitur logout, saya mengimport logout dan menambahkan fungsi logout_user di views.py. Kemudian saya menambahkan *button* logout di main.html serta melakukan routing URL. Setelah melakukan implementasi registrasi, login, dan logout, saya menjalankan program dan membuat 2 akun pada halaman register di *localhost*. Setelah akun terbuat, saya membuat 3 produk pada masing-masing akun.

Untuk menggunakan *cookies*, saya melakukan *import* HttpResponseRedirect, *reverse*, dan *datetime* pada views.py. Untuk melihat kapan terakhir login, saya mengganti beberapa kode pada blok if form.is_valid() di fungsi login_user. Tujuannya untuk menambahkan *cookie* berupa last_login. Pada fungsi show_main, saya menyisipkan last_login di variabel *context*. Tujuannya untuk menambahkan informasi *cookie* last_login. Kemudian saya mengubah kode pada fungsi logout_user agar saat pengguna logout, *cookie* akan terhapus. Kemudian menambahkan potongan kode pada main.html untuk menampilkan informasi *last login* di web.

Untuk menghubungkan model dengan *user*, saya menambahkan beberapa kode pada models.py. Saya menggunakan ForeignKey sebagai penghubung suatu model dan *user* melalui *relationship* antara *products*. Lalu saya mengubah beberapa kode pada fungsi create_product_entry karena *field user* akan terisi dengan objek *user* dari request.user yang menandakan bahwa objek tersebut milik *user* yang sedang login. Untuk menampilkan objek produk dari pengguna yang sedang login, saya mengubah value product_entries dan *context* pada fungsi show_main di views.py. Selanjutnya, saya melakukan *migration*

Sumber:

StackOverflow. (2014). What the difference between using Django redirect and HttpResponseRedirect? Retrieved September 24, 2024, from https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect

Vivi, S. (2021). Cookies Browser: Fungsi, Keamanan, dan Cara Mengelolanya. Retrieved September 24, 2024, from https://www.exabytes.co.id/blog/cookies-browser-adalah/
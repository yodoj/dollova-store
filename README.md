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



**Essay Tugas 5**

1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan berdasarkan prioritas:

- *Inline styles*

Memiliki prioritas tertinggi karena ditujukan untuk satu elemen tertentu dan tidak dapat diubah oleh *stylesheet* eksternal.

- *ID selectors*

*ID selectors* dirancang untuk elemen yang unik dan berbeda dari elemen lainnya. Misalnya adalah judul utama.

- *Classes selector*

*Classes selector* dirancang untuk atribut *class*. *Selector* ini biasanya digunakan untuk mecptakan beberapa elemen dengan *style* yang sama.

- *Element selector*

*Selector* ini memiliki prioritas terakhir karena menargetkan semua elemen dengan jenis yang sama, sehingga dapat menyebabkan perubahan yang tidak diinginkan pada semua elemen tersebut.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Karena *responsive design*menyesuaikan ukuran layar secara otomatis di berbagai perangkat, seperti desktop, tablet, dan ponsel. Contoh website yang responsif adalah Facebook. Tampilan Facebook dapat menyesuaikan dengan baik pada berbagai ukuran layar, misalnya pada detskop ataupun ponsel. Sedangkan website yang tidak responsif adalah SIAKNG karena jika SIAKNG dibuka di HP, layoutnya akan sesuai dengan ukuran layar laptop sehingga kita harus *zoom* saat menggunakan SIAKNG di HP.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! 

- Margin: Ruang di luar elemen yang memisahkan elemen dari elemen lainnya.

- *Border*: Garis yang mengelilingi elemen, terletak di antara margin dan *padding*.

- *Padding*: Ruang di dalam elemen, antara konten dan *border*.

Contoh implementasi:
```html
element {
  margin: 20px;
  border: 2px solid black;
  padding: 10px;
}
```

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

*Flex box* merupakan konsep *layout* CSS yang digunakan untuk mengatur elemen, *container*, dan *item* pada web. Sedangkan *grid Layout* adalah metode tata letak yang memungkinkan untuk menyusun elemen dalam baris dan kolom. Fungsinya untuk mengontrol posisi elemen dengan lebih fleksibel.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama, untuk mengimplementasikan fitur edit dan *delete*, saya membuat fungsi edit_product dan delete_product pada views.py. Lalu melakukan *routing* URL pada variabel urlpatterns di urls.py.Tujuannya agar edit dan *delete* ini dapat diakses di web. Kemudian membuat navbar.html pada folder templates untuk versi desktop dan *mobile* yang responsif. Lalu tambahkan tags *include* berupa {% include 'navbar.html' %} di create_product_entry.html, main.html, dan edit_product.html. Untuk mengkonfigurasi *static files* pada aplikasi, tambahkan *middleware* WhiteNoise pada settings.py. Setelah itu, saya mendesain login.html, register.html, create_product_entry.html, card_product.html, edit_product.html, card_info.html dan main.html dengan *tailwind*. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan pesan belum ada produk yang terdaftar dan gambar sedih yang saya simpan di folder image pada static. 

Referensi

Nufer, S. (2021, February 23). Understand margins, paddings, and Borders. How to Canvas. Retrieved Oktober 2, 2024, https://www.howtocanvas.com/create-amazing-pages-in-canvas/margins-and-padding 

Pratama, M. A. (2021). Mengenal Flexbox Pada CSS. Retrieved Oktober 2, 2024, from https://www.gamelab.id/news/817-mengenal-flexbox-pada-css

Revou. (n.d.). CSS Selectors: Jenis, Cara Membuat, dan Contoh. Retrieved Oktober 2, 2024, from https://revou.co/panduan-teknis/css-selectors

Urmaliya, A. K. (2023, June 26). Importance of CSS specificity and its best practices. Halodoc Blog. Retrieved Oktober 2, 2024, https://blogs.halodoc.io/best-practices-that-we-follow-to-avoid-specificity-issues/#:~:text=CSS%20specificity%20rule&text=Below%20are%20the%20order%20of,These%20selectors%20has%20lowest%20priority. 

W3School. (n.d.). CSS Grid Layout Module. Retrieved Oktober 2, 2024, from https://www.w3schools.com/CSS/css_grid.asp

W3School. (n.d.). HTML Responsive Web Design. Retrieved Oktober 2, 2024, from https://www.w3schools.com/html/html_responsive.asp

**Essay Tugas 6**

1.  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Manfaat dari penggunaan JavaScript adalah halaman web dapat dimanipulasi secara dinamis dan dapat meningkatkan interaksi pengguna dengan halaman web. Beberapa contoh penggunaan JavaScript dalam pengembangan web yaitu:
- Menyajikan informasi berdasarkan waktu
- Validasi form atau data
- Mengenali jenis perangkat pengguna
- Membuat HTTP *cookies*
- Merubah *styling* dan CSS suatu elemen secara dinamis.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Fungsi *await* digunakan untuk menunggu hasil dari fungsi *async*. Fungsi *async* sendiri digunakan sebagai penanda fungsi yang mengembalikan nilai secara asinkronus. Secara umum, *fetch* digunakan dalam implementasi AJAX dengan XMLHttpRequest. Apabila tidak ada *await*, eksekusi akan terus berjalan tanpa menunggu proses dari fungsi *async*.  Artinya, fungsi *async* akan berjalan secara sinkron.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Karena *decorator* csrf_exempt membuat keberadaan csrf_token tidak perlu diperiksa oleh Django saat pengiriman fungsi pada POST *request*. Csrf_token  akan menandani *view* sebagai pengecualian dari perlindungan CSRF (perlindungan yang dipastikan *middleware* di semua *view*). 

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data perlu dilakukan pada *backend* karena *backend* berfokus pada keamanan data. Pada *backend*, data pengguna diproses dan disimpan. Jika pembersihan dilakukan pada *frontend* saja, data bisa dimanipulasi oleh pengguna yang memiliki niat buruk. Melakukan pembersihan data pada *backend* memastikan bahwa data yang diterima server aman dan tidak dapat dimodifikasi sebelum masuk ke sistem.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Sebelumnya, saya menambahkan *error message* pada halaman login untuk memastikan pengguna yang login adalah pengguna yang sah. Untuk implementasi *AJAX GET*, pada views.py saya melakukan impor csrf_attempt agar Django tidak perlu memeriksa keberadaan csrf_token pada POST *request* yang dikirimkan dan impor require_POST agar fungsi hanya dapat diakses ketika POST *request* dikirimkan. Selanjutnya, saya membuat fungsi add_product_entry_ajax untuk menambahkan produk baru ke basis data dengan AJAX.

Untuk melakukan pengambilan data produk, terdapat kode ``request.POST.get("product")`` pada fungsi tersebut yang digunakan untuk mengambil data produk dari pengguna yang telah login. Kemudian agar fungsi dapat diakses di web, saya melakukan *routing* URL dengan membuat *path* create-product-entry-ajax di variabel urlpatterns dan mengimpor add_product_entry_ajax pada urls.py. 

Untuk mengubah kode *cards* data produk agar dapat mendukung AJAX GET, di HTML, saya membuat *block script* yang berisi fungsi getProductEntries yang menggunakan fetch() API ke data JSON secara asinkronus. Kemudian membuat fungsi refreshProduct untuk *refresh* data secara asinkronus. 

Kemudian saya mengimplementasikan modal (*Tailwind*) dengan meletakkan beberapa kode di bawah id=product_entry_cards. Agar modal tersebut dapat berfungsi, saya menammbahkan fungsi-fungsi JavaScript yaitu showModal dan hideModal. Agar data dapat ditambahkan oleh pengguna, saya membuat sebuah tombol baru untuk penambahan data dengan AJAX.

```
 <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-rose-700 hover:bg-rose-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
    Add New Product Entry by AJAX
  </button>
  ```

  Agar modal dapat digunakan, saya membuat fungsi JavaScript addProductEntry di main.html untuk menambahkan data berdasarkan *input* ke basis data. Pada fungsi tersebut, ```document.getElementById("productEntryForm").reset()``` digunakan untuk mengosongkan isi form modal setelah disubmit. Kemudian saya menambahkan *event listener* agar addProductEntry() dapat berjalan. 

  Kemudian saya mengimpor strip_tags pada views.py dan forms.py dan menggunakan fungsi strip_tags tersebut pada nama produk dan deskripsi. Fungsi ini berguna agar data yang disimpan di basis data adalah data yang bersih dari tag HTML. Di forms.py pada *class* ProductEntryForm, saya menambahkan fungsi clean_name dan clean_description yang akan dipanggil dalam pengecekan create_product_entry dan edit_product. Ini berguna untuk menampilkan pesan error jika penambahan produk gagal. Untuk membersihkan data lama, saya menggunakan DOMPurify.




Referensi

Trinh, L. (2024, February 19). Declare an async function without await in JavaScript?. Medium.Retrieved October 8, 2024, https://medium.com/@louistrinh/declare-an-async-function-without-await-in-javascript-751ad86789f9 

StackHawk. (2021, June 15). Defend your django app against CSRF. Retrieved October 8, 2024, https://www.stackhawk.com/blog/django-csrf-protection-guide/ 
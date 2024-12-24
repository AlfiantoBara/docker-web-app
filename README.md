# Book Management App

Aplikasi manajemen buku sederhana berbasis Flask, SQLite, dan HTML yang mendukung fitur CRUD (Create, Read, Update, Delete). Proyek ini dikemas menggunakan Docker untuk mempermudah distribusi dan deployment.

---

# Fitur Utama

- Tambah Buku : Tambahkan informasi buku baru ke dalam daftar.
- Edit Buku : Ubah informasi buku yang sudah ada.
- Hapus Buku :Hapus buku dari daftar.
- Daftar Buku : Lihat semua buku yang sudah ditambahkan.

---

## Instalasi Docker dan Cara Menjalankan Aplikasi

# Persiapan AWAL

1. Unduh dan Instal Docker

   - Kunjungi [https://www.docker.com/products/docker-desktop/] dan unduh versi Docker Desktop yang sesuai untuk sistem operasi Anda (ARM64 atau AMD64).

   - Instal Docker sesuai OS dari laptop/PC digunakan.
   - untuk Windows, silahkan buka setting → about → Device specifications → System type :

     - Jika 64-bit operating system, ARM-based processor → Download for Windows-ARM64.

     - Jika 64-bit operating system, x64-based processor → Download for Windows-AMD64.

2. Verifikasi Instalasi Docker

   - Buka terminal/command prompt dan jalankan:

     docker --version

3. Pada aplikasi docker desktop memerlukan WSL (Windows Subsystem for Linux) untuk menjalankan container Linux. Maka itu buka Windows PowerShell yang ada di komputer , lalu klik kanan untuk Run as administrator. ketikkan :
   wsl --install

   - Saran restart komputer jika diminta untuk restart

4. Siapkan struktur proyek :

   - app.py :
     adalah inti aplikasi yang menggunakan Flask untuk menangani logika backend, termasuk rute seperti penambahan, pengeditan, dan penghapusan buku, serta mengelola database SQLite menggunakan SQLAlchemy.

   - templates/index.html :
     Template HTML untuk menampilkan dan mengelola daftar buku.

   - static/style.css :
     digunakan untuk mengatur tampilan (style) halaman HTML Anda. Dalam aplikasi Anda, file ini berfungsi untuk mengatur elemen visual, seperti warna, ukuran, tata letak, font, dan efek lainnya, sehingga halaman menjadi lebih menarik secara estetika dan lebih nyaman digunakan.

   - static/script.js :
     File JavaScript untuk mengelola event seperti tombol edit.

   - requirements.txt :
     Untuk mengelola dependensi, yang mencantumkan semua library Python yang diperlukan, seperti Flask, Werkzeug dan Flask-SQLAlchemy.

   - Dockerfile :
     digunakan untuk membangun image Docker yang berisi aplikasi Flask beserta semua dependensinya.

   - docker-compose.yml :
     yang mempermudah pengelolaan dan pengaturan container, memungkinkan aplikasi berjalan dengan cepat hanya dengan satu perintah.

# Untuk folder **pycache** berisi .pyc Tidak perlu dibuat manual. Python secara otomatis membuat folder ini saat menjalankan program, dan itu berisi file yang berfungsi untuk menjalankan aplikasi dengan lebih efisien.

# File Database seperti books.db atau your_database.db Tidak perlu dibuat manual, ini terbuat secara otomatis jika di jalankan.

4. Kembali ke aplikasi docker desktop buka terminalnya dan ketikan :
   docker login

   - outputnya :
     PS C:\Users\Alfia> docker login

   USING WEB-BASED LOGIN
   To sign in with credentials on the command line, use 'docker login -u <username>'

   Your one-time device confirmation code is: GPQD-WKVV
   Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

   Waiting for authentication in the browser…

   - silahkan click ctrl+ arahkan kursor ke link login atau bisa langsung arahkan kursor ke link yang di berikan.

   - di kolom [ Enter your one-time code ] ada di bagian terminal jika sudah mengetikan docker login contoh nya : GPQD-WKVV.

   - lalu continue → Confirm

5. Setelah login, ketikkan di terminal : cd C:direktori/penyimpanan struktur proyek nya contoh : C:\Users\Alfia\docker-web-app .

6. Jika sudah ketikan lagi :

   - untuk membangun image terlebih dahulu

   PS C:\Users\Alfia\docker-web-app> docker-compose build

   - untuk menjalankan kontainer yang didefinisikan di docker-compose.yml

   PS C:\Users\Alfia\docker-web-app> docker-compose up

7. Jika tidak ingin menggunakan docker-compose , bisa menggunakan dengan command :

   - untuk membangun image

   docker build -t docker-web-app .

   - untuk menjalankan container, dengan image yang sudah di buat

   docker run -d -p 5000:5000 docker-web-app

8. Penjelasan Dockerfile :

   - FROM python:3.9-slim:
     Menggunakan base image Python versi 3.9.

   - WORKDIR /app:
     Menetapkan direktori kerja dalam kontainer.

   - COPY requirements.txt .:
     Menyalin file requirements.txt ke dalam kontainer.

   - RUN pip install -r requirements.txt:
     Menginstal semua dependensi Python dari requirements.txt.

   - COPY . .:
     Menyalin seluruh proyek ke dalam kontainer.

   - CMD ["python", "app.py"]:
     Menjalankan aplikasi Flask saat kontainer dijalankan.

9. Penjelasan docker-compose.yml :

   - version: "3":
     Menentukan versi file Docker Compose.

   - services:
     Mendefinisikan layanan yang menjalankan aplikasi.
     - web:
       Menentukan layanan yang menjalankan aplikasi web.
     - build: .:
       Membuat image Docker dari Dockerfile yang ada di direktori saat ini.
     - ports:
       Memetakan port 5000 di kontainer ke port 5000 di host.
     - volumes:
       Menyinkronkan direktori proyek antara host dan kontainer.
     - environment:
       Mendefinisikan variabel lingkungan untuk Flask.

10. Kembali ke terminal docker desktop jika ada tulisan seperti ini:

    2024-12-07 22:12:13 WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    2024-12-07 22:12:13 _ Running on http://127.0.0.1:5000
    2024-12-07 22:12:13 Press CTRL+C to quit
    2024-12-07 22:12:13 _ Restarting with stat
    2024-12-07 22:12:14 _ Debugger is active!
    2024-12-07 22:12:14 _ Debugger PIN: 133-878-567
    2024-12-07 22:12:13 _ Serving Flask app 'app'
    2024-12-07 22:12:13 _ Debug mode: on

    - Perhatikan bagian 2024-12-07 22:12:13 \* Running on http://127.0.0.1:5000

    - Klik saja http://127.0.0.1:5000 ini akan mengarahkan ke web browsernya

* Apa itu PIP?

PIP merupakan program untuk manajemen paket di Python. Tugasnya untuk menginstal, menghapus, upgrade paket Python, dll.

Paket Python itu apa?

Paket Pyhon itu merupakan sebuah modul yang berisi kode-kode python dan isi paket ini bisa kita impor ke dalam program kita.
Kamu juga bisa membuat sendiri paket Python, lalu menyebarkannya ke seluruh dunia. Sehingga programmer yang lain bisa memanfaatkannya.

* Cara Menggunakan PIP
1. pip install <nama paket>
Paket ini berisi modul untuk membuat data palsu (fake). Biasanya dipakai untuk ujicoba aplikasi.

2. pip uninstall <nama paket>
untuk melakukan unistall pada paket

3. pip install Faker --upgrade
Jika kita ingin meng-upgrade versi paket yang terinstal ke versi terbaru.

* Lokasi Penyimpanan Paket
4. python -m site
Paket-paket Python yang diinstal dengan pip akan disimpan ke dalam direktori di sistem operasi kita.
Untuk mengeceknya, silahkan ketik perintah diatas

* Melihat Informasi Paket
5. pip list
Jika kita ingin melihat daftar paket apa saja yang sudah terinstal.

6. pip show <nama paket>
Lalu untuk melihat informasi paket secara detail, kita bisa gunakan show.

* Mencari Paket Python
7. pip serach <kata kunci> 
Unutuk mencari nama paker.

* Membekukan Paket
8. pip freeze
Untuk membekukan paket, Perintah ini akan menghasilkan output nama-nama paket dan versinya yang digunakan pada aplikasi.

9. pip freeze > requirements.txt
Hasil output ini harus kita simpan ke dalam requirements.txt.
Maka akan tercipta file baru bernama requirements.txt yang berisi daftar paket dan versinya.

10. pip install -r requirements.txt
Lalu pada komputer tim yang lain, kita bisa gunakan perintah ini untuk menginstal semua paket yang terdaftar di requirements.txt.
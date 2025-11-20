Struktur Data Dictionary pada Daftar Kontak

Struktur data dictionary dalam Python merupakan sebuah wadah yang menyimpan informasi dalam bentuk pasangan key dan value. Dalam konteks program daftar kontak, dictionary digunakan untuk menghubungkan nama dengan nomor telepon secara langsung. Setiap entri memiliki key berupa nama kontak, seperti wan, wennn, dan ridwan, sedangkan nilai (value) yang menyertainya adalah nomor telepon masing-masing.

Pada program daftar kontak ini, dictionary berfungsi sebagai pusat penyimpanan data yang memudahkan proses pencarian, penambahan, pembaruan, penampilan, dan penghapusan kontak. Ketika program dijalankan, dictionary awal berisi tiga pasangan data, yaitu:

wan → 08123456789

wennn → 08211223344

ridwan → 08999888777

Pengaksesan data dilakukan dengan memanggil key, misalnya saat program menampilkan kontak wan. Untuk menambah kontak baru, dictionary cukup diberi pasangan key dan value baru, seperti ketika kontak wennn diperbarui menjadi 087654544. Proses pembaruan kontak ridwan juga dilakukan dengan mengganti value-nya menjadi 088999776.

Seluruh key dapat ditampilkan melalui contacts.keys(), seluruh value menggunakan contacts.values(), dan pasangan lengkap nama–nomor dapat ditampilkan melalui contacts.items(). Pada bagian akhir, kontak ridwan dihapus menggunakan fungsi .pop(), sehingga daftar kontak yang tersisa hanya mencakup nama-nama yang masih ada dalam dictionary tersebut.

Melalui mekanisme ini, dictionary menjadi struktur data yang sangat efektif untuk mengelola daftar kontak karena memberikan akses cepat, fleksibel, serta mudah dimodifikasi sesuai kebutuhan program.



Struktur Data Dictionary pada Program Daftar Nilai Mahasiswa

Pada program pengelolaan daftar nilai mahasiswa ini, struktur data dictionary digunakan sebagai komponen utama untuk menyimpan dan memproses informasi setiap mahasiswa. Dictionary bernama students berfungsi sebagai wadah yang menampung seluruh data dengan bentuk NIM/ID sebagai key, sementara value berupa dictionary lain yang berisi detail mahasiswa, seperti nama, nilai tugas, nilai UTS, nilai UAS, hingga nilai akhir. Melalui susunan ini, setiap entri mahasiswa dapat diakses, ditelusuri, atau diubah hanya menggunakan NIM sebagai pengenal unik.

Setiap value dari dictionary students menyimpan pasangan key–value berikut:

nama → nama mahasiswa

tugas → nilai tugas

uts → nilai UTS

uas → nilai UAS

akhir → nilai akhir hasil perhitungan

Struktur seperti ini memungkinkan program melakukan beberapa operasi penting seperti menambah data, mengubah data, menghapus data, menampilkan keseluruhan daftar, serta mencari mahasiswa berdasarkan NIM atau nama. Perhitungan nilai akhir juga memanfaatkan dictionary lain bernama WEIGHTS, yang memuat bobot penilaian: tugas 30%, UTS 35%, dan UAS 35%. Dengan memanggil fungsi hitung_nilai_akhir(), nilai akhir setiap mahasiswa dihitung otomatis berdasarkan bobot tersebut dan disimpan kembali ke dalam dictionary mahasiswa.

Penggunaan dictionary dalam program ini membuat proses manajemen data menjadi lebih terstruktur dan efisien. Sistem dapat memperbarui nilai tertentu tanpa mengubah keseluruhan data, menampilkan isi dictionary secara terformat melalui iterasi students.items(), serta menghapus entri dengan cepat menggunakan del atau .pop(). Melalui pendekatan ini, dictionary menjadi pilihan yang tepat untuk mengelola kumpulan data mahasiswa yang terdiri dari elemen-elemen kompleks namun saling berkaitan.

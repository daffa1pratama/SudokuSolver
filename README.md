# Sudoku Solver


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.


## Getting Started
### Prerequisites
Beberapa hal yang harus diinstall sebelum menjalankan program :
1. **Python**(disarankan versi 3.x.x) : https://www.python.org/downloads/
2. **PIP** : https://www.liquidweb.com/kb/install-pip-windows/
3. **Pytesseract** : https://github.com/UB-Mannheim/tesseract/wiki dan `pip install pytesseract` pada pip
4. **PIL** : `pip install Pillow` pada pip
5. **OpenCV** : `pip install opencv-python` pada pip

### How to run program
Sebelum menjalankan program, pastikan library-library di atas sudah terinstall dengan benar.
1. Buka file `FileHandler.py` pada folder src dan ubah kode program bagian `tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`. Sesuaikan dengan direktori pytesseract anda
2. Pastikan file uji berada pada folder `test` dan file uji berekstensi .png / .txt
3. Jalankan command prompt di dalam folder src dan masukkan command `python main.py <nama-file-uji.png/txt>`
4. Tunggu hingga program menampilkan hasil penyelesaian sudoku pada command prompt dan mencetak file eksternal pada folder-result dengan format `<nama-file-uji>-result.txt`


## Strategi Pencarian Solusi
Strategi yang digunakan adalah menggunakan algoritma Backtracking. Algoritma Backtracking dinilai cukup mudah diimplementasikan pada kasus persoalan Sudoku seperti ini. Algoritma Backtracking lebih cepat dalam melakukan pencarian solusi dibanding algoritma Brute Force. Hal ini karena pada algoritma Backtracking, pencarian dilakukan dengan menelusuri simpul yang berkemungkinan menghasilkan solusi. Ketika saat mencari solusi menemukan jalan buntu atau dalam kasus Sudoku ini tidak memenuhi syarat peletakan angka (tidak ada angka yang sama dalam satu baris, kolom, dan square), algoritma Backtracking akan mundur satu langkah dan mencoba kemungkinan meletakkan angka lain. Jika ditemukan lagi jalan buntu, algoritma ini akan mundur lagi terus menerus sampai solusi ditemukan. Sedangkan pada algoritma Brute Force akan mencetak semua kemungkinan simpul yang mungkin, baik itu yang memenuhi syarat peletakan angka ataupun tidak. Hal ini tentunya akan memakan waktu yang lebih lama. Dalam persoalan Sudoku ini, algoritma Backtracking memiliki kompleksitas waktu sebesar O(9^(n^2)) dan kompleksitas ruang sebesar O(n^2) dengan n adalah ukuran papan permainan Sudoku (9x9).


## Library untuk Mengekstraksi Gambar
Dalam memenuhi bonus yang diberikan, berikut adalah beberapa library yang digunakan untuk mengekstraksi gambar
### 1. PyTesseract
PyTesseract digunakan untuk mengekstraksi angka-angka yang terdapat pada papan permainan Sudoku. Library ini dapat mendeteksi tulisan yang terdapat pada gambar. Library ini cukup mudah digunakan, dengan hanya memanggil fungsi `image_to_string(image)`, library ini akan mengeluarkan tulisan yang terdapat pada gambar dalam bentuk string. Namun sayangnya, library ini bisa saja mendeteksi tulisan yang salah. Seperti contoh pada saat mengekstraksi papan Sudoku, garis-garis pembatas antar cell pada papan akan dideteksi sebagai angka 1 atau 7 karena kemiripannya, sehingga harus benar-benar yang diekstraksi adalah angka yang tepat. 
### 2. OpenCV
OpenCV adalah library untuk pemrosesan gambar. Library ini banyak digunakan oleh programmer untuk mengekstraksi gambar, tulisan, augmented reality, bahkan real-time solver Sudoku. Pada program yang dibuat, OpenCV bertindak untuk memroses gambar dan memotong gambar (cropping) pada bagian cell yang nantinya akan dilempar kepada PyTesseract untuk diproses. Proses cropping ini cukup sulit karena hardcode, sehingga perlu mengkalkulasi ukuran cropping yang sesuai. Kelebihan dari library ini adalah banyaknya fungsi-fungsi yang keren untuk memroses gambar, sehingga dapat digunakan untuk menyelesaikan persoalan yang menggunakan gambar. Namun untuk programmer pemula yang kurang terbiasa dengan pemrosesan gambar, cukup struggle dalam memelajarinya karena banyaknya fungsi yang dimiliki. Kekurangannya, sering terjadi salah ekstraksi/deteksi gambar, sehingga programmer harus cukup jeli untuk melakukannya.


## Referensi
1. [Python Sudoku Solver - Computerphile](https://www.youtube.com/watch?v=G_UYXzGuqvM)
2. [Sudoku Solver using OCR - tej17](https://github.com/tej17/Sudoku-Solver-using-OCR/blob/master/sudoku.py)
3. [OCR with Python, OpenCV and PyTesseract](https://medium.com/@jaafarbenabderrazak.info/ocr-with-tesseract-opencv-and-python-d2c4ec097866)
4. Stackoverflow


## Author
Daffa Pratama Putra / 13518033

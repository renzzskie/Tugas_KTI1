# Tugas_KTI1
Tugas BAGIAN 3 - ENIGMA MACHINE

Sebuah pesan telah dienkripsi menggunakan mesin Enigma dengan
konfigurasi berikut (konfigurasi ini unik untuk Anda):

  Urutan rotor (kanan ke kiri) : II, III, I
  Ring setting (kanan ke kiri) : P, M, H
  Posisi awal (kanan ke kiri)  : L, G, F
  Plugboard                    : R-X, G-A
  Reflector                    : B (standar)

Ciphertext:
    IGSLGGHXWYRZGSHUCOHYXGCPJKYVVFDZIBYNXYFFSJ

Tugas Anda:
  a. Dekripsikan pesan di atas. Anda boleh mengerjakan manual langkah
     demi langkah, ATAU menulis program (Python/lainnya) yang
     mensimulasikan mesin Enigma sesuai konfigurasi di atas.
  b. Jika Anda menulis program, lampirkan kode sumbernya.

Berdasarkan konfigurasi pada soal, dekripsi dilakukan dengan mensimulasikan mesin Enigma menggunakan tiga rotor dengan urutan II, III, I dari kanan ke kiri, ring setting P, M, H, posisi awal L, G, F, plugboard R-X dan G-A, serta reflector B. 
Pada setiap karakter, rotor kanan bergerak terlebih dahulu dan mekanisme double stepping diterapkan pada rotor tengah dan kiri. 
Setelah itu karakter melewati plugboard, rotor kanan, rotor tengah, rotor kiri, reflector, kemudian kembali melalui rotor kiri, rotor tengah, rotor kanan dan plugboard. 
Hasil simulasi menghasilkan plaintext :
HALORENDYNIMFDSELAMATMENGERJAKANSOALENIGMA
Hasil tersebut diperoleh langsung dari simulasi Enigma
berdasarkan konfigurasi yang diberikan pada soal.

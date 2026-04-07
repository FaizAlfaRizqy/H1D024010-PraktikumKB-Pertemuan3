# Tugas Praktikum Kecerdasan Buaatan 

Repository ini berisi dua implementasi sistem fuzzy menggunakan library scikit-fuzzy pada tugas Praktikum Kecerdasan Buatan Pertemuan ke-3.

## Identitas
- Nama: M. Umar Faiz Alfa Rizqy
- NIM: H1D024010
- Shift baru: E
- Shift lama: H

## Struktur Utama
- SOAL1.py: Tugas 1, simulasi fuzzy untuk rekomendasi setok makanan.
- SOAL2.py: Tugas 2, sistem fuzzy kepuasan pelayanan berbasis 4 input dan 1 output.

## Tugas 1 - kerjaan2kabe.py
### Tujuan
Menentukan nilai setok makanan berdasarkan:
- terjual
- permintaan
- harga
- profit

Output:
- setok

### Gambaran Sistem
- Input fuzzy:
  - terjual: rendah, sedang, tinggi
  - permintaan: rendah, sedang, tinggi
  - harga: murah, sedang, mahal
  - profit: rendah, sedang, tinggi
- Output fuzzy:
  - setok: sedang, banyak

## Tugas 3 - kerjaan3kb.py
### Tujuan
Menentukan tingkat kepuasan pelayanan berdasarkan:
- kejelasan informasi
- kejelasan persyaratan
- kemampuan petugas
- ketersediaan sarpras

Output:
- kepuasan pelayanan

### Gambaran Sistem
- Input fuzzy:
  - informasi: tidak_memuaskan, cukup_memuaskan, memuaskan
  - persyaratan: tidak_memuaskan, cukup_memuaskan, memuaskan
  - petugas: tidak_memuaskan, cukup_memuaskan, memuaskan
  - sarpras: tidak_memuaskan, cukup_memuaskan, memuaskan
- Output fuzzy:
  - pelayanan: tidak_memuaskan, kurang_memuaskan, cukup_memuaskan, memuaskan, sangat_memuaskan
- Basis aturan:
  - 81 aturan eksplisit (aturan1 sampai aturan81)
  - disusun dari kombinasi 3 x 3 x 3 x 3


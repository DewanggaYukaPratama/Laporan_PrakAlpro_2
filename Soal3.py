# Input gaji perjam dari pengguna
gaji_jam = float(input("Masukkan gaji per jam yang Anda inginkan: "))\

#Input jam kerja perminggu
jam_minggu = int(input("Masukkan jumlah jam kerja yang akan dilakukan dalam 1 minggu: "))

# Menghitung pendapatan sebelum terkena pajak/penghasilan kotor
total_jam = jam_minggu * 5  # Total jam kerja selama 5 minggu
penghasilan_kotor = gaji_jam * total_jam

# Menghitung pajak yang harus dibayarkan
persen_pajak = 0.14 #14% pajak selama kerja
total_pajak = penghasilan_kotor * persen_pajak

# Menghitung pendapatan setelah pajak/penghasilan bersih
penghasilan_bersih = penghasilan_kotor - total_pajak

# Menghitung pengeluaran budi untuk keperluan lain-lain
baju_aksesoris = 0.10 * penghasilan_bersih
alat_tulis = 0.01 * penghasilan_bersih
total_donasi = 0.25 * penghasilan_bersih
anak_yatim = 0.3 * total_donasi
kaum_duafa = 0.7 * total_donasi

# Menampilkan hasil perhitungan
print("Pendapatan Budi sebelum pajak/kotor:", penghasilan_kotor)
print("Pendapatan Budi setelah pajak/bersih:", penghasilan_bersih)
print("Pengeluaran untuk baju dan aksesoris:", baju_aksesoris)
print("Pengeluaran untuk alat tulis:", alat_tulis)
print("Pengeluaran untuk sedekah:", total_donasi)
print("Jumlah uang yang akan diterima anak yatim:", anak_yatim)
print("Jumlah uang yang akan diterima kaum dhuafa:", kaum_duafa)
#Membuat Inputan dari user untuk menentukan tinggi dan bmi yang diinginkan 
tinggi_badan = float(input("Masukkan tinggi badan (dalam meter): "))
bmi_harapan = float(input("Masukkan nilai BMI yang diharapkan: "))

#Proses hitungan untuk mencari berat badan yang diperlukan untuk memenuhi inputan yang diinginkan user
berat_badan_diperlukan = bmi_harapan * (tinggi_badan**2)


print(f"Berat badan yang diperlukan adalah {berat_badan_diperlukan:.2f} kg")

# Fungsi untuk konversi mata uang
def konversi_mata_uang(jumlah, kurs):
    hasil_konversi = jumlah * kurs
    return hasil_konversi

# Daftar kurs mata uang
kurs_mata_uang = {
    "USD": 1.18, #Contoh kurs untuk USD ke EUR
    "GBP": 0.88, # Contoh kurs untuk GBP ke EUR
    "JPY": 130.52 # Contoh kurs untuk JPY ke EUR
}

while True:
    jumlah_uang = float(input("Masukkan jumlah uang: "))
    mata_uang_asal = input("Masukkan kode mata uang asal (USD, GBP, JPY, dll.): ").upper()
    mata_uang_tujuan = input("Masukkan kode mata uang tujuan (USD, GBP, JPY, dll.): ").upper()

# Memeriksa apakah mata uang asal dan tujuan valid
    if mata_uang_asal not in kurs_mata_uang or mata_uang_tujuan not in kurs_mata_uang:
        print("Kode mata uang tidak valid.")
    else:
# Mengambil kurs konversi
        kurs_konversi = kurs_mata_uang[mata_uang_tujuan] / kurs_mata_uang[mata_uang_asal]

# Memanggil fungsi konversi_mata_uang
        hasil_konversi = konversi_mata_uang(jumlah_uang, kurs_konversi)

# Menampilkan hasil konversi
        print(f"{jumlah_uang} {mata_uang_asal} setara dengan {hasil_konversi} {mata_uang_tujuan}")
        
        ulang = input("Apakah Anda ingin melakukan konversi lagi? (y/n): ").lower()
    if ulang != 'y':
        break
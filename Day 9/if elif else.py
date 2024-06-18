# Meminta input dari pengguna
nilai = int(input("Masukkan nilai ujian: "))

# Memeriksa nilai dan menentukan kategori
if nilai >= 85:
    print("Nilai Anda adalah A.")
elif nilai >= 70:
    print("Nilai Anda adalah B.")
elif nilai >= 55:
    print("Nilai Anda adalah C.")
elif nilai >= 40:
    print("Nilai Anda adalah D.")
else:
    print("Nilai Anda adalah E.")

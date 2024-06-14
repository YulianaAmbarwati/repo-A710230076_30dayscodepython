#Fungsi input()akan membaca menjadi string
jarak = input("Masukkan nilai jarak dalam kilometer :")
print(type(jarak))

#ubah string ke int untuk menjalankan operasi matematika
jarak_meter = int(jarak) * 1000

print(f"jarak kamu dalam satuan meter adalah : {jarak_meter} m")
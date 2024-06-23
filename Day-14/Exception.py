try:
    # Memasukkan angka dan melakukan pembagian
    num = int(input("Masukkan angka:"))
    result = num / 10

except ZeroDivisionError:
    print("Error: Tidak dapat membagi dengan nol.")

except ValueError:
    print("Error: Input harus berupa angka.")

else:
    print(f"Hasil pembagian adalah: {result}")

finally:
    print("Operasi selesai.")
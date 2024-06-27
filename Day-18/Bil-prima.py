def apakah_prima (bilangan_bulat):
     if bilangan_bulat > 1 :
         for i in range (2, int(bilangan_bulat/2) + 1):
              if (bilangan_bulat % i) ==0 :
                   return "Bukan Bilangan Prima"
         else:
             return "Bilangan Prima"
     else: 
          return"Bukan Bilangan Prima"
     
bilangan_bulat = int(input("Masukkan Bilangan:"))
hasil = apakah_prima (bilangan_bulat)
print(hasil)
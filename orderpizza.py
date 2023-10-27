print('\nSelamat datang di Pizza Hut')
print('\nSilahkan pilih menu topping pizza anda :')
print('- Frankfurter')
print('- Meat Monsta')
print('- Super Supreme')
print('- Super Supreme Chicken')

topping = str(input('Masukkan menu pilihan anda: '))

if topping == 'Frankfurter':
    nama_topping = 'Frankfurter'
    
elif topping == 'Meat Monsta':
    nama_topping = 'Meat Monsta'
    
elif topping == 'Super Supreme':
    nama_topping = 'Super Supreme'
    
elif topping == 'Super Supreme Chicken':
    nama_topping = 'Super Supreme Chicken'
else :
    print("Pilihan Anda tidak valid. Silahkan ulangi program.")

print("Silahkan pilih crust pizza Anda: ")
print("- Pan Pizza")
print("- CheesyBites")
print("- Crowncrust")
print("- StuffedCrust")

crust = str(input("Masukkan pilihan crust pizza Anda: "))

if crust in ['Pan Pizza', 'CheesyBites', 'Crowncrust', 'StuffedCrust']:
    harga_crust = 12000
else: print("Pilihan Anda tidak valid. Silahkan ulangi program.")

print("Silahkan pilih ukuran pizza Anda: ")
print("- Personal")
print("- Medium")
print("- Large") 

Ukuran = str(input("Masukkan pilihan Ukuran pizza Anda: "))

if Ukuran == "Personal":
 harga_ukuran = 10000
elif Ukuran == "Medium":
  harga_ukuran = 15000
elif Ukuran == "Large":
  harga_ukuran = 20000
else: print("Ukuran yang anda masukkan tidak valid.")

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

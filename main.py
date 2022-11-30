namaBuku = "null"
stok = 0
jumlahBuku = 0
status = "Tidak Aman"
hargaBuku =  int(0)
kodeBuku = str.upper(input('Masukkan kode : '))
validasi = 'Y'

# FISIKA
if kodeBuku == "FSK01":
    jumlahBuku = 1
    kodeBuku = "FSK01"
    namaBuku = "Fisika"
    hargaBuku = 35000
    hargaJual = hargaBuku+(12.5/100*hargaBuku)
    stok = 25
    stokAman = int(input("Masukkan stok aman : "))
    if stokAman <= 25 :
        status = "Stok Aman"
        validasi = str.upper(input('Masukkan Data Lagi? [Y/T] : '))
        if validasi == 'Y':
            jumlahBuku  == jumlahBuku + 1
            kodeBuku = str.upper(input('Masukkan kode : '))
            # KIMIA
            if kodeBuku == "KIM02":
                namaBuku = "Kimia"
                hargaBuku = 40000
                hargaJual = hargaBuku+(15/100*hargaBuku)
                stok = 40
                stokAman = int(input("Masukkan stok aman : "))
                if stokAman <= 40 :
                    status = "Stok Aman"
                    validasi = str.upper(input('Masukkan Data Lagi? [Y/T] : '))
                    if validasi == 'Y':
                        jumlahBuku  == jumlahBuku + 1
                        kodeBuku = str.upper(input('Masukkan kode : '))
                else:
                    jumlahBuku  == jumlahBuku + 1
                    status ="Tidak Aman"
        else:
            jumlahBuku  == jumlahBuku + 1
            print('jumlah buku =', jumlahBuku)
    else:
        status ="Tidak Aman"
    
# KIMIA
# elif kodeBuku == "KIM02":
#     namaBuku = "Kimia"
#     hargaBuku = 40000
#     hargaJual = hargaBuku+(15/100*hargaBuku)
#     stok = 40
#     stokAman = int(input("Masukkan stok aman : "))
#     if stokAman <= 40 :
#         status = "Stok Aman"
#     else:
#         status ="Tidak Aman"

# BIOLOGI
# elif kodeBuku == "BIG03":
#     namaBuku = "Biologi"
#     hargaBuku = 50000
#     hargaJual = hargaBuku+(15/100*hargaBuku)
#     stok = 10 
#     stokAman = int(input("Masukkan stok aman : "))
#     if stokAman <= 10 :
#         status = "Stok Aman"
#     else:
#         status ="Tidak Aman"

# MTK
# elif kodeBuku == "MTK04" :
#     namaBuku = "Matematika"
#     hargaBuku = 45000
#     hargaJual = hargaBuku+(12.5/100*hargaBuku)
#     stok = 7
#     stokAman = int(input("Masukkan stok aman : "))
#     if stokAman <= 7 :
#         status = "Stok Aman"
#     else:
#         status ="Tidak Aman"

# BINDONESIA
# elif kodeBuku == "BIN05":
#     namaBuku = "Bindonesia"
#     hargaBuku = 42500
#     hargaJual = hargaBuku+(12.5/100*hargaBuku)
#     stok = 22
#     stokAman = int(input("Masukkan stok aman : "))
#     if stokAman <= 22 :
#         status = "Stok Aman"
#     else:
#         status ="Tidak Aman"

else :
    print("Kode buku salah")
    kodeBuku = str.upper(input('Masukkan kode : '))

# print("Jumlah Buku = ", jumlahBuku)
# print("")

print(40*("-"))
kode_buku = input('Masukkan Kode Barang   : ')
kode_buku = kode_buku.upper()
stok_aman = int(input('Masukkan Stok Aman     : '))
juml_dt_buku = 0
status_aman = 0
fisika = 0
kimia = 0
biologi = 0
matematika = 0
indonesia = 0
if(kode_buku == "FSK01"):
    nama_buku  = "FISIKA"
    harga_beli = 35000
    harga_jual = harga_beli + (harga_beli * 0.125)
    stok       = 25
    fisika     = stok_aman
    juml_dt_buku += 1  
    if(stok_aman >= stok):
        status_aman += 1
    else:
        status_aman = 0
elif(kode_buku == "KIM02"):
    nama_buku   = "KIMIA"
    harga_beli  = 40000
    harga_jual  = harga_beli + (harga_beli * 0.15)
    stok        = 40
    kimia       = stok_aman
    juml_dt_buku += 1
    if(stok_aman >= stok):
        status_aman += 1
    else:
        status_aman = 0
elif(kode_buku == "BIG03"):
    nama_buku   = "BIOLOGI"
    harga_beli  = 50000
    harga_jual  = harga_beli + (harga_beli * 0.15)
    stok        = 10
    biologi = stok_aman
    juml_dt_buku += 1
    if(stok_aman >= stok):
        status_aman += 1
    else:
        status_aman = 0
elif(kode_buku == "MTK04"):
    nama_buku   = "MATEMATIKA"
    harga_beli  = 45000
    harga_jual  = harga_beli + (harga_beli * 0.125)
    stok        = 7
    matematika  = stok_aman
    juml_dt_buku += 1
    if(stok_aman >= stok):
        status_aman += 1
    else:
        status_aman = 0
elif(kode_buku == "BIN05"):
    nama_buku   = "BAHASA INDONESIA"
    harga_beli  = 42500
    harga_jual  = harga_beli + (harga_beli * 0.125)
    stok        = 22
    indonesia = stok_aman
    juml_dt_buku += 1
    if(stok_aman >= stok):
        status_aman += 1
    else:
        status_aman = 0
else:
    print("Buku Tidak Tersedia")

print("Nama Barang            :",nama_buku)
print(f'Harga Beli             : Rp { harga_beli:,}')
print(f'Harga Jual             : Rp { harga_jual:,}')
print("Stok                   :",stok)
print("Stok Aman              :",stok_aman)
if(status_aman > 0):
    print("Status                 : Aman")
    print(40*("-"))
else:
    print("Status                 : Tidak Aman")
    print(40*("-"))

 
pilihan = input("Mau Input Data Lagi Gak [Y/T] ? : ")
print(40*("-"))
juml_dt_buku = juml_dt_buku
status_aman  = status_aman
print
while(pilihan == "Y"):
    kode_buku = input('Masukkan Kode Barang   : ')
    kode_buku = kode_buku.upper()
    stok_aman   = int(input('Masukkan Stok Aman     : '))
    if(kode_buku == "FSK01"):
        nama_buku   = "FISIKA"
        harga_beli  = 35000
        harga_jual  = harga_beli + (harga_beli * 0.125)
        stok        = 25
        fisika = stok_aman
        juml_dt_buku += 1  
        if(stok_aman >= stok):
            status_aman += 1
        else:
            status_aman = 0
    elif(kode_buku == "KIM02"):
        nama_buku   = "KIMIA"
        harga_beli  = 40000
        harga_jual  = harga_beli + (harga_beli * 0.15)
        stok        = 40
        kimia = stok_aman
        juml_dt_buku += 1
        if(stok_aman >= stok):
            status_aman += 1
        else:
            status_aman = 0
    elif(kode_buku == "BIG03"):
        nama_buku   = "BIOLOGI"
        harga_beli  = 50000
        harga_jual  = harga_beli + (harga_beli * 0.15)
        stok        = 10
        biologi = stok_aman
        juml_dt_buku += 1
        if(stok_aman >= stok):
            status_aman += 1
        else:
            status_aman = 0
    elif(kode_buku == "MTK04"):
        nama_buku   = "MATEMATIKA"
        harga_beli  = 45000
        harga_jual  = harga_beli + (harga_beli * 0.125)
        stok        = 7
        matematika  = stok_aman
        juml_dt_buku   += 1
        if(stok_aman >= stok):
            status_aman += 1
        else:
            status_aman = 0
    elif(kode_buku == "BIN05"):
        nama_buku   = "BAHASA INDONESIA"
        harga_beli  = 42500
        harga_jual  = harga_beli + (harga_beli * 0.125)
        stok        = 22
        indonesia   = stok_aman
        juml_dt_buku += 1
        if(stok_aman >= stok):
            status_aman += 1
        else:
            status_aman = 0
    else:
        print("Buku Tidak Tersedia")

    print("Nama Barang            :",nama_buku)
    print(f'Harga Beli             : Rp { harga_beli:,}')
    print(f'Harga Jual             : Rp { harga_jual:,}')
    print("Stok                   :",stok)
    print("Stok Aman              :",stok_aman)
    if(status_aman > 0):
        print("Status                 : Aman")
        print(40*("-"))
    else:
        print("Status                 : Tidak Aman")
        print(40*("-"))
    pilihan = input("Mau Input Data Lagi Gak [Y/T] ? :")
    print(40*("-"))


if(pilihan == "T"):
    print('Jumlah Data Buku       : ', juml_dt_buku)
    print("Stok Aman              : ", status_aman, "Buku")
    stok_tidak_aman = juml_dt_buku - status_aman
    print("Stok Tidak Aman        : ", stok_tidak_aman, "Buku, yaitu Buku dengan Kode :")
    no = 0
    if(fisika < 25  and fisika != 0):
        no += 1
        print(no, ". FISIKA")
    if(kimia < 40 and kimia != 0):
        no += 1
        print(no, ". KIMIA")
    if(biologi < 10 and biologi != 0):
        no += 1
        print(no, ". BIOLOGI")
    if(indonesia < 22 and indonesia != 0):
        no += 1
        print(no, ". BAHASA INDONESIA")
    if(matematika < 7 and matematika != 0):
        no += 1
        print(no, ". MATEMATIKA")

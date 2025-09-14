# Mini Project 1 - Sistem Informasi Inventaris Cafe Kopi Lima
# Pembuat: Alif Anugrah Ramadhan
# NIM: 2509116019
# Kelas: Sistem Informasi A

# Data inventaris (tuple: nama, jumlah, harga)
inventaris = [
    ("Espresso", 10, 10000),
    ("Cappuccino", 8, 18000),
    ("Latte", 12, 20000),
    ("Brownies", 5, 12000),
    ("Croissant", 7, 15000)
]
# info penulis 
print("=== Sistem Informasi Inventaris Cafe Kopi Lima ===")
print("Nama    : Alif Anugrah Ramadhan")
print("NIM     : 2509116019")
print("Kelas   : Sistem Informasi A")
print()

# Menu
print("Menu:")
print("1. Tambah Barang (Create)")
print("2. Lihat Barang (Read)")
print("3. Update Barang")
print("4. Hapus Barang (Delete)")
print("5. Keluar")

pilihan = input("Pilih menu (1-5): ")

# CREATE/TAMBAH
if pilihan == "1":
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah: "))
    harga = int(input("Masukkan harga: "))
    inventaris.append((nama, jumlah, harga))
    print(f"kopi '{nama}' berhasil ditambahkannn:D")

# READ
elif pilihan == "2":
    if len(inventaris) == 0:
        print("Inventaris masih kosong, kayak hati admin yg buat:(")
    else:
        print("Daftar Inventaris:")
        index = 1
        for barang in inventaris:
            print(f"{index}. Nama: {barang[0]}, Jumlah: {barang[1]}, Harga: Rp{barang[2]}")
            index += 1

# UPDATE
elif pilihan == "3":
    if len(inventaris) == 0:
        print("Inventaris kosong broo, ga bisa.")
    else:
        indeks = int(input("Masukkan nomor barang yang ingin diperbarui, yg dsruh perbarui ya bkn cari org baru ")) - 1
        if 0 <= indeks < len(inventaris):
            nama = input("Masukkan nama baru: ")
            jumlah = int(input("Masukkan jumlah baru: "))
            harga = int(input("Masukkan harga baru: "))
            inventaris[indeks] = (nama, jumlah, harga)
            print("yeyy update lagii nii, makasih admin:D")
        else:
            print("Nomor tidak valid.")

# DELETE
elif pilihan == "4":
    if len(inventaris) == 0:
        print("ups inventaris kosong, gabisa ngehapus:D.")
    else:
        indeks = int(input("Pilih barang yang ingin dihapus, TAPI INGET BUKAN KENANGAN BERSAMANYA: ")) -1
        if 0 <= indeks < len(inventaris):
            barang = inventaris.pop(indeks)
            print(f"kopi'{barang[0]}' berhasil dihapus. TAPI BUKAN KENANGAN BERSAMANYA KANN?")
        else:
            print("Nomor tidak valid.")

# EXIT
elif pilihan == "5":
    print("Terima kasih telah menggunakan sistem inventaris Cafe Kopi Lima!")

else:
    print("Pilihan tidak valid, coba lagi.")
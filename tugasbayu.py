class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

mahasiswa_list = []

def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan nomor mahasiswa: ")
    mahasiswa = Mahasiswa(nama, nim)
    mahasiswa_list.append(mahasiswa)
    print("Data mahasiswa telah ditambahkan.")
    print()

def cari_mahasiswa_by_nama():
    cari_nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
    found = False
    for mahasiswa in mahasiswa_list:
        if mahasiswa.nama.lower() == cari_nama.lower():
            print("Mahasiswa ditemukan:")
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            found = True
            break
    if not found:
        print("Mahasiswa tidak ditemukan.")
    print()

def cari_mahasiswa_by_nim():
    cari_nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
    found = False
    for mahasiswa in mahasiswa_list:
        if mahasiswa.nim == cari_nim:
            print("Mahasiswa ditemukan:")
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            found = True
            break
    if not found:
        print("Mahasiswa tidak ditemukan.")
    print()

def ubah_data_mahasiswa_by_nim():
    cari_nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ")
    found = False
    for mahasiswa in mahasiswa_list:
        if mahasiswa.nim == cari_nim:
            print("Data mahasiswa saat ini:")
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            new_nama = input("Masukkan nama baru: ")
            new_nim = input("Masukkan NIM baru: ")
            mahasiswa.nama = new_nama
            mahasiswa.nim = new_nim
            print("Data mahasiswa berhasil diubah.")
            found = True
            break
    if not found:
        print("Mahasiswa tidak ditemukan.")
    print()

# Contoh penggunaan fungsi-fungsi di atas
tambah_mahasiswa()
tambah_mahasiswa()
cari_mahasiswa_by_nama()
cari_mahasiswa_by_nim()
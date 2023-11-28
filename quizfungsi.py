#filename:quizlistmahasiswa.py
import os
import json

#deklarasi fungsi menu()
def menu():
    os.system("cls")
    
    print("==Program Data Mahasiswa==")
    print("==========================")
    print("1. Input Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")
    print("==========================")

    ops = input("masukkan pilihan :")
    return ops
    
#deklarasi fungsi cari_maahasiswa()
def cari_mahasiswa(listmahasiswa,nim):
    if nim in listmahasiswa:
        mahasiswa=listmahasiswa[nim]
        return mahasiswa
    else:
        print("NIM tidak ditemukan!")
        return False
    

#deeklarasi  fungssi tambah_maahasiswa()
def tambah_mahasiswa(listmahasiswa):
    mahasiswa={}
    nim =input("Masukkan NIM [Harus diisi]:")
    nama=input("Masukkan Nama Mahasiswa   :")
    umur=input("Masukkan Umur Mahasiswa   :")
    mahasiswa.update({"nama":nama})
    mahasiswa.update({"nim":nim})
    mahasiswa.update({"umur":int(umur)})

    #tmbah mahasiswa pada listmahasiswa
    listmahasiswa.update({mahasiswa["nim"]:mahasiswa})
    with open('data.json', 'w') as f:
        json.dump(listmahasiswa,f)
    return listmahasiswa


def hapus_mahasiswa(listmahasiswa):
    nim=input("Masukkan NIM data mahasiswa yang akan dihapus :")
    del listmahasiswa[nim]
    with open('data.json', 'w') as f:
        json.dump(listmahasiswa,f)
    return listmahasiswa
    

def ubah_mahasiswa(listmahasiswa):
    nim=input("Masukkan NIM data mahasiswa yang akan diubah :")
    mahasiswa = cari_mahasiswa(listmahasiswa, nim):
    if mahasiswa :
        nama=input("Masukkan Nama Mahasiswa   :")
        umur=input("Masukkan Umur Mahasiswa   :")
        if nama != "" :
            mahasiswa.update({"nama": nama})
        if umur != "" :
            mahasiswa.upate({"umur":int(umur)})

        listmahasiswa.update({nim:mahasiswa})
        with open('data.json', 'w') as f:
            json.dump(listmahasiswa,f)

        return listmahasiswa
    
    else:
        print("NIM tidak ditemukan!")
        return False
    

listmahasiswa={}
if os.path.exists('data.json') :
    f = open('data.json','r')
    listmahasiswa.update(json.load(f))
    print(listmahasiswa)

while True:
    pilihan = menu()
    
    if pilihan == "1":
        # tambah data dictionary
        # passs
        listmahasiswa=tambah_mahasiswa()
        
    elif pilihan=="2":
        # cari data berdasrkan nim
        #pass
        nim=input("Masukkan NIM yang dicari [tidak boleh kosong] :")
      


    elif pilihan == "3":
        # ubah data berdasarkan nim
        #pass
        
        while True:
            x_quit=input("")
            if x_quit =="":
                break

    elif pilihan=="4":
        break
    else :
        print("pilihan tidak tersedia")

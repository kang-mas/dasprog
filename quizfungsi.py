#filename:quizlistmahasiswa.py
import os
import json

listmahasiswa={}
if os.path.exists('data.json') :
    f = open('data.json','r')
    listmahasiswa.update(json.load(f))
    print(listmahasiswa)

while True:    
    os.system("cls")
    
    print("==Program Data Mahasiswa==")
    print("==========================")
    print("1. Input Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Keluar")
    print("==========================")

    pilihan = input("masukkan pilihan :")
    if pilihan == "1":
        # tambah data dictionary
        # passs
        nim =input("Masukkan NIM [Harus diisi]:")
        nama=input("Masukkan Nama Mahasiswa   :")
        umur=input("Masukkan Umur Mahasiswa   :")
        mahasiswa={}
        mahasiswa.update({"nama":nama})
        mahasiswa.update({"nim":nim})
        mahasiswa.update({"umur":int(umur)})

        #tmbah mahasiswa pada listmahasiswa
        listmahasiswa.update({mahasiswa["nim"]:mahasiswa})
        with open('data.json', 'w') as f:
            json.dump(listmahasiswa,f)

    elif pilihan=="2":
        # cari data berdasrkan nim
        #pass
        nim=input("Masukkan NIM yang dicari [tidak boleh kosong] :")
        if nim in listmahasiswa:
            mahasiswa=listmahasiswa[nim]
            print(mahasiswa)
        else:
            print("NIM tidak ditemukan!")

        while True:
            x_quit=input("")
            if x_quit =="":
                break


    elif pilihan == "3":
        # ubah data berdasarkan nim
        #pass
        nim=input("Masukkan NIM data mahasiswa yang akan diubah :")
        if nim in listmahasiswa:
            mahasiswa=listmahasiswa[nim]
            print(mahasiswa)
            nama=input("Masukkan Nama Mahasiswa   :")
            umur=input("Masukkan Umur Mahasiswa   :")
            if nama != "" :
                mahasiswa.update({"nama": nama})
            if umur != "" :
                mahasiswa.upate({"umur":int(umur)})

            listmahasiswa.update({nim:mahasiswa})
            with open('data.json', 'w') as f:
                sjson.dump(listmahasiswa,f)
        else:
            print("NIM tidak ditemukan!")
        while True:
            x_quit=input("")
            if x_quit =="":
                break

    elif pilihan=="4":
        break
    else :
        print("pilihan tidak tersedia")

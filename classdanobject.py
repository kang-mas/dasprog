#filename:classdanobject.py
import os
import json

#deklarasi class Mahassiswa
class Mahasiswa(object):
     """docstring for Mahasiswa"""
     def __init__(self, nim, nama):
        super(Mahasiswa, self).__init__()
        self.nim=nim
        self.nama=nama
        self.umur=0

    def __str__():
        return f"{self.nim} - {self.nama}"
          


#fungssi untuk membersihkan layar
def clear_screen():
    if os.name=='posix':
        os.system("clear")
    if os.name=='nt':
        os.system("cls")

#deklarasi fungsi menu()
def menu():
    clear_screen()
    
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

#deklarasi fungsi untuk menmpilkan data mahasiswa
def menampilkan_data_mahasiswa(mahasiswa):
    clear_screen()

    print("====== Data Mahasiswa =======")
    print(f"NIM     :{mahasiswa.nim}")
    print(f"Nama    :{mahasiswa.nama}")
    print(f"Umur    :{mahasiswa.umur}")
    print("=============================")

#deklarasi fungsi cari_maahasiswa()

def cari_mahasiswa(listmahasiswa,nim):
    if nim in listmahasiswa:
        mahasiswa=listmahasiswa[nim]
        menampilkan_data_mahasiswa(mahasiswa)
        return mahasiswa
    else:
        clear_screen()
        print("NIM tidak ditemukan!")
        return False

def cari_mahasiswa_by_nim(listmahasiswa):
    nim=input("Masukkan NIM yang dicari [tidak boleh kosong] :")
    for mahasiswa in listmahasiswa:
        if mahasiswa.nim == nim :
            menampilkan_data_mahasiswa(mahasiswa)
            return mahasiswa
    
    clear_screen()
    print("NIM tidak ditemukan!")
    return False
    
def cari_mahasiswa_by_nama(listmahasiswa, nama):
    nama=input("Masukkan Nama yang dicari [tidak boleh kosong] :")
    for mahasiswa in listmahasiswa:
        if mahasiswa.nama.lower() == nama.lower() :
            menampilkan_data_mahasiswa(mahasiswa)
            return mahasiswa
    
    clear_screen()
    print("Nama tidak ditemukan!")
    return False


#deeklarasi  fungssi tambah_maahasiswa()
def tambah_mahasiswa(listmahasiswa):
    nim =input("Masukkan NIM [Harus diisi]:")
    nama=input("Masukkan Nama Mahasiswa   :")
    umur=input("Masukkan Umur Mahasiswa   :")
    mahasiswa = Mahasiswa(nim,nama)
    mahasiswa.umur=umur

    #tmbah mahasiswa pada listmahasiswa
    listmahasiswa.append(mahasiswa)
    with open('data.json', 'w') as f:
        json.dump(listmahasiswa,f)

    menampilkan_data_mahasiswa(mahasiswa)
    #return listmahasiswa


def hapus_mahasiswa(listmahasiswa):
    nim=input("Masukkan NIM data mahasiswa yang akan dihapus :")
    del listmahasiswa[nim]
    with open('data.json', 'w') as f:
        json.dump(listmahasiswa,f)
    #return listmahasiswa
    

def ubah_mahasiswa(listmahasiswa):
    nim=input("Masukkan NIM data mahasiswa yang akan diubah :")
    mahasiswa = cari_mahasiswa(listmahasiswa, nim)
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

        menampilkan_data_mahasiswa(mahasiswa)
        return listmahasiswa
    
    else:
        clear_screen()
        print("NIM tidak ditemukan!")
        return False
    
def main():    
    listmahasiswa=[]
    if os.path.exists('data.json') :
        f = open('listmahasiswa.json','r')
        listmahasiswa.update(json.load(f))
        print(listmahasiswa)

    while True:
        pilihan = menu()
        
        if pilihan == "1":
            # tambah data dictionary
            # passs
            listmahasiswa=tambah_mahasiswa(listmahasiswa)
            
        elif pilihan=="2":
            # cari data berdasrkan nim
            #pass
            nim=input("Masukkan NIM yang dicari [tidak boleh kosong] :")
            cari_mahasiswa(listmahasiswa,nim)


        elif pilihan == "3":
            # ubah data berdasarkan nim
            #pass
            ubah_mahasiswa(listmahasiswa)
            

        elif pilihan=="4":
            #hhapus data maahasiswa
            hapus_mahasiswa(listmahasiswa)
            
        elif pilihan=="5":
            break
        else :
            print("pilihan tidak tersedia")

        while True:
                x_quit=input("Tekan Enter")
                if x_quit =="":
                    break

if __name__=='__main__':
    main()

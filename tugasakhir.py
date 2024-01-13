import os
class Bola:
  def __init__(self, r):
    self.r=r
  
  def volume_bola(self):
    vol =
    return vol
  
  def luas_kulit_bola(self):
    luas = 
    return luas

  def volume_setengah_bola(self):
    vol=
    return vol

def clear_screen():
    if os.name=='posix':
        os.system("clear")
    if os.name=='nt':
        os.system("cls")
def menu():
    clear_screen()
    
    print("==Program Menhitung Bola==")
    print("==========================")
    print("2. Ubah Diameter Bola")
    print("3. Tampilkan jari-jari  Bola")
    print("4. Tampilkan Volume Bola")
    print("5. Tampilkan luas kulit Bola")
    print("6. Tampilkan Volume setengah Bola")
    print("7. Tampilkan Semua ") 
    print("8. Keluar")
    print("==========================")

    ops = input("masukkan pilihan :")
    return ops
def main():
    diameter= int(input("Masukkan Diameter Bola :")) 
    bola= new Bola(diameter/2)  
    while True:
        pilihan = menu()
        
        if pilihan == "1":
          pass
                  
        elif pilihan=="2":
            diameter=int(input("Masukkan Diameter Bola :"))
            bola.r=diameter/2


        elif pilihan == "3": #Tampilkan jari-ari
            print("==Program Menhitung Bola==")
            print("==========================")
            printt(f" Jari-Jari Bola : {bola.r}")
            print("==========================")

        elif pilihan=="4": #tampikan volume bola
           
            print("==Program Menhitung Bola==")
            print("==========================")
            printt(f" Volume Bola : {bola.volume_bola()}")
            print("==========================")
        
        elif pilihan=="5": # tampilkan luas kulit bola 
          
        elif pilihan=="6": # tampilkan volume setengah bola

        elif pilihan=="7": # tapilkan  jari-jari, volume bola dan luas kulit bola  
        
        elif pilihan=="8":
             break
           
        else :
            print("pilihan tidak tersedia")

        while True:
                x_quit=input("Tekan Enter")
                if x_quit =="":
                    break

if __name__=="main__":
  main()

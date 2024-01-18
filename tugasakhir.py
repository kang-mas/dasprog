import os
import  math

class Bola:
  def __init__(self, r):
    self.r=r
  
  def volume_bola(self):
    vol =(4/3) * math.pi * self.r**3 ## solusi
    return vol
  
  def luas_kulit_bola(self):
    luas = 4 * math.pi * self.r**2 ## solusi
    return luas

  def volume_setengah_bola(self):
    vol= (2/3)  * math.pi * self.r ** 3 ## solusi 
    # vol = 0.5 * self.volume_bolla() ##  alternatif solusi
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
    bola= Bola(diameter/2)  
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
            print("==Program Menhitung Bola==")
            print("==========================")
            printt(f" Luas kulit Bola : {bola.luas_kulit_bola()}")
            print("==========================")
          
        elif pilihan=="6": # tampilkan volume setengah bola
            print("==Program Menhitung Bola==")
            print("==========================")
            printt(f" Volume setengah Bola : {bola.volume_setengah_bola()}")
            print("==========================")

        elif pilihan=="7": # tapilkan  jari-jari, volume bola dan luas kulit bola
            print("==Program Menhitung Bola==")
            print("==========================")
            printt(f" Jari-Jari Bola : {bola.r}")
            printt(f" Volume Bola : {bola.volume_bola()}")
            printt(f" Luas kulit Bola : {bola.luas_kulit_bola()}")
            print("==========================")  
        
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

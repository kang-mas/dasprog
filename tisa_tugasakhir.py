import os
import math

class Bola:
    def init(self, r):
        self.r = r

    def volume_bola(self):
        volume = (4/3) * math.pi * self.r ** 3
        return volume

    def luas_kulit_bola(self):
        luas = 4 * math.pi * self.r ** 2
        return luas

    def volume_setengah_bola(self):
        volume = (2/3) * math.pi * self.r ** 3
        return volume

    def clear_screen():
        if os.name=='posix':
           os.system("clear")
        if os.name=='nt':
           os.system("cls")

    def menu():
       clear_screen()
	   
         print ("==Program Menhitung Bola==")
         print ("========================")
         print ("2. Ubah Diameter Bola")
         print ("3. Tampilkan Jari-Jari Bola")
         print ("4. Tampilkan Volume Bola")
         print ("5. Tampilkan Luas Kulit Bola")
         print ("6. Tampilkan Volume Setengah Bola")
		 print ("7. Tampilkan Semua")
         print ("8. Keluar")
         print ("========================")
         
         ops = input("Masukkan pilihan: ")
		 return ops
       
    def main():
        diameter = int(input("Masukkan Diameter Bola: "))
        bola = Bola(diameter / 2)

    while True:
        pilihan = menu ()
		
        if pilihan=="1":
		  pass
		
        elif pilihan=="2":		
            diameter = int(input("Masukkan Diameter Bola: "))
            bola.r = diameter / 2
			
        elif pilihan=="3": #Tampilkan jari-jari
            print("==Program Menhitung Bola==")
            print("========================")
			print(f"jari-jari bola : {bola.r}")
			print("========================")
			
        elif pilihan=="4": # Tampilkan volume bola
		    print("==Program Menhitung Bola==")
            print("========================")
            print(f"Volume Bola: {bola.volume_bola()}")
            print("========================")
			
        elif pilihan=="5": #Tampilkan luas kulit bola
		    print("==Program Menhitung Bola==")
            print("========================")
            print(f"Luas Kulit Bola: {bola.luas_kulit_bola()}")
            print("========================")
			
        elif pilihan=="6": #Tampilkan volume setengah bola
		    print("==Program Menhitung Bola==")
            print("========================")
            print(f"Volume Setengah Bola: {bola.volume_setengah_bola()}")
            print("========================")
		
        elif pilihan=="7": #Tampilkan jari - jari, volume, dan luas kulit bola
            print("==Program Menhitung Bola==")
            print("========================")
			print(f"jari-jari bola : {bola.r}")
            print(f"Volume Bola: {bola.volume_bola()}")
		    print(f"Luas Kulit Bola: {bola.luas_kulit_bola()}")
            print("========================")
			
        elif pilihan=="8":
            break
			
        else:
            print("Pilihan tidak tersedia")

		while True:
            x_quit=input("")
            if x_quit =="":
                break
		
if _name_ == "_main_":
		main()

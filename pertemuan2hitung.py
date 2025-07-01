from pertemuan2 import *

def show_menu():
    print("\n")
    print("--menghitung bangun dasar--")
    print("[1]. Persegi")
    print("[2]. Persegi Panjang")
    print("[3]. Luas Segitiga")
    print("[4]. Luas Lingkaran")
    print("[5]. Keluar")
    print("---------------------------")

    menu = int(input("Pilih menu: "))
    if menu == 1:
        v1=int(input("Masukkan sisi persegi: "))
        print("Hasil Luas Persegi : ",lpersegi(v1))
    elif menu == 2:
        v1=int(input("Masukkan panjang persegi panjang: "))
        v2=int(input("Masukkan lebar persegi panjang: "))
        print("Hasil Luas Persegi Panjang : ",lperpjg(v1,v2))
    elif menu == 3:
        v1=int(input("Masukkan alas segitiga: "))
        v2=int(input("Masukkan tinggi segitiga: "))
        print("Hasil Luas Segitiga : ",lsegitiga(v1,v2))
    elif menu == 4:
        v1=int(input("Masukkan jejari lingkaran: "))
        print("Hasil Luas Lingkaran : ",llingkaran(v1))
    elif menu == 5:
        exit()
    else:
        print("Menu tidak tersedia")

if __name__ == "__main__":
    while True:
        show_menu()
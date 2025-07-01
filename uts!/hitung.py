from rumus import llingkaran, lperpjg, lpersegi, lsegitiga

def show_menu():
    print("\n")
    print("--- Menu Hitung Luas Bangun Datar ---")
    print("[1] Luas Persegi")
    print("[2] Luas Persegi Panjang")
    print("[3] Luas Segetiga")
    print("[4] Luas Lingkaran")
    print("[5] Keluar")
    print("-------------------------------------")
    
    menu =int(input("Pilihan Menu : "))

    if menu == 1 :
        v1=int(input("Masukkan sisi persegi : "))
        print("Hasil Luas Persegi : ",lpersegi(v1))
    elif menu == 2 :
        p=int(input("Masukkan panjang persegi panjang : "))
        l=int(input("Masukka lebar persegi panjang : "))
        print("Hasil Luas Persegi Panjang : ",lperpjg(p,l))
    elif menu == 3 :
        alas=int(input("Masukkan alas segitiga : "))
        tinggi=int(input("Masukkan tinggi segitiga : "))
        print("Hasil Luas Segitiga : ",lsegitiga(alas,tinggi))
    elif menu==4 :
        r=int(input("Masukkan jari-jari lingkaran : "))
        print("Hasil Luas Lingkaran : ",llingkaran(r))
    elif menu==5 :
        exit()
    else :
        print("Salah Pilih !")

if __name__=="__main__" :
    while (True):
        show_menu()
import math

def lperpjg(pjg,lbr):
    return pjg*lbr

def lpersegi (sisi):
    return sisi*sisi

def lsegitiga (alas,tinggi):
    return 0.5*alas*tinggi

def llingkaran (jejari):
    return math.pi*jejari**2
'''
s =int(input("Masukkan sisi persegi: "))
print("Hasil Luas Persegi : ",lpersegi(s))
p =int(input("Masukkan panjang persegi panjang: "))
l =int(input("Masukkan lebar persegi panjang: "))
print("Hasil Luas Persegi Panjang : ",lperpjg(p,l))
alas=int(input("Masukkan alas segitiga: "))
tinggi=int(input("Masukkan tinggi segitiga: "))
print("Hasil Luas Segitiga : ",lsegitiga(alas,tinggi))
r=int(input("Masukkan jejari lingkaran: "))
print("Hasil Luas Lingkaran : ",llingkaran(r))
'''
import math

def lperpjg(pjg,lbr):
    return pjg*lbr

def lpersegi(sisi):
    return sisi*sisi

def lsegitiga(a,t):
    return 0.5*a*t

def llingkaran(jejari):
    return math.pi*jejari**2

s=int(input("Masukkan sisi persegi : "))
print("Hasil Luas Persegi : ",lpersegi(s))
p=int(input("Masukkan panjang persegi panjang : "))
l=int(input("Masukka lebar persegi panjang : "))
print("Hasil Luas Persegi Panjang : ",lperpjg(p,l))
alas=int(input("Masukkan alas segitiga : "))
tinggi=int(input("Masukkan tinggi segitiga : "))
print("Hasil Luas Segitiga : ",lsegitiga(alas,tinggi))
r=int(input("Masukkan jari-jari lingkaran : "))
print("Hasil Luas Lingkaran : ",llingkaran(r))
print(__name__)
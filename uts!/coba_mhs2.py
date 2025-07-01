class mhs():
    pass

saya=mhs()
temanku_1=mhs()
temanku_2=mhs()

saya.nim="242011106"
saya.nama="Septa Derindra Afnan"
saya.gender="Laki-laki"
saya.prodi="TI"

temanku_1.nim="242011007"
temanku_1.nama="James Sugeng"
temanku_1.gender="Laki-laki"
temanku_1.prodi="Manajemen"

temanku_2.nim="242011123"
temanku_2.nama="Susi"
temanku_2.gender="Perempuan"
temanku_2.prodi="DKV"

print("Nama saya : "+saya.nama)
print("Kuliah di Institut Asia Malang dengan NIM : "+saya.nim+" di prodi : "+saya.prodi)
print("Nama teman saya : "+temanku_1.nama)
print(saya.__dict__)
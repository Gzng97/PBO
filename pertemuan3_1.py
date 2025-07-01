class mhs():  
    pass

saya=mhs()
temanku1=mhs()
temanku2=mhs()

saya.nim = "242011288"
saya.nama ="gesang"
saya.gender = "Laki-laki"
saya.prodi = "Teknik Informatika"

temanku1.nim = "242011289"
temanku1.nama = "budi"
temanku1.gender = "Laki-laki"
temanku1.prodi = "manajemen"

temanku2.nim = "242011290"
temanku2.nama = "siti"
temanku2.gender = "Perempuan"
temanku2.prodi = "Akuntansi"

print('nama saya:',saya.nama)
print('kuliah di asia malang dengan NIM:',saya.nim)
print('nama teman saya:',temanku1.nama)
print(saya.__dict__)